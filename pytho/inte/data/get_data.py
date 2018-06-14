#!/user/bin/env python
#_*_ coding:utf-8 _*_
from base.oper_excel import OperationExcel
from base.operation_json import OperationJson
import data_config
class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()
    #去获取excel行数，即case数
    def get_case_lines(self):
        return self.opera_excel.get_lines()
    def get_is_run(self,row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cel_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag
    #是否有header
    def is_header(self,row):
        col = int(data_config.get_header_value())
        header = self.opera_excel.get_cel_value(row,col)
        if header == 'yes':
            return data_config.get_header_value()
        else:
            return None
    #获取请求方式
    def get_request_way(self,row):
        col = int(data_config.get_request_method())
        request_way = self.opera_excel.get_cel_value(row,col)
        return request_way
    #获取url
    def get_request_url(self,row):
        col = int(data_config.get_url())
        request_url = self.opera_excel.get_cel_value(row,col)
        return request_url
    #获取请求数据
    def get_request_data(self,row):
        col = int(data_config.get_request_data())
        data = self.opera_excel.get_cel_value(row,col)
        if data == '':
            return None
        else:
            return data
    #通过获取关键字拿到data数据
    def get_data_for_json(self,row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data
    #获取预期结果
    def get_expect_data(self,row):
        col = int(data_config.get_expect_data())
        expect_data = self.opera_excel.get_cel_value(row,col)
        if expect_data == '':
            return None
        else:
            return expect_data
    #写入数据
    def write_result(self,row,value):
        col = int(data_config.get_result_data())
        self.opera_excel.wirte_value(row,col,value)

    #获取依赖数据的key
    def get_depend_key(self,row):
        col = int(data_config.get_depend_data())
        depend_key = self.opera_excel.get_cel_value(row,col)
        if depend_key == '':
            return None
        else:
            return depend_key
    #判断是否有case依赖
    def is_depend(self,row):
        col = int(data_config.get_depend_id())
        depend_case_id = self.opera_excel.get_cel_value(row,col)
        if depend_case_id == '':
            return None
        else:
            return depend_case_id
    #获取数据依赖字段
    def get_depend_field(self,row):
        col = int(data_config.get_depend_data_field())
        data = self.opera_excel.get_cel_value(row,col)
        if data == '':
            return None
        else:
            return data


