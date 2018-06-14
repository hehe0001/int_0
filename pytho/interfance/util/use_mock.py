#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
from util.test_interfance_1 import RunMain
import json
from util.mokc_demo import mock_test
class TestMethod(unittest.TestCase):
    def test_01(self):
        url='https://t.yh.120yibao.com/yb/customerInfo/getCustomerInfoByUserId.do'
        data1={
            't':'1524636011063',
            'Yb-Yh-Client':'0',
            'Yb-Yh-Token':'15c0ac61334823268d71fcf162b0f35d',
            }
        data2={"body":
                   {"FSex":0,
                    "importantInfor":
                        {"msgNum":2,
                         "recordCompletNum":66,
                         "todoNum":27},
                    "FPhone":"15235668144",
                    "FCustomerId":33049,
                    "FEmail":"",
                    "FImgPath":"https://odqxe8nnu.qnssl.com/customerHeadImg/20180403160959A8OYPr",
                    "isMutualMember":0,
                    "FCityId":0,
                    "isMember":0,
                    "FNickName":"",
                    "FBirthday":57600000,
                    "FName":"N",
                    "FProvinceId":0,
                    "FIdCard":"",
                    "FProvinceName":"全国"},
               "info":"获得用户个人资料成功",
               "status":100
               }
        run = RunMain(url, 'GET', data1)
        res=mock_test(run.run_main(url, 'GET', data1),data1,data2,url,'GET')
        # mock_data = mock.Mock(return_value=data)
        # print mock_data
        # print mock_data()
        #run.run_main=mock_data
        #res = run.run_main(url,'GET',data)
        print res
        rre=json.dumps(res)
        print rre
        #re=json.loads(res)
        #print re
        #rint re.get('status')
        #self.assertEqual(re.get('status'),0,'测试通过')
        print('this is the first testMethod')


if __name__=='__main__':
    #unittest.main()
    # filepath='../report/htmlreport.html'
    # fp = file(filepath,'wb')
    suite=unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    #runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is the first report')
    #runner.run()
    #unittest.TextTestRunner().run(suite)
