#!/user/bin/env python
#_*_ coding:utf-8 _*_
from data.get_data import GetData
from util.runmethod import RunMethod
from util.commonutil import CommonUtil
from util.dependdent_data import DependdentData
from util.send_mail import SendEmail

class RunTest:
    def __init__(self):
        self.run_method=RunMethod()
        self.data=GetData()
        self.com_util=CommonUtil()
        self.send_mail = SendEmail()
    #程序执行
    def go_on_run(self):
        res = None
        pass_count = []
        error_count = []
        rows_count=self.data.get_case_lines()
        #print rows_count
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            # print is_run
            if is_run:
                url=self.data.get_url(i)
                #print url
                method = self.data.get_request_method(i)
                #print method
                request_data=self.data.get_data_for_json(i)
                #print data
                expect = self.data.get_expect_data(i)
                print expect
                header=self.data.is_header(i)
                #print header
                depend_case = self.data.is_depend(i)
                #print depend_case_id
                res = self.run_method.run_main(method,url,request_data,header)
                #print res
                if depend_case != None:
                    self.depend_data = DependdentData(depend_case)
                    #获取依赖的响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_response_data

                if self.com_util.is_contain(expect,res):
                    self.data.write_data(i,"PASS")
                    pass_count.append(i)
                    #print "PASS"
                else:
                    print self.data.write_data(i,res)
                    error_count.append(i)
        print len(pass_count)
        print len(error_count)
        self.send_mail.send_main(pass_count,error_count)

if __name__=='__main__':
    run = RunTest()
    res = run.go_on_run()
    #print res