import os
import glob
import json


txt_file_list = glob.glob('**/*DM.刑事訴訟.txt', recursive=True)



def pair_case_info(case_dict, case_info):
    case_dict['c0案件']['c1控制碼'] = case_info[0]
    case_dict['c0案件']['c2法院'] = case_info[1]
    case_dict['c0案件']['c3案號-年'] = case_info[2]
    case_dict['c0案件']['c4案號-字別'] = case_info[3]
    case_dict['c0案件']['c5案號-號'] = case_info[4]
    case_dict['c0案件']['c6案由'] = case_info[5]
    case_dict['c0案件']['c7法官名 1'] = case_info[6]
    case_dict['c0案件']['c8法官名 2'] = case_info[7]
    case_dict['c0案件']['c9法官名 3'] = case_info[8]
    case_dict['c0案件']['c10原審法院'] = case_info[9]
    case_dict['c0案件']['c11原審案號-年'] = case_info[10]
    case_dict['c0案件']['c12原審案號-字別'] = case_info[11]
    case_dict['c0案件']['c13原審案號-號'] = case_info[12]
    case_dict['c0案件']['c14全案終結日期-年'] = case_info[13]
    case_dict['c0案件']['c15全案終結日期-月'] = case_info[14]
    case_dict['c0案件']['c16全案終結日期-日'] = case_info[15]
    case_dict['c0案件']['c17全案終結情形'] = case_info[16]
    case_dict['c0案件']['c18得上訴'] = case_info[17]
    case_dict['c0案件']['c19不得上訴'] = case_info[18]
    case_dict['c0案件']['c20得抗告'] = case_info[19]
    case_dict['c0案件']['c21不得抗告'] = case_info[20]
    case_dict['c0案件']['c22自訴人是否有律師代理'] = case_info[21]
    case_dict['c0案件']['c23裁判內容出現「消除對婦女一切形式歧視公約」'] = case_info[22]
    case_dict['c0案件']['c24裁判內容出現「兒童權利公約」'] = case_info[23]
    case_dict['c0案件']['c25裁判內容出現「兩人權公約」'] = case_info[24]
    case_dict['c0案件']['c26裁判內容出現「身心障礙者權利公約」'] = case_info[25]
    case_dict['c0案件']['c27犯選罷法終結選舉類別'] = case_info[26]
    case_dict['c0案件']['c28裁判書ID'] = case_info[27]   
    return case_dict

