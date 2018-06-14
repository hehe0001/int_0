#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
from run_main.run_main import Run_main
import HTMLTestRunner
class TestMethod(unittest.TestCase):
    def setUp(self):
        self.userid = self.test_1()
    def test_1(self):
        url = 'https://t.yh.120yibao.com/yb/im/resetUnreadMsgCount.do'
        data = {
            "t": "1527134081498",
            "Yb-Yh-Client": "0",
            "Yb-Yh-Token": "379772e16a86c93ce238f642b2e72bf6",
            "conversationId": "6194"
        }
        self.userid = 10002
        globals()['id'] = 10014
        return self.userid
        run = Run_main(url,'POST',data)
        res = run.run_main(url,'POST',data)
        #print res.text
        print res.status_code
        self.assertEqual(res.status_code,20,'error')
    #@unittest.skip('test_2')
    def test_2(self):
        urll = 'https://t.yh.120yibao.com/yb/serviceGroup/getConcernDoctorList.do'
        data = {
            "t": "1527128460976",
            "Yb-Yh-Client": "0",
            "Yb-Yh-Token": "379772e16a86c93ce238f642b2e72bf6",
            "start": "0",
            "size": "10"
        }
        run = Run_main(urll,'GET',data)
        res = run.run_main(urll,'GET',data)
        print self.userid
        print id
        #print res.text
        #print res.status_code
        if res.status_code == 200:
            print 'pass'
        else:
            print 'error'
if __name__=='__main__':
    #unittest.main()
    suite1 = unittest.TestSuite()
    suite1.addTest(TestMethod('test_1'))
    suite1.addTest(TestMethod('test_2'))
    #unittest.TextTestRunner().run(suite)
    filepath = '../report/HTMLreport.html'
    fp = file(filepath,'wb')
    Runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title = 'this is a report')
    Runner.run(suite1)
