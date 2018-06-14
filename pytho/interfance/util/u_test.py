#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest

class TestMethod(unittest.TestCase):
    @classmethod#注解
    def setUpClass(cls):
        print('类执行之前的方法\n')
    @classmethod
    def tearDownClass(cls):
        print('类执行之后的方法\n')
    def setUp(self):
        print('test---->setUp')

    def test_01(self):
        print('this is the first testMethod')

    def test_02(self):
        print('this is the second testMethod')

    def tearDown(self):
        print('test---->tearDown')

if __name__=='__main__':
    unittest.main()