def pair_defendant_info(case_dict, defendant_info, n_of_defendants):
    for n in n_of_defendants:
        case_dict[f'd0被告_{n}']['d1控制碼'] = defendant_info[0]
        case_dict[f'd0被告_{n}']['d2被告終結日期-年'] = defendant_info[1]
        case_dict[f'd0被告_{n}']['d3被告終結日期-月'] = defendant_info[2]
        case_dict[f'd0被告_{n}']['d4被告終結日期-日'] = defendant_info[3]
        case_dict[f'd0被告_{n}']['d5辯護及代理'] = defendant_info[4]
        case_dict[f'd0被告_{n}']['d6保安處分-感化教育'] = defendant_info[5]
        case_dict[f'd0被告_{n}']['d7保安處分-監護'] = defendant_info[6]
        case_dict[f'd0被告_{n}']['d8保安處分-禁戒'] = defendant_info[7]
        case_dict[f'd0被告_{n}']['d9保安處分-強制工作'] = defendant_info[8]
        case_dict[f'd0被告_{n}']['d10保安處分-保護管束'] = defendant_info[9]
        case_dict[f'd0被告_{n}']['d11保安處分-強制治療'] = defendant_info[10]
        case_dict[f'd0被告_{n}']['d12保安處分-驅逐出境'] = defendant_info[11]
        case_dict[f'd0被告_{n}']['d13保安處分-安置輔導'] = defendant_info[12]
        case_dict[f'd0被告_{n}']['d14保安處分-其他'] = defendant_info[13]
        case_dict[f'd0被告_{n}']['d15裁判程序'] = defendant_info[14]
        case_dict[f'd0被告_{n}']['d16協商賠償支付對象-被害人'] = defendant_info[15]
        case_dict[f'd0被告_{n}']['d17協商賠償支付對象-公庫'] = defendant_info[16]
        case_dict[f'd0被告_{n}']['d18協商賠償支付對象-公益團體'] = defendant_info[17]
        case_dict[f'd0被告_{n}']['d19協商賠償支付對象-地方自治團體'] = defendant_info[18]
        case_dict[f'd0被告_{n}']['d20協商賠償支付金額'] = defendant_info[19]
        case_dict[f'd0被告_{n}']['d21宣告沒收適用法律-刑法第 38 條第 1 項(違禁物)'] = defendant_info[20]
        case_dict[f'd0被告_{n}']['d22宣告沒收適用法律-刑法第 38 條第 2 項(犯罪工具產物)'] = defendant_info[21]
        case_dict[f'd0被告_{n}']['d23宣告沒收適用法律-刑法第 38 條第 3 項(犯罪工具產物)'] = defendant_info[22]
        case_dict[f'd0被告_{n}']['d24宣告沒收適用法律-刑法第 38-1 條第 1 項(犯罪所得)'] = defendant_info[23]
        case_dict[f'd0被告_{n}']['d25宣告沒收適用法律-刑法第 38-1 條第 2 項(犯罪所得)'] = defendant_info[24]
        case_dict[f'd0被告_{n}']['d26宣告沒收適用法律-刑法第 38-1 條第 2 項第 1 款(犯罪所得)'] = defendant_info[25]
        case_dict[f'd0被告_{n}']['d27宣告沒收適用法律-刑法第 38-1 條第 2 項第 2 款(犯罪所得)'] = defendant_info[26]
        case_dict[f'd0被告_{n}']['d28宣告沒收適用法律-刑法第 38-1 條第 2 項第 3 款(犯罪所得)'] = defendant_info[27]
        case_dict[f'd0被告_{n}']['d29沒收資料-沒收客體'] = defendant_info[28]
        case_dict[f'd0被告_{n}']['d30沒收資料-沒收金額'] = defendant_info[29]
        case_dict[f'd0被告_{n}']['d31是否宣告緩刑'] = defendant_info[30]
        case_dict[f'd0被告_{n}']['d32宣告緩刑附記應遵收事項-向被害人道歉'] = defendant_info[31]
        case_dict[f'd0被告_{n}']['d33宣告緩刑附記應遵收事項-立悔過書'] = defendant_info[32]
        case_dict[f'd0被告_{n}']['d34宣告緩刑附記應遵收事項-向被害人支付相當數額之財產或非財產上之損害賠償'] = defendant_info[33]
        case_dict[f'd0被告_{n}']['d35向被害人支付損害賠償金額'] = defendant_info[34]
        case_dict[f'd0被告_{n}']['d36宣告緩刑附記應遵收事項-向公庫支付一定之金額'] = defendant_info[35]
        case_dict[f'd0被告_{n}']['d37向公庫支付金額'] = defendant_info[36]
        case_dict[f'd0被告_{n}']['d38宣告緩刑附記應遵收事項-向指定之政府機關（構）、行政法人、社區、公益機構或團體，提供40小時以上240小時以下之義務勞務'] = defendant_info[37]
        case_dict[f'd0被告_{n}']['d39宣告緩刑附記應遵收事項-完成戒癮治療、精神治療、心理輔導或其他適當之處遇措施'] = defendant_info[38]
        case_dict[f'd0被告_{n}']['d40宣告緩刑附記應遵收事項-保護被害人安全之必要命令'] = defendant_info[39]
        case_dict[f'd0被告_{n}']['d41宣告緩刑附記應遵收事項-預防再犯所為之必要命'] = defendant_info[40]
        case_dict[f'd0被告_{n}']['d42違反家暴法緩刑期間應遵守事項-第 38 條第 2 項第 1 款禁止實施家庭暴力'] = defendant_info[41]
        case_dict[f'd0被告_{n}']['d43違反家暴法緩刑期間應遵守事項-第 38 條第 2 項第 3 款強制遷出'] = defendant_info[42]
        case_dict[f'd0被告_{n}']['d44反家暴法緩刑期間應遵守事項第 38 條第 2 項第 2款禁止騷擾等行為'] = defendant_info[43]
        case_dict[f'd0被告_{n}']['d45違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款強制戒癮治療'] = defendant_info[44]
        case_dict[f'd0被告_{n}']['d46違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款強制精神治療'] = defendant_info[45]
        case_dict[f'd0被告_{n}']['d47違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款強制心理輔導'] = defendant_info[46]
        case_dict[f'd0被告_{n}']['d48違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款強制其他治療、輔導'] = defendant_info[47]
        case_dict[f'd0被告_{n}']['d49違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 6款其他必要保護被害人等措施'] = defendant_info[48]
        case_dict[f'd0被告_{n}']['d50違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 4款強制遠離'] = defendant_info[49]
        case_dict[f'd0被告_{n}']['d51違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款強制認知教育輔導'] = defendant_info[50]
        case_dict[f'd0被告_{n}']['d52違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款強制親職教育輔導'] = defendant_info[51]
        case_dict[f'd0被告_{n}']['d53違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款（舊法）其他更生保護事項'] = defendant_info[52]
        case_dict[f'd0被告_{n}']['d54減刑條例（年度1）'] = defendant_info[53]
        case_dict[f'd0被告_{n}']['d55減刑條例（年度2）'] = defendant_info[54]
        case_dict[f'd0被告_{n}']['d56減刑條例（年度3）'] = defendant_info[55]
        case_dict[f'd0被告_{n}']['d57減刑條例（年度4）'] = defendant_info[56]
        case_dict[f'd0被告_{n}']['d58應執行刑（1020401前）-主刑'] = defendant_info[57]
        case_dict[f'd0被告_{n}']['d59應執行刑（1020401前）-有期徒刑'] = defendant_info[58]
        case_dict[f'd0被告_{n}']['d60定應執行刑-有期徒刑得易科'] = defendant_info[59]
        case_dict[f'd0被告_{n}']['d61定應執行刑-有期徒刑不得易科逾 6 月'] = defendant_info[60]
        case_dict[f'd0被告_{n}']['d62定應執行刑-有期徒刑不得易科 6 月以下'] = defendant_info[61]
        case_dict[f'd0被告_{n}']['d63定應執行刑-拘役'] = defendant_info[62]
        case_dict[f'd0被告_{n}']['d64定應執行刑-罰金類別'] = defendant_info[63]
        case_dict[f'd0被告_{n}']['d65定應執行刑-罰金'] = defendant_info[64]
        case_dict[f'd0被告_{n}']['d66定應執行刑-無期徒刑或死刑'] = defendant_info[65]
        case_dict[f'd0被告_{n}']['d67是否為累犯'] = defendant_info[66]
        case_dict[f'd0被告_{n}']['d68是否有刑法第 91 條之 1 第 1 項審前鑑定'] = defendant_info[67]
        case_dict[f'd0被告_{n}']['d69被告終結情形'] = defendant_info[68]
        case_dict[f'd0被告_{n}']['d70上訴人別(1)'] = defendant_info[69]
        case_dict[f'd0被告_{n}']['d71上訴人別(2)'] = defendant_info[70]
    return case_dict

