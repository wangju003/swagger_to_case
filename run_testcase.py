import requests
import logging,re,json

from settings import uid_token_map


def runTest(testcase):
    errorCase =[]
    correlationDict = {}
    #读取数据库中的case
    for i in testcase:
        if i[9].replace("\n", "").replace("\r", "") != "Yes":
            continue
        # num = str(i.index)
        city=i[0].replace("\n", "").replace("\r", "")
        api_purpose = i[1].replace("\n", "").replace("\r", "")
        request_url = i[2].replace("\n", "").replace("\r", "")

        # request_method = i[3].replace("\n", "").replace("\r", "")
        request_data_type = i[4].replace("\n", "").replace("\r", "")
        request_data = i[5].replace("\n", "").replace("\r", "").replace("'", '"')
        check_point = i[7]
        correlation = i[8].replace("\n", "").replace("\r", "").split(";")
        creater =i[10]
        project = i[11]

        api_host='appts.5i5j.com'


            #检查correlationDict是否包含 入参中需要使用的变量,如果有,使用correlationDict中保存的值
        for keyword in correlationDict:
            if request_data.find(keyword) > 0:
                request_data = request_data.replace(keyword, str(correlationDict[keyword]))

        status,resp = interfaceTest(city,api_purpose,api_host,request_url,request_data,check_point)
        #print(resp)
        #记录响应状态不等200的接口
        if status !=200:
            request_url = "https://" + api_host + request_url

            errorCase.append(( api_purpose, str(status), request_url, resp[:40], creater))
            continue
        #检查是否有关联参数,如果有将关联参数保存到correlationDict
        for j in range(len(correlation)):
            param = correlation[j].split("=")
            if len(param)==2:
                if param[1] == "" or not re.search(r'^\[',param[1]) or not re.search(r'\]',param[1]):
                    logging.error(+api_purpose+"关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！")
                    continue
                value = json.loads(resp)

                for key in param[1][1:-1].split("]["):
                    try:
                        temp = value[int(key)]
                    except:
                        try:
                            temp = value[key]
                        except:
                            break
                    value = temp
                correlationDict[param[0]] = value
    return errorCase

#执行接口测试
def interfaceTest(city,api_purpose,api_host,request_url,request_data,check_point):
    try:
        request_data = request_data.encode("utf-8")
        request_data = json.loads(request_data)
    except Exception as e:
        logging.error(city + ' ' + api_purpose + ' 请求的数据有误，请检查[Request Data]字段是否是标准的json格式字符串！')
        return 400, ' 请求的数据有误，请检查[Request Data]字段是否是标准的json格式字符串！'
    #使用指定账号进行测试
    headers = {}

    idlist= ["uid","userId","userID","userid"]
    for uid in idlist:
        if uid in request_data:
            uid = request_data[uid]
            if isinstance(uid, int):
                uid = str(uid)
            if uid not in uid_token_map:
                logging.error(city + ' ' + api_purpose + ' 查无此uid,请去test_account表中录入测试账号信息!')
                return 400, ' 查无此uid,请补充测试数据'
            else:
                headers["token"] = uid_token_map[uid]

    #匹配拼接不同项目的url地址
    request_url = "https://" + api_host + request_url
    r = requests.post(request_url, request_data, headers=headers)

    status = r.status_code
    resp = r.text

    if  status == 200:
        if re.search(check_point,resp):
            logging.info(city+" "+api_purpose + "成功"+str(status) +", "+resp)
            return status,resp
        else:
            logging.error(city+" "+api_purpose+" 失败！！！,["+str(status)+"],"+resp)
            return 2001, resp
    else:
        logging.error(city+" "+api_purpose+"失败！！！,["+str(status)+"],"+resp)
        return status, resp



if __name__ =='__main__':
    from build_case import get_testcase_handle
    from settings import handleCaseFile

    handle_testcase=get_testcase_handle(handleCaseFile)
    print('开始执行测试用例')
    res = runTest(handle_testcase)
    print('结束测试')
    print(len(res))








