# 司法院裁判書API

這是一個用來從[司法院資料開放平台](https://opendata.judicial.gov.tw/)抓取判決書的python程式。

## 功能

- 使用者需要自行從[司法院資料開放平台](https://opendata.judicial.gov.tw/)註冊帳號
- 使用者需要將需要抓取的裁判書ID存成json格式清單
- 因為司法院API僅開放午夜0到6點，程式會在時間區間內自動開始與停止
- 以json格式儲存抓取下來的裁判書
- 每次啟動會比對已經抓取的裁判書檔案，避免重複query
- 將query失敗的紀錄成failed_log.csv

## 安裝套件

使用需要以下python套件
- requests
- schedule

```
pip install -r requirements.txt
```

## 要抓取的裁判書json範例

請把要抓取的裁判書存成「verdict_id.json」，格式範例如下。

```{json}
[
    "LCDM,101,訴,6,20130102,1",
    "LCDM,101,易,3,20130117,1",
    "LCDM,101,易,8,20130104,1",
    "LCDM,102,簡,1,20130116,1",
    "LCDM,102,簡,2,20130116,1",
    "KMDM,101,易,24,20130108,1",
    "KMDM,101,易,28,20130131,1",
    "KMDM,101,易,29,20130107,1"
]
```

## 用法

請以下格式在command line中啟動程式。
```
python get_verdict.py -u 司法院資料開放平台帳號 -p 司法院資料開放平台密碼
```
抓取下來的裁判書會存在json_files資料夾中。


## 參考

- [司法院裁判書開放API 規格說明（下載PDF）](https://www.google.com/url?sa=i&url=https%3A%2F%2Fopendata.judicial.gov.tw%2Fapi%2FNewses%2F37%2Ffile&psig=AOvVaw28ogVlgknhCODOmrHucYf0&ust=1720084777638000&source=images&cd=vfe&opi=89978449&ved=0CAcQr5oMahcKEwjgzLKixYqHAxUAAAAAHQAAAAAQBA)