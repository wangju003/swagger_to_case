import requests
import pandas as pd

#根据swagger文档，获取所有接口，并利用文档中的数据生成简单case
def get_simple_cases():
    '''

    :param update_swagger_url:
    :param swagger_url:
    :return: simple_case集合 [[],[]]  可以用pd.to_excel()写入excel表的数据格式
    '''
    from settings import update_swagger_url, swagger_url
    # 刷新接口文档
    r = requests.get(update_swagger_url)  # 响应时间3S

    swagger_datas = requests.get(swagger_url).json()['paths']

    simple_case = []

    for api_data in swagger_datas:

        # 请求方式 post or get
        if 'post' in swagger_datas[api_data]:
            request_method = 'post'
        else:
            request_method = 'get'

        # 接口描述信息
        api_purpose = swagger_datas[api_data][request_method]['summary'].replace(' ', '')
        if api_purpose is '':
            api_purpose = swagger_datas[api_data][request_method]['description'].replace(' ', '')

        # 判断请求参数是否包含{city}
        try:
            parameters = swagger_datas[api_data][request_method]['parameters']
        except:
           #数据结构中 No parameters
            parameters=''
        parameters =str(parameters)
        if 'cityId' in parameters or 'cityid' in parameters or 'city_id' in parameters or 'city' in parameters:
            data_city_flag = True
        else:
            data_city_flag = False

        #判断url是否包含{city}
        if 'cityId' in api_data or 'cityid' in api_data or 'city_id' in api_data or 'city' in api_data:
            url_city_flag=True
        else:
            url_city_flag=False


        simple_case.append([api_data,api_purpose,data_city_flag,url_city_flag])

    return simple_case

def get_city_cases(swagger_caseFild):
    '''
    将swagger_case中的url进行参数化，规则：url或data中包含city字样，即参数化url
    :return: all_cases 可以通过pd.to_excel写入excle的格式 [[],[]]
    '''
    from settings import citys
    df = pd.read_excel(swagger_caseFild)
    all_cases = []

    #读取swaggercase,遇到cityid生成参数化后的case,再按照[[],[]]的格式重新组装好
    for case in df.values:
        request_url = case[1]
        api_purpose = case[2]
        data_city_flag = case[3]
        url_city_flag = case[4]

        if url_city_flag :
            # 只要url中包含{city}就参数化
            for city in citys:
                city_name = city['name']
                city_id=city['city_id']
                if '{cityId}' in request_url :
                    request_url_new = request_url.replace('{cityId}',city_id )
                elif '{cityid}' in request_url:
                    request_url_new = request_url.replace('{cityid}',city_id )
                elif '{city_id}' in request_url:
                    request_url_new = request_url.replace('{city_id}',city_id )
                elif '{city}' in request_url:
                    request_url_new = request_url.replace('{city}',city_id )

                all_cases.append([request_url_new, api_purpose, city_name])
        elif data_city_flag and (not url_city_flag):
                # 如果url中不包含{city},再确认data中是否包含{city},生成多条url,city列填充城市
            for city in citys:
                city_name = city['name']
                all_cases.append([request_url, api_purpose, city_name])
        elif (not data_city_flag) and (not url_city_flag):
            # url和data中都不包含{city},使用默认数据
            city_name = None

            all_cases.append([request_url, api_purpose, city_name])
            
    return all_cases

def get_diff_cases(dbCaseFile,city_CaseFile):
    #求出 db_case和all_swagger_Case的差集（swagger_case有，而db_case中没有的case），
    df1 = pd.read_excel(dbCaseFile)
    df1.replace(r'/appapi','',regex=True,inplace=True)
    df2 = pd.read_excel(city_CaseFile)

    diff_cases = []
    # 数据库中所有的url列表
    db_urls = []
    for case in df1.values:
        db_urls.append(case[4])
    # 遍历自动生成的case-url，如果这个url在case库中没有，那么就记录下来，需要进行人工补充测试数据
    for case in df2.values:
        request_url = case[1]
        api_purpose = case[2]
        city = case[3]
        if request_url not in db_urls:
            diff_cases.append([request_url, api_purpose, city])

    return diff_cases

def get_testcase_handle(handleCaseFile):
    '''

    :return: handle_tsetcase列表集合 [[],[]]
    '''

    df = pd.read_excel(handleCaseFile)
    #使用空格 填充 city 和 correlation的non值
    df['city']=df.fillna(value=' ')
    # df['correlation'] = df.fillna(value='abc')
    #active列置为Yes
    df['active']='Yes'
    testcase = df.values
    return testcase


if __name__ == '__main__':
    from settings import dbCaseFile,city_CaseFile,handleCaseFile
    #
    # handleCase=get_testcase_handle(handleCaseFile)
    # print(handleCase[1:2])

    diff_cases = get_diff_cases(dbCaseFile, city_CaseFile)
    print('diff_cases', len(diff_cases))