from build_case import get_simple_cases,get_city_cases,get_diff_cases
from tool import db_case_to_excel,swagger_case_to_excle,city_case_to_excel,diff_case_to_excle,case_to_db
from settings import swaggerCaseFile,city_CaseFile,dbCaseFile,diffCaseFile,handleCaseFile


if __name__ == '__main__':
    #step1
    # 获取swagger数据清理整合
    simple_case=get_simple_cases()
    print('simple_case',len(simple_case))
    #
    # # 导出swagger_case至excel
    #
    swagger_case_to_excle(simple_case,swaggerCaseFile)
    #
    # #step2
    # # swagger按city进行参数化，生成对应城市的case url,api_purpose,city
    #
    all_cases=get_city_cases(swaggerCaseFile)
    print('all_cases',len(all_cases))
    #
    # # 导出swagger_case至excel
    city_case_to_excel(all_cases,city_CaseFile)
    #
    # #step3
    # # 导出testcase现在所有的测试用例
    db_case_to_excel(dbCaseFile)
    #
    # # step4
    # #求出db_case和all_swagger_Case的差集（swagger_case有，而db_case中没有的case）
    diff_cases=get_diff_cases(dbCaseFile,city_CaseFile)
    print('diff_cases',len(diff_cases))
    #
    # #step5 # 导出diff_cases
    diff_case_to_excle(diff_cases,diffCaseFile)


    #step6 运行handle_case确认测试结果 run_testcase.py

    # step7 将step6运行没问题的case导入testcase库
    # case_to_db(handleCaseFile)

