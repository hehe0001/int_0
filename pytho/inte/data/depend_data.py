#!/user/bin/env python
#_*_ coding:utf-8 _*_
import xlrd
from base.oper_excel import OperationExcel
from data.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
import json
class DependdentData:
    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()
    #通过case_id获取整行的数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data
    #执行依赖测试，获取结果
    def run_dependdent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_way(row_num)
        url = self.data.get_request_url(row_num)
        res = run_method.run_main(method,url,request_data,header)
        return json.loads(res)
    #根据依赖的key去获取依赖测试的case的响应，然后返回
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependdent()
        json_exe = parse(depend_data)
        madel = json_exe.find(response_data)
        return [math.value for math in madel][0]#增强的for循环
if __name__ == '__main__':
    getConversationInfo = {"status":0,"info":"请求成功","data":{"conversationId":6194},"timeStamp":1528427365458}
    res = 'data.conversationId'
    json_exe = parse(res)
    madel = json_exe.find(getConversationInfo)
    print [math.value for math in madel][0]

    getOnLineCommodityDetail = {"status":0,"info":"请求成功",
                                "data":"{\"orderType\":10,\"priceId\":4090,"
                                       "\"doctor\":{\"name\":\"呵呵测试\","
                                       "\"imgPath\":\"https://ognvoq0qy.qnssl.com/doctor-man.png-mini\","
                                       "\"itemName\":\"营养科\",\"titleName\":\"主治医师\",\"hospitalName\":\"浙江大学附属第一医院\","
                                       "\"userId\":141273},"
                                       "\"hasPriceFavorable\":0,\"processDefinitionId\":11610,"
                                       "\"prevPage\":\"consult_my\",\"commodityId\":11282}","timeStamp":1528707588710}
    dat = json.loads(getOnLineCommodityDetail['data'])
    type(getOnLineCommodityDetail)
    res = 'data.processDefinitionId'
    json_exe = parse(res)
    madel1 = json_exe.find(dat)
    print [math.value for math in madel1][0]







