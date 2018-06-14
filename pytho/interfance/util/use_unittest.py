#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import mock
from test_interfance_1 import RunMain
import HTMLTestRunner

class TestMethod(unittest.TestCase):

    #def setUp(self):
        #self.run=RunMain(url,method)

    def test_01(self):
        url='https://t.yh.120yibao.com/yb/im/getImMsgTemplateInfo.do'
        data={
            't':'1524193658241',
            'Yb-Yh-Client':'0',
            'Yb-Yh-Token':'109bdefcfc10b1470cff15b394564b1d',
            'key':'chat_room'
        }
        mock_data = mock.Mock(return_value=data)
        print mock_data
        run = RunMain(url,'GET',data)
        res = run.run_main(url,'GET',data)

        #self.assertEqual(res['errorcode'], 1000, 'pass')
        print res
        #print('this is the first testMethod')

    def test_02(self):
        url = 'https://t.yh.120yibao.com/yb/im/resetUnreadMsgCount.do'
        data = {
            't':'1524109346742',
            'Yb-Yh-Client':'0',
          'Yb-Yh-Token':'109bdefcfc10b1470cff15b394564b1d',
            'conversationId':'6199'
        }
        run = RunMain(url,'POST', data)
        res = run.run_main(url,'POST', data)
        #self.assertEqual(res['errorcode'],1001,'pass')
        print res
        #print('this is the second testMethod')

if __name__=='__main__':
    #unittest.main()
    filepath='../report/htmlreport.html'
    fp = file(filepath,'wb')
    suite=unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is the first report')
    runner.run()
    #unittest.TextTestRunner().run(suite)


