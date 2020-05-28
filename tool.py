import pandas as pd


def db_case_to_excel(dbCaseFile):
    '''
    导出测试用例至excel文件
    :return: None
    '''

    from sqlalchemy import create_engine
    engine = create_engine('mysql+mysqlconnector://root:admin123456@10.2.1.92/autotest?charset=utf8')

    sql = 'select  * from testcase'
    df = pd.read_sql_query(sql, engine)
    df.to_excel(dbCaseFile)

def swagger_case_to_excle(simple_cases,swaggerCaseFile):
    '''
    将swagger文档数据按照固定的格式导出至excle
    :return: None
    '''

    df = pd.DataFrame(simple_cases, columns=['api_data', 'api_purpose', 'data_city_flag', 'url_city_flag'])
    df.to_excel(swaggerCaseFile)

def diff_case_to_excle(diff_cases,diffCaseFile):
    '''
    导出swagger自动生成，但数据库中没有的case--需要人工维护的用例
    :param db_caseFile: 导出的case excel文件
    :param city_caseFile:已经进行city参数化之后的swagger case excel文件
    :return:None
    '''

    res=pd.DataFrame(diff_cases,columns=['request_url','api_purpose','city'])
    res.to_excel(diffCaseFile)

def city_case_to_excel(all_cases,city_CaseFile):
    '''
    导出已经参数化后的swagger_case至excel
    :return: None
    '''

    df1=pd.DataFrame(all_cases,columns=['request_url','api_purpose','city'])
    df1.to_excel(city_CaseFile)

def case_to_db(handleCaseFile):
    # 测试好的case追加进testcase表
    from sqlalchemy import create_engine
    engine = create_engine('mysql+mysqlconnector://root:admin123456@10.2.1.92/autotest?charset=utf8')

    df = pd.read_excel(handleCaseFile)
    df.to_sql('testcase', engine, index=False, if_exists='append')


if __name__ =='__main__':
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqlconnector://root:admin123456@10.2.1.92/autotest?charset=utf8')
    from settings import dbCaseFile
    df = pd.to_sql('testcase',engine)
    df.to_sql('testcase', engine, index=False, if_exists='append')