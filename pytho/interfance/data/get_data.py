#!/user/bin/env python
#_*_ coding:utf-8 _*_
from util.operation_excel import OperationExcel
from data import data_config
from util.operation_json_class import OperationJson
class GetData:
    def __init__(self):
        self.opera_excel=OperationExcel()
    #获取excel行数，即case数
    def get_case_lines(self):
        return self.opera_excel.get_lines()
    #获取是否执行
    def get_is_run(self,row):
        flag=None
        col=int(data_config.get_run())
        run_model=self.opera_excel.get_cell_value(row,col)
        if run_model=='yes':
            flag=True
        else:
            flag=False
        return flag
    #是否有header
    def is_header(self,row):
        col=int(data_config.get_header())
        header=self.opera_excel.get_cell_value(row,col)
        if header=='yes':
            return data_config.get_header_value()
        else:
            return None
    #获取请求方式
    def get_request_method(self,row):
        col=int(data_config.get_run_way())
        request_method=self.opera_excel.get_cell_value(row,col)
        return request_method
    #获取url
    def get_url(self,row):
        col=int(data_config.get_url())
        request_url=self.opera_excel.get_cell_value(row,col)
        return request_url
    #获取请求数据
    def get_reuquest_data(self,row):
        col =int(data_config.get_request_data())
        request_data=self.opera_excel.get_cell_value(row,col)
        if request_data == '':
            return None
        return request_data
    #获取关键字拿到data数据
    def get_data_for_json(self,row):
        opera_json=OperationJson()
        request_data=opera_json.get_data(self.get_reuquest_data(row))
        return request_data
    #获取预期结果
    def get_expect_data(self,row):
        col = int(data_config.get_expect())
        expect_data = self.opera_excel.get_cell_value(row,col)
        if expect_data == '':
            return None
        return expect_data
    #写入实际结果
    def write_data(self,row,value):
        col = int(data_config.get_result())
        self.opera_excel.write_value(row,col,value)

    #获取依赖数据的key
    def get_depend_key(self,row):
        col = int(data_config.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row,col)
        if depend_key == "":
            return None
        else:
            return depend_key

    #判断是否有case依赖
    def is_depend(self,row):
        col = int(data_config.get_filed_depend())
        depend_case_id = self.opera_excel.get_cell_value(row,col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    #获取数据依赖字段
    def get_depend_field(self,row):
        col = int(data_config.get_filed_depend())
        data = self.opera_excel.get_cell_value(row,col)
        if data == "":
            return None
        else:
            return data


if __name__=="__main__":
    get=GetData()
    line=get.get_case_lines()
    print line
    for i in range(1,line):
        print get.get_url(i)
        print get.get_reuquest_data(i)
        print get.get_is_run(i)
        print get.get_data_for_json(i)
        print get.get_request_method(i)
        print get.get_expect_data(i)


