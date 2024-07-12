import argparse
import concurrent.futures
import json
import os
import queue
import threading
import time
from datetime import datetime
from functools import partial

import requests
import schedule


class VerdictJSON:

    def __init__(self):
        """
        Initializes the VerdictJSON object.

        Attributes:
        - stop_work (bool): Flag to indicate whether the work should be stopped.
        - stop_query (bool): Flag to indicate whether the query should be stopped.
        - in_service_hour (bool): Flag to indicate whether the service is currently in operation hours.
        - message_queue (Queue): A queue to store messages.
        - api_token (str): The API token.
        - verdict_id_set (set): A set to store verdict IDs.
        - json_progress_file (str): The file path for the progress JSON file.
        - json_file_path (str): The file path for the JSON files.
        - processed_counter (int): The counter for the number of processed items.
        - id_to_process (set): A set to store IDs that need to be processed.
        - output_thread (Thread): The thread object for output.
        - scheduler_thread (Thread): The thread object for scheduler.
        - check_service_hour_thread (Thread): The thread object for checking service hours.
        - listen_for_command_thread (Thread): The thread object for listening to commands.
        """
        # flags
        self.stop_work = False
        self.stop_query = False
        self.in_service_hour = False
        self.message_queue = queue.Queue() # Initialize the message queue
        # variables
        self.api_token = None
        self.verdict_id_set = set()
        self.json_file_path = "json_files"
        self.processed_counter = 0
        self.verdict_id_set = set()
        self.id_to_process_len = None
        # thread objects
        self.output_thread = None
        self.scheduler_thread = None
        self.check_service_hour_thread = None
        self.listen_for_command_thread = None


    def print_message(self, message):
        """
        Prints a message to the console.

        Args:
            message (str): The message to print.
        """
        self.message_queue.put(message)

    def handle_output_messages(self):
        """
        Handles printing of output messages from a separate thread.
        """
        while True:
            if not self.message_queue.empty():
                message = self.message_queue.get()
                print(message)
                self.message_queue.task_done() 

    def authenticate(self, user, password):
        """
        Authenticates the user with the API.

        Args:
            user (str): User name.
            password (str): User password.

        Returns:
            bool: True if authentication is successful, False otherwise.
            
        Side Effects:
            - Updates the API token.
        """
        try:
            login = {"user": user, "password": password}
            response = requests.post("https://data.judicial.gov.tw/jdg/api/Auth", json=login, timeout=10)
            response.raise_for_status()
            if response.json().get("Token") is None:
                self.print_message("Authentication failed, please check your credentials")
                return False
            self.api_token = response.json().get("Token")  # get the API token
            self.print_message("Authenticated successfully")
            self.print_message(f"API token: {self.api_token}")
            return True
        except requests.exceptions.Timeout:
            self.print_message("Timeout error during authentication")
            return False
        except requests.exceptions.RequestException as e:
            self.print_message(f"Request error during authentication: {e}")
            return False

    def load_progress(self):
        """
        Loads the progress by retrieving the existing files in the specified JSON file path.

        Returns:
            A set containing the names of the existing files without the file extension.
        """
        self.print_message("Loading progress...")
        existing_files = os.listdir(self.json_file_path)
        existing_files_set = set([file.split(".")[0] for file in existing_files])
        self.print_message("Loading verdict_id.json...")
        with open('verdict_id.json', 'r', encoding='utf-8') as f:
            verdict_id_set = set(json.load(f))
        self.print_message("comparing...")
        id_to_process = verdict_id_set.difference(existing_files_set)
        return id_to_process

    def send_request(self, verdict_id):
        """
        Sends a request to retrieve a verdict with the given verdict_id.

        Args:
            verdict_id (str): The ID of the verdict to retrieve.

        Raises:
            requests.exceptions.Timeout: If the request times out.
            requests.exceptions.RequestException: If there is an error in the request.

        IO:
            - Writes the JSON data to a file.
            - Writes the failed log to a file.

        """
        payload = {"token": self.api_token, "j": verdict_id}
        if self.stop_query or not self.in_service_hour:
            return
        try:
            response = requests.post("https://data.judicial.gov.tw/jdg/api/JDoc", json=payload, timeout=10)
            response.raise_for_status()
            json_data = response.json()
            json_file = os.path.join(self.json_file_path, f"{verdict_id}.json")
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(json_data, f, ensure_ascii=False, indent=4)
                self.print_message(f"Verdict {verdict_id} saved to {json_file}")
                self.processed_counter += 1
                self.print_message(f"Processed {self.processed_counter} / {self.id_to_process_len} verdicts")
        except requests.exceptions.Timeout:
            self.print_message(f"Timeout error for verdict {verdict_id}")
            with open("failed_log.csv", "a", encoding="utf-8") as f:
                f.write(
                    f'"{verdict_id}", {datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}, Timeout\n'
                )
            return None
        except requests.exceptions.RequestException as e:
            self.print_message(f"Request error for verdict {verdict_id}")
            with open("failed_log.csv", "a", encoding="utf-8") as f:
                f.write(
                    f'"{verdict_id}", {datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}, {e}\n'
                )
            return None
        return

    def check_service_hour(self):
        """
        Checks if the current time is within the service hours.

        """
        while not self.stop_work:
            current_time = datetime.now()
            start_time = current_time.replace(hour=0, minute=0, second=10, microsecond=0)
            end_time = current_time.replace(hour=5, minute=59, second=0, microsecond=0)
            if start_time <= current_time <= end_time:
                self.in_service_hour = True
                time.sleep(1)
            else:
                self.in_service_hour = False
                self.stop_query = True
                time.sleep(1)

    def job(self, user, password):
        """
        The main job that processes the verdicts with multithreading.
        Checks for service hours from flag and stop query from user.
        
        Args:
            user (str): The username for authentication.
            password (str): The password for authentication.  
        """
        if not self.authenticate(user, password): # Authenticate the user, if unsuccessful, return
            return
        self.print_message("Starting the task, with large quantity of data it might takes a while...")
        id_to_process = self.load_progress() # Load the progress, by retrieving the existing files in the specified JSON file path
        self.print_message("progress loaded...")
        self.id_to_process_len = len(id_to_process)
        self.print_message(f"Total verdicts to process: {len(id_to_process)}")
        with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
            futures = {executor.submit(self.send_request, verdict_id): verdict_id for verdict_id in id_to_process}
            for future in concurrent.futures.as_completed(futures):
                future.result()

    def schedule_job(self, user, password):
        """
        Schedule a task to run at a specific time every day and continuously check for service hours.

        Args:
            user (str): The username for authentication.
            password (str): The password for authentication.
        """
        animation = "|/-\\"
        idx = 0
        schedule.every().day.at("00:02").do(partial(self.job,user, password))
        while True:
            if self.stop_work:
                break
            schedule.run_pending()
            if not self.in_service_hour:
                print(
                    animation[idx % len(animation)]
                    + "Waiting for service hour, this app will resume automatically. 司法院API開放時間為00:00-06:00"
                    + animation[idx % len(animation)],
                    end="\r",
                )
                idx += 1
            time.sleep(1)

    def listen_for_command(self):
        
        # do not work right now
        # TODO fix this function
        
        """
        Listens for user commands and performs corresponding actions.

        The method continuously listens for user input and checks for specific commands.
        If the command is 'stop', it stops the task scheduler.

        Returns:
            None
        """
        while True:
            command = input()
            if command.strip().lower() == "stop":
                self.print_message("Stopping the task scheduler...")
                self.stop_work = True
                self.stop_query = True
                if self.output_thread is not None:
                    self.output_thread.join()  # Ensure output thread has finished
            elif command.strip().lower() == "g0v":
                self.print_message("everyone is no one")
                break
        return

