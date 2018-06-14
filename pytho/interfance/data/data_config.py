#!/user/bin/env python
#_*_ coding:utf-8 _*_
class global_val:
    #case_id
    id ='0'
    request_name='1'
    url = '2'
    request_way='3'
    header='4'
    case_depend='5'
    data_depend='6'
    filed_depend='7'
    request_data='8'
    expect='9'
    result='10'
    run='11'
#获取case_id
def get_id():
    return global_val.id
#获取url
def get_url():
    return global_val.url
#获取是否运行
def get_run():
    return global_val.run
#获取运行方式
def get_run_way():
    return global_val.request_way
#获取header
def get_header():
    return global_val.header
#获取依赖id
def get_case_depend():
    return global_val.case_depend
#获取数据依赖
def get_data_depend():
    return global_val.data_depend
#获取filed_depend
def get_filed_depend():
    return global_val.filed_depend
#获取请求数据request_data
def get_request_data():
    return global_val.request_data
#获取预期结果expect
def get_expect():
    return global_val.expect
#获取实际结果
def get_result():
    return global_val.result
def get_header_value():
    header={
        "header":"1234",
        "cookie":"Mushishi"
    }
