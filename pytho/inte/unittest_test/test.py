#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
class Test(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
        self.assertEqual('fOo'.upper(), 'FOO')
        self.assertEqual('Foo'.upper(), 'FOO')
        self.assertEqual('foo'.upper(), 'FOO')

if __name__=="__main__":
    unittest.main()