def main():
    """
    Main function to download JSON files of verdicts from Judicial Yuan API.

    Usage: python get_verdict.py -u <username> -p <password>

    Note: The Judicial Yuan API is only available from 00:00 to 06:00.

    For more information, see https://github.com/dodgydogg/verdict_api
    """
    # Create an instance of VerdictJSON
    vj = VerdictJSON()
    os.makedirs(vj.json_file_path, exist_ok=True) # Ensure the directory for JSON files exists
    parser = argparse.ArgumentParser(
        description="Download JSON files of verdicts from Judicial Yuan API",
        usage="python get_verdict.py -u <username> -p <password>",
        epilog="司法院API開放時間為00:00-06:00\nFor more information, see https://github.com/dodgydogg/verdict_api",
    )
    parser.add_argument("-u", "--username", help="Username for authentication", required=True)
    parser.add_argument("-p", "--password", help="Password for authentication", required=True)
    args = parser.parse_args()
    
    # command line threading
    output_thread = threading.Thread(target=vj.handle_output_messages)
    output_thread.start()
    check_service_hour_thread = threading.Thread(target=vj.check_service_hour)
    check_service_hour_thread.start()
    schedule_thread = threading.Thread(target=vj.schedule_job, args=(args.username, args.password))
    schedule_thread.start()
    listen_for_command_thread = threading.Thread(target=vj.listen_for_command)
    listen_for_command_thread.start()
    # add threads to VerdictJSON instance
    vj.listen_for_command_thread = listen_for_command_thread # add listen_for_command_thread to VerdictJSON instance
    vj.output_thread = output_thread # add output_thread to VerdictJSON instance
    vj.scheduler_thread = schedule_thread # add scheduler_thread to VerdictJSON instance
    vj.check_service_hour_thread = check_service_hour_thread
    if vj.in_service_hour:
        vj.print_message("Service hour, starting the task...")
        vj.job(args.username, args.password)

if __name__ == "__main__":
    main()