#!/user/bin/env python
#_*_ coding:utf-8 _*_
class global_val:
    #case_id
    case_ID = '0'
    #名称
    case_name = '1'
    #是否执行
    is_run = '2'
    #url
    url = '3'
    #请求方式
    request_method = '4'
    #header
    header = '5'
    #依赖ID
    depend_case_ID = '6'
    #依赖数据
    depend_data = '7'
    #依赖数据所属字段
    depend_field = '8'
    #请求数据
    request_data = '9'
    #预期结果
    expect_data = '10'
    #实际结果
    result_data = '11'

#获取case_id
def get_id():
    return global_val.case_ID
#获取是否运行
def get_run():
    return global_val.is_run
#获取url
def get_url():
    return global_val.url
#获取请求方式
def get_request_method():
    return global_val.request_method
#获取header
def get_header_value():
    # header = {
    #     "header":"1234",
    #     "cookie":"11111"
    # }
    return global_val.header
#获取依赖ID
def get_depend_id():
    return global_val.depend_case_ID
#获取依赖数据
def get_depend_data():
    return global_val.depend_data
#获取依赖数据所属字段
def get_depend_data_field():
    return global_val.depend_field
#获取请求数据
def get_request_data():
    return global_val.request_data
#获取预期结果
def get_expect_data():
    return global_val.expect_data
#获取实际结果
def get_result_data():
    return global_val.result_data

