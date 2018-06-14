#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
from run_main.run_main import Run_main
import mock
from mock_demo import mock_test
class TestMethod(unittest.TestCase):
    def setUp(self):
        pass
        #self.Run = Run_main()
    def test_2(self):
        urll = 'https://t.yh.120yibao.com/yb/serviceGroup/getConcernDoctorList.do'
        data = {
            "t": "1527128460976",
            "Yb-Yh-Client": "0",
            "Yb-Yh-Token": "379772e16a86c93ce238f642b2e72bf6",
            "start": "0",
            "size": "10"
        }
        run = Run_main(urll, 'GET', data)
        res = mock_test(run.run_main,data,urll,'GET',data)
        # run.run_main = mock.Mock(return_value=data)
        # res = run.run_main(urll, 'GET', data)
        print res
if __name__=='__main__':
    unittest.main()