def pair_charge_info(case_dict, charge_info):
    case_dict['d0被告']['c0被告罪名']['c1控制碼'] = charge_info[0]
    case_dict['d0被告']['c0被告罪名']['c2刑事法令'] = charge_info[1]
    case_dict['d0被告']['c0被告罪名']['c3刑事法令:條'] = charge_info[2]
    case_dict['d0被告']['c0被告罪名']['c4刑事法令:之條'] = charge_info[3]
    case_dict['d0被告']['c0被告罪名']['c5刑事法令:條-段'] = charge_info[4]
    case_dict['d0被告']['c0被告罪名']['c6刑事法令:項'] = charge_info[5]
    case_dict['d0被告']['c0被告罪名']['c7刑事法令:項-段'] = charge_info[6]
    case_dict['d0被告']['c0被告罪名']['c8刑事法令:款'] = charge_info[7]
    case_dict['d0被告']['c0被告罪名']['c9修法年月'] = charge_info[8]
    case_dict['d0被告']['c0被告罪名']['c10被告罪名裁判結果'] = charge_info[9]
    case_dict['d0被告']['c0被告罪名']['c11宣告有期徒刑'] = charge_info[10]
    case_dict['d0被告']['c0被告罪名']['c12拘役日數'] = charge_info[11]
    case_dict['d0被告']['c0被告罪名']['c13罰金金額'] = charge_info[12]
    case_dict['d0被告']['c0被告罪名']['c14是否得易科'] = charge_info[13]
    case_dict['d0被告']['c0被告罪名']['c15是否褫奪公權'] = charge_info[14]
    case_dict['d0被告']['c0被告罪名']['c16罪犯類型-少年犯'] = charge_info[15]
    case_dict['d0被告']['c0被告罪名']['c17罪犯類型-幫助犯'] = charge_info[16]
    case_dict['d0被告']['c0被告罪名']['c18罪犯類型-未遂犯'] = charge_info[17]
    case_dict['d0被告']['c0被告罪名']['c19罪犯類型-家庭暴力'] = charge_info[18] 
    return case_dict

