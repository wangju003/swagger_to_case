import  os

dirname,filename=os.path.split(os.path.abspath(__file__))
case_path=os.path.join(dirname,'case_excel')

swaggerCaseFile='swagger_cases.xlsx'
swaggerCaseFile = os.path.join(case_path,swaggerCaseFile)

city_CaseFile='build_city_case.xlsx'
city_CaseFile=os.path.join(case_path,city_CaseFile)

dbCaseFile='db_testcase.xlsx'
dbCaseFile=os.path.join(case_path,dbCaseFile)

diffCaseFile='diff_case.xlsx'
diffCaseFile=os.path.join(case_path,diffCaseFile)

handleCaseFile = 'db_testcase_from_cxt.xlsx'
handleCaseFile = os.path.join(case_path,handleCaseFile)


update_swagger_url = 'https://appapi-test.5i5j.com/swagger.php'
swagger_url='https://appapi-test.5i5j.com/swagger.json'


config = {
    "host": "10.2.1.92",  # 地址
    "port": 3306,  # 端口
    "user": "root",  # 用户名
    "password": "admin123456",  # 密码
    "database": "autotest",  # 数据库名;如果通过Python操作MySQL,要指定需要操作的数据库
    "charset": "utf8"
}

citys = [
    {"name": "北京", "city_id": "1"},
    {"name": "杭州", "city_id": "2"},
    {"name": "苏州", "city_id": "5"},
    {"name": "太原", "city_id": "6"},
    {"name": "成都", "city_id": "15"},
    {"name": "郑州", "city_id": "18"},
    {"name": "上海", "city_id": "9"},
    {"name": "武汉", "city_id": "20"},
    {"name": "天津", "city_id": "7"},
    {"name": "南京", "city_id": "8"},
    {"name": "无锡", "city_id": "19"},
    {"name": "南宁", "city_id": "16"},
    {"name": "南昌", "city_id": "24"},
    {"name": "长沙", "city_id": "22"},
    {"name": "青岛", "city_id": "21"},
    {"name": "常州", "city_id": "25"},
    {"name": "东莞", "city_id": "66"},
]

