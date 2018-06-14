#!/user/bin/env python
#_*_ coding:utf-8 _*_
from util.operation_excel import OperationExcel
from util.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import parser

class DependdentData:
    def __init__(self,case_id):
        self.opera_excel = OperationExcel()
        self.case_id = case_id
        self.data = GetData()
    '''
    通过case_id去获取case_di的整行数据
    '''
    def get_case_line_data(self,case_id):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data
    #执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_url(row_num)

        res = run_method.run_main(method,url,request_data,header)
        return res

    #根据依赖的key去获取执行依赖测试case的响应数据，然后返回
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        print depend_data
        print response_data
        json_exe = parser(depend_data)
        madel = json_exe.find(response_data)
        return [math.value for math in madel][0]