def pair_aggravating_info(case_dict, aggravating_info):
    case_dict['d0被告']['c0被告罪名']['a0量刑加重資料']['a1控制碼'] = aggravating_info[0]
    case_dict['d0被告']['c0被告罪名']['a0量刑加重資料']['a2量刑加重'] = aggravating_info[1]
    return case_dict

def pair_special_aggravating_info(case_dict, special_aggravating_info):
    case_dict['d0被告']['c0被告罪名']['sa0量刑特殊加重資料']['sa1控制碼'] = special_aggravating_info[0]
    case_dict['d0被告']['c0被告罪名']['sa0量刑特殊加重資料']['sa2量刑特殊加重'] = special_aggravating_info[1]
    return case_dict

for file in txt_file_list: # iterate through all txt files
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines() # read all lines in the txt file
    case_list = lines.split('#') # split the txt file into cases
    for case in case_list: # iterate through all cases
        case_dict = {} # create a case_dictionary to store the case information
        n_of_defendants = 0 # initialize the number of defendants to 0
        n_of_charges = 0 # initialize the number of charges to 0
        case_lines = case.split('\n') # split the case into lines
        for case_line in case_lines: # iterate through all lines in the case
            if case_line[0] == '0': # if the line starts with 0, it is the case information
                case_info = case_line.split('!')
            elif case_line[0] == '1': # if the line starts with 1, it is the defendant information
                defendant_info = [] # create a list to store multiple defendants' information
                n_of_defendants += 1
                defendant_info[n_of_defendants] = case_line.split('!') 
            elif case_line[0] == '1.1': # if the line starts with 1.1, it is the defendant's charge information
                charge_info = [] # create a list to store multiple charges' information
                n_of_charges += 1
                charge_info[n_of_charges] = case_line.split('!')
            elif case_line[0] == '1.1.1': # if the line starts with 1.1.1, it is the defendant's 加重量刑 information
                aggravating_info = case_line.split('!')
                
            elif case_line[0] == '1.1.2': # if the line starts with 1.1.2, it is the defendant's 減輕量刑 information
                commutation_info = case_line.split('!')
                case_dict['d0被告']['c0被告罪名']['r0量刑減輕資料']['r1控制碼'] = commutation_info[0]
                case_dict['d0被告']['c0被告罪名']['r0量刑減輕資料']['r2量刑減輕'] = commutation_info[1]
            elif case_line[0] == '1.1.3': # if the line starts with 1.1.3, it is the defendant's 特殊加重量刑 information
                special_aggravating_info = case_line.split('!')
                case_dict['d0被告']['c0被告罪名']['sa0量刑特殊加重資料']['sa1控制碼'] = special_aggravating_info[0]
                case_dict['d0被告']['c0被告罪名']['sa0量刑特殊加重資料']['sa2量刑特殊加重'] = special_aggravating_info[1]
            elif case_line[0] == '1.1.4': # if the line starts with 1.1.4, it is the defendant's 特殊減輕量刑 information
                special_commutation_info = case_line.split('!')
                case_dict['d0被告']['c0被告罪名']['sr0量刑特殊減輕資料']['sr1控制碼'] = special_commutation_info[0]
                case_dict['d0被告']['c0被告罪名']['sr0量刑特殊減輕資料']['sr2量刑特殊減輕'] = special_commutation_info[1]
            elif case_line[0] == '2': # if the line starts with 2, it is the third party information
                third_party_info = case_line.split('!')
                case_dict['c0案件']['t0第三人沒收資料']['t1控制碼'] = third_party_info[0]
                case_dict['c0案件']['t0第三人沒收資料']['t2沒收程序裁判結果'] = third_party_info[1]
                case_dict['c0案件']['t0第三人沒收資料']['t3宣告沒收適用法律-刑法第 38 條第 1 項(違禁物)'] = third_party_info[2]
                case_dict['c0案件']['t0第三人沒收資料']['t4宣告沒收適用法律-刑法第 38 條第 3 項(犯罪工具產物)'] = third_party_info[3]
                case_dict['c0案件']['t0第三人沒收資料']['t5宣告沒收適用法律-刑法第 38-1 條第 2 項(犯罪所得)'] = third_party_info[4]
                case_dict['c0案件']['t0第三人沒收資料']['t6宣告沒收適用法律-刑法第 38-1 條第 2 項第 1 款(犯罪所得)'] = third_party_info[5]
                case_dict['c0案件']['t0第三人沒收資料']['t7宣告沒收適用法律-刑法第 38-1 條第 2 項第 2 款(犯罪所得)'] = third_party_info[6]
                case_dict['c0案件']['t0第三人沒收資料']['t8宣告沒收適用法律-刑法第 38-1 條第 2 項第 3 款(犯罪所得)'] = third_party_info[7]
                case_dict['c0案件']['t0第三人沒收資料']['t9沒收資料-沒收客體'] = third_party_info[8]
                case_dict['c0案件']['t0第三人沒收資料']['t10沒收資料-沒收金額'] = third_party_info[9]