uid_token_map = {
    '7807408': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjEifQ.eyJpc3MiOiJ6aGFuZ3NhbiIsImp0aSI6IjEiLCJpYXQiOjE1Nzc3NjE4OTksImF1ZCI6IntcInVpZFwiOlwiNzgwNzQwOFwiLFwibG9naW5uYW1lXCI6bnVsbCxcIm5pY2tuYW1lXCI6XCJcXHU1MzY3XFx1NjlmZFwiLFwiZW1haWxcIjpudWxsLFwiZ2VuZGVyXCI6bnVsbCxcInJlZ2lvblwiOm51bGwsXCJjaXR5XCI6bnVsbCxcImhlYWRpbWdcIjpudWxsLFwiaW52aXRpbmdjb2RlXCI6bnVsbCxcInJlZ2RhdGVcIjpcIjE1NjQ5Njg1MzRcIixcInN0YXR1c1wiOjEsXCJwYXNzV29yZFwiOlwiZDE1MTVhNmRmMzc4NTg2ZTAxOTc3ZWFjYjQ5ODk5MzRcIixcInNhbHRcIjpcIjk4ZDIyMVwifSIsInN1YiI6InN1YmplY3QifQ.FScflgI-feX-p6xepEgj_fl63G_naGeONffrj_wO2JY',
    '7782413': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjEifQ.eyJpc3MiOiJ6aGFuZ3NhbiIsImp0aSI6IjEiLCJpYXQiOjE1Nzc0MTY2OTAsImF1ZCI6IntcInVpZFwiOlwiNzc4MjQxM1wiLFwibG9naW5uYW1lXCI6bnVsbCxcIm5pY2tuYW1lXCI6XCJcXHU1NjFmXFx1NTYxZmJ1ZHVcIixcImVtYWlsXCI6bnVsbCxcImdlbmRlclwiOm51bGwsXCJyZWdpb25cIjpudWxsLFwiY2l0eVwiOm51bGwsXCJoZWFkaW1nXCI6bnVsbCxcImludml0aW5nY29kZVwiOm51bGwsXCJyZWdkYXRlXCI6XCIxNTY0NzIzNzkyXCIsXCJzdGF0dXNcIjoxLFwicGFzc1dvcmRcIjpcImM1NmI4ZGFlNzcwZjdlNGVhMGIwNjg5MGUxNzdiODI0XCIsXCJzYWx0XCI6XCJhR0djN21cIn0iLCJzdWIiOiJzdWJqZWN0In0.5SqN2FEXnohFJi9hmwAFUX3lA-NDIOQPtCH77fX4bdM',
    '6312286': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjEifQ.eyJpc3MiOiJ6aGFuZ3NhbiIsImp0aSI6IjEiLCJpYXQiOjE1NzY4MTA4NDksImF1ZCI6IntcInVpZFwiOlwiNjMxMjI4NlwiLFwibG9naW5uYW1lXCI6bnVsbCxcIm5pY2tuYW1lXCI6XCJcXHU3NTFmXFx1NGVhN1wiLFwiZW1haWxcIjpudWxsLFwiZ2VuZGVyXCI6bnVsbCxcInJlZ2lvblwiOm51bGwsXCJjaXR5XCI6bnVsbCxcImhlYWRpbWdcIjpudWxsLFwiaW52aXRpbmdjb2RlXCI6bnVsbCxcInJlZ2RhdGVcIjpcIjE1NTM0OTY2MzJcIixcInN0YXR1c1wiOjEsXCJwYXNzV29yZFwiOlwiNzIxOTk2YTQxMjU0MjY0NTE1OTRkNDI0NTc5MjMzMjhcIixcInNhbHRcIjpcIjNVMWVjNFwifSIsInN1YiI6InN1YmplY3QifQ.KZFAOXnRKnkxCd9Q9cdvfy2jF1HvIoD_rx00Z2L0RZE',
    '6546639': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdWJqZWN0IiwiYXVkIjoie1widWlkXCI6NjU0NjYzOSxcIm5pY2tuYW1lXCI6bnVsbCxcInJlZ2RhdGVcIjpudWxsLFwiZ2VuZGVyXCI6bnVsbCxcImVtYWlsXCI6bnVsbCxcImhlYWRpbWdcIjpudWxsLFwiY2l0eVwiOm51bGwsXCJyZWdpb25cIjpudWxsLFwiaW52aXRpbmdjb2RlXCI6bnVsbCxcImxvZ2lubmFtZVwiOlwiMTg2MTE4MDQ1NDdcIixcInRva2VuXCI6bnVsbCxcInBhc3NXb3JkXCI6bnVsbH0iLCJpc3MiOiJ6aGFuZ3NhbiIsImlhdCI6MTU1ODMzNDIzNDE2NywianRpIjoiMSJ9.9p4OdpPsPou-fjLszbB9UV796u3efIiQtxDj808hmX4',
    '6226103': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdWJqZWN0IiwiYXVkIjoie1widWlkXCI6NjU0NjYzOSxcIm5pY2tuYW1lXCI6bnVsbCxcInJlZ2RhdGVcIjpudWxsLFwiZ2VuZGVyXCI6bnVsbCxcImVtYWlsXCI6bnVsbCxcImhlYWRpbWdcIjpudWxsLFwiY2l0eVwiOm51bGwsXCJyZWdpb25cIjpudWxsLFwiaW52aXRpbmdjb2RlXCI6bnVsbCxcImxvZ2lubmFtZVwiOlwiMTg2MTE4MDQ1NDdcIixcInRva2VuXCI6bnVsbCxcInBhc3NXb3JkXCI6bnVsbH0iLCJpc3MiOiJ6aGFuZ3NhbiIsImlhdCI6MTU1ODMzNDIzNDE2NywianRpIjoiMSJ9.9p4OdpPsPou-fjLszbB9UV796u3efIiQtxDj808hmX4',
    '6741913': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjEifQ.eyJpc3MiOiJ6aGFuZ3NhbiIsImp0aSI6IjEiLCJpYXQiOjE1Nzc5NTU4NjMsImF1ZCI6IntcInVpZFwiOlwiNjc0MTkxM1wiLFwibG9naW5uYW1lXCI6bnVsbCxcIm5pY2tuYW1lXCI6XCJcXHU5ZWQ4XFx1OWVkOFxcdTY1ZTBcXHU5NWZiNjY4OFwiLFwiZW1haWxcIjpudWxsLFwiZ2VuZGVyXCI6bnVsbCxcInJlZ2lvblwiOm51bGwsXCJjaXR5XCI6bnVsbCxcImhlYWRpbWdcIjpudWxsLFwiaW52aXRpbmdjb2RlXCI6bnVsbCxcInJlZ2RhdGVcIjpcIjE1NTY0MzY0MjdcIixcInN0YXR1c1wiOjEsXCJwYXNzV29yZFwiOlwiY2Y5MjdmY2FlODg1OTE4MjA3MmZmN2EyNjE5YzU4YzVcIixcInNhbHRcIjpcIkVkQXdMdlwifSIsInN1YiI6InN1YmplY3QifQ.xlZ6yYZu7h6AkIDq8TizUUJywzhAqaTFvn9Dkkb4Y-k',
    '7621408': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIiwianRpIjoiMSJ9.eyJpc3MiOiJ6aGFuZ3NhbiIsImp0aSI6IjEiLCJpYXQiOjE1NjYyOTA2MzMsImF1ZCI6IntcInVpZFwiOjc2MjE0MDgsXCJsb2dpbm5hbWVcIjpcIjEzOTEwNzc1NTc0XCIsXCJuaWNrbmFtZVwiOlwiMTM5MTA3NzU1NzRcIixcImVtYWlsXCI6bnVsbCxcImdlbmRlclwiOm51bGwsXCJyZWdpb25cIjpudWxsLFwiY2l0eVwiOm51bGwsXCJoZWFkaW1nXCI6XCJcIixcImludml0aW5nY29kZVwiOlwiMDAxNTA4NDM3XCIsXCJyZWdkYXRlXCI6XCIyMDE5LTA3LTE4IDE2OjQwOjE4XCIsXCJzdGF0dXNcIjoxLFwicGFzc1dvcmRcIjpcIjkzMmFiODgxMTRiMWQyMDE1OWJhNWYzNTg4YmZlYWMyXCJ9Iiwic3ViIjoic3ViamVjdCJ9.',
    '923544': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjEifQ.eyJpc3MiOiJ6aGFuZ3NhbiIsImp0aSI6IjEiLCJpYXQiOjE1NzA2NzE3MjQsImF1ZCI6IntcInVpZFwiOjkyMzU0NCxcImxvZ2lubmFtZVwiOlwiMTMzMTAyMTIyNjBcIixcIm5pY2tuYW1lXCI6XCJcXHU5NjQ4XFx1NTJjN1NDXCIsXCJlbWFpbFwiOlwiXCIsXCJnZW5kZXJcIjpudWxsLFwicmVnaW9uXCI6XCJcIixcImNpdHlcIjpudWxsLFwiaGVhZGltZ1wiOlwiaHR0cHM6XFxcL1xcXC9yZXMuNWk1ai5jb21cXFwvdXBsb2Fkc1xcXC9pbWFnZXNcXFwvMjAxOVxcXC8wNTI1XFxcLzE2XFxcLzE1NTg3NzM1NTQxMTg0ODYuanBnXCIsXCJpbnZpdGluZ2NvZGVcIjpudWxsLFwicmVnZGF0ZVwiOlwiMjAxOS0wOS0xOCAxNTo0NToyN1wiLFwic3RhdHVzXCI6MSxcInBhc3NXb3JkXCI6XCJiODY1M2M0YTJkNzVmZmQwNzllNGY1NGViYjVmNDYyZVwiLFwic2FsdFwiOlwiQjlTQVlDXCJ9Iiwic3ViIjoic3ViamVjdCJ9.aYdyL2VkjtplG2qY9MKMZ-upMfoNqrLMav0ZScz_yqc'
}