# TODO 把上面惡夢般的邏輯完成，所有pairing都以函式進行，input dict info_list 還有n_of_XXX，來對應多重的辯護人跟案由



case_dict_layout = {
        'c0案件': {
            'c1控制碼' : '',
            'c2法院' : '',
            'c3案號-年' : '',
            'c4案號-字別' : '', 
            'c5案號-號' : '', 
            'c6案由' : '', 
            'c7法官名 1' : '', 
            'c8法官名 2' : '', 
            'c9法官名 3' : '', 
            'c10原審法院' : '', 
            'c11原審案號-年' : '', 
            'c12原審案號-字別' : '', 
            'c13原審案號-號' : '', 
            'c14全案終結日期-年' : '', 
            'c15全案終結日期-月' : '', 
            'c16全案終結日期-日' : '', 
            'c17全案終結情形' : '',
            'c18得上訴' : '',
            'c19不得上訴' : '',
            'c20得抗告' : '',
            'c21不得抗告' : '',
            'c22自訴人是否有律師代理' : '',
            'c23裁判內容出現「消除對婦女一切形式歧視公約」' : '',
            'c24裁判內容出現「兒童權利公約」' : '',
            'c25裁判內容出現「兩人權公約」' : '',
            'c26裁判內容出現「身心障礙者權利公約」' : '',
            'c27犯選罷法終結選舉類別' : '',
            'c28裁判書ID' : ''
        },
        'd0被告': {
            'd1控制碼' : '',
            'd2被告終結日期-年' : '',
            'd3被告終結日期-月' : '',
            'd4被告終結日期-日' : '',
            'd5辯護及代理' : '',
            'd6保安處分-感化教育' : '',
            'd7保安處分-監護' : '',
            'd8保安處分-禁戒' : '',
            'd9保安處分-強制工作' : '',
            'd10保安處分-保護管束' : '',
            'd11保安處分-強制治療' : '',
            'd12保安處分-驅逐出境' : '',
            'd13保安處分-安置輔導' : '',
            'd14保安處分-其他' : '',
            'd15裁判程序' : '',
            'd16協商賠償支付對象-被害人' : '',
            'd17協商賠償支付對象-公庫' : '',
            'd18協商賠償支付對象-公益團體' : '',
            'd19協商賠償支付對象-地方自治團體' : '',
            'd20協商賠償支付金額' : '',
            'd21宣告沒收適用法律-刑法第 38 條第 1 項(違禁物)' : '',
            'd22宣告沒收適用法律-刑法第 38 條第 2 項(犯罪工具產物)' : '',
            'd23宣告沒收適用法律-刑法第 38 條第 3 項(犯罪工具產物)' : '',
            'd24宣告沒收適用法律-刑法第 38-1 條第 1 項(犯罪所得)' : '',
            'd25宣告沒收適用法律-刑法第 38-1 條第 2 項(犯罪所得)' : '',
            'd26宣告沒收適用法律-刑法第 38-1 條第 2 項第 1 款(犯罪所得)' : '',
            'd27宣告沒收適用法律-刑法第 38-1 條第 2 項第 2 款(犯罪所得)' : '',
            'd28宣告沒收適用法律-刑法第 38-1 條第 2 項第 3 款(犯罪所得)' : '',
            'd29沒收資料-沒收客體' : '',
            'd30沒收資料-沒收金額' : '',
            'd31是否宣告緩刑' : '',
            'd32宣告緩刑附記應遵收事項-向被害人道歉' : '',
            'd33宣告緩刑附記應遵收事項-立悔過書' : '',
            'd34宣告緩刑附記應遵收事項-向被害人支付相當數額之財產或非財產上之損害賠償' : '',
            'd35向被害人支付損害賠償金額' : '',
            'd36宣告緩刑附記應遵收事項-向公庫支付一定之金額' : '',
            'd37向公庫支付金額' : '',
            'd38宣告緩刑附記應遵收事項-向指定之政府機關（構）、行政法人、社區、公益機構或團體，提供40小時以上240小時以下之義務勞務' : '',
            'd39宣告緩刑附記應遵收事項-完成戒癮治療、精神治療、心理輔導或其他適當之處遇措施' : '',
            'd40宣告緩刑附記應遵收事項-保護被害人安全之必要命令' : '',
            'd41宣告緩刑附記應遵收事項-預防再犯所為之必要命' : '',
            'd42違反家暴法緩刑期間應遵守事項-第 38 條第 2 項第 1 款禁止實施家庭暴力' : '',
            'd43違反家暴法緩刑期間應遵守事項-第 38 條第 2 項第 3 款強制遷出' : '',
            'd44反家暴法緩刑期間應遵守事項第 38 條第 2 項第 2款禁止騷擾等行為' : '',
            'd45違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款強制戒癮治療' : '',
            'd46違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款強制精神治療' : '',
            'd47違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款強制心理輔導' : '',
            'd48違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款強制其他治療、輔導' : '',
            'd49違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 6款其他必要保護被害人等措施' : '',
            'd50違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 4款強制遠離' : '',
            'd51違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款強制認知教育輔導' : '',
            'd52違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款強制親職教育輔導' : '',
            'd53違反家暴法緩刑期間應遵守事項第 38 條第 2 項第 5款（舊法）其他更生保護事項' : '',
            'd54減刑條例（年度1）' : '',
            'd55減刑條例（年度2）' : '',
            'd56減刑條例（年度3）' : '',
            'd57減刑條例（年度4）' : '',
            'd58應執行刑（1020401前）-主刑' : '',
            'd59應執行刑（1020401前）-有期徒刑' : '',
            'd60定應執行刑-有期徒刑得易科' : '',
            'd61定應執行刑-有期徒刑不得易科逾 6 月' : '',
            'd62定應執行刑-有期徒刑不得易科 6 月以下' : '',
            'd63定應執行刑-拘役' : '',
            'd64定應執行刑-罰金類別' : '',
            'd65定應執行刑-罰金' : '',
            'd66定應執行刑-無期徒刑或死刑' : '',
            'd67是否為累犯' : '',
            'd68是否有刑法第 91 條之 1 第 1 項審前鑑定' : '',
            'd69被告終結情形' : '',
            'd70上訴人別(1)' : '',
            'd71上訴人別(2)' : '',
            'c0被告罪名' : {
                'c1控制碼' : '',
                'c2刑事法令' : '',
                'c3刑事法令:條' : '',
                'c4刑事法令:之條' : '',
                'c5刑事法令:條-段' : '',
                'c6刑事法令:項' : '',
                'c7刑事法令:項-段' : '',
                'c8刑事法令:款' : '',
                'c9修法年月' : '',
                'c10被告罪名裁判結果' : '',
                'c11宣告有期徒刑' : '',
                'c12拘役日數' : '',
                'c13罰金金額' : '',
                'c14是否得易科' : '',
                'c15是否褫奪公權' : '',
                'c16罪犯類型-少年犯' : '',
                'c17罪犯類型-幫助犯' : '',
                'c18罪犯類型-未遂犯' : '',
                'c19罪犯類型-家庭暴力' : '',
                'a0量刑加重資料' : {
                    'a1控制碼' : '',
                    'a2量刑加重' : ''
                },
                'r0量刑減輕資料' : {
                    'r1控制碼' : '',
                    'r2量刑減輕' : ''
                },
                'sa0量刑特殊加重資料' : {
                    'sa1控制碼' : '',
                    'sa2量刑特殊加重' : ''
                },
                'sr量刑特殊減輕資料' : {
                    'sr1控制碼' : '',
                    'sr2量刑特殊減輕' : ''
                }
            }
        },
        't0第三人沒收資料' : {
            't1控制碼' : '',
            't2沒收程序裁判結果' : '',
            't3宣告沒收適用法律-刑法第 38 條第 1 項(違禁物)' : '',
            't4宣告沒收適用法律-刑法第 38 條第 3 項(犯罪工具產物)' : '',
            't5宣告沒收適用法律-刑法第 38-1 條第 2 項(犯罪所得)' : '',
            't6宣告沒收適用法律-刑法第 38-1 條第 2 項第 1 款(犯罪所得)' : '',
            't7宣告沒收適用法律-刑法第 38-1 條第 2 項第 2 款(犯罪所得)' : '',
            't8宣告沒收適用法律-刑法第 38-1 條第 2 項第 3 款(犯罪所得)' : '',
            't9沒收資料-沒收客體' : '',
            't10沒收資料-沒收金額' : ''
        }
    }