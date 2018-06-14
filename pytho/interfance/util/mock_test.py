# #!/user/bin/env python
# #_*_ coding:utf-8 _*_
# import unittest
# from mock import Mock
# mockObj=Mock(name='oom')
# print mockObj
# #print('********')
# return_v=Mock(return_value=100)
# print return_v
# print('********')
# mockObj=return_v()
# print mockObj
# print('********')
#
# class Foo(object):
#     _num=200
#     def fun1(self):
#        print('call fun1')
#     def fun2(self,argValue):
#         print'value=',argValue
# fooObj = Foo()
# print fooObj
# #print('****+++****')
# mockFoo=Mock(return_value=fooObj)
# print mockFoo
# print('****---****')
# print(fooObj._num)
# #print('****====****')
# print(fooObj.fun1())
# #print('****....****')
# print(fooObj.fun1())
# print('****////****')
# print(fooObj.fun2())
# #print('****````****')
# print(fooObj.fun2((20)))
#
# #side_effect设置之后，会覆盖return_value的值
# mockAoo1=Mock(return_value=1000,side_effect=StandardError)
# mockObj0=mockAoo1()
#
# # #指定的参数值是一个list或者tuple
# #  fooList=[10,20,30,40]
# #  mockFoo1=Mock(return_value=15,side_effect=fooList)
# #  mockObj1=mockFoo1()
# # # print('==============')
# #  print mockObj1
# #  mockObj1=mockFoo1()
# # # print('==============')
# #  print mockObj1
# #  mockObj1=mockFoo1()
# # # print('==============')
# #  print mockObj1
# #  mockObj1=mockFoo1()
# # # print('==============')
# #  print mockObj1
#
# # #spec参数
# # #指定的是属性组成的list
# specList=['_value','callFun1']
# mockFoo2=Mock(spec=specList)
# # print('||||||||||')
# print mockFoo2
# # print('\\\\\\\\')
# print mockFoo2._value
# # print('/////////')
# print mockFoo2.callFun1
# # #指定的是一个类属性
# class Boo(object):
#     _num=11
#     def fun1(self):
#         print 'call fun1'
#     def fun2(self,argValue):
#         print 'argValue = ',argValue
#
# mockFoo3=Mock(spec=Boo)
# # print('----------')
# print mockFoo3
# # print('==========')
#  print mockFoo3._num
# # print(',,,,,,,,,,,,')
#  print mockFoo3.fun1
# # print('[[[[[[[[[[[[')
#  print mockFoo3.fun2
#
# #assert断言:至少有一个参数有错误的值或者类型时，
# # 当参数的个数出现错误时，当参数顺序不正确时
# #这个断言会发生错误
#  class Woo(object):
#      _num=29
#      def fun1(self):
#          pass
#      def fun2(self,argValue):
#          pass
#  mockWoo=Mock(spec=Woo)
#  print mockWoo
#  print mockWoo.fun1
#  mockWoo.fun1()
#  mockWoo.fun1.assert_called_once_with()
#  #mockWoo.fun1.assert_called_with()
#  mockWoo.fun1.assert_called_once_with()
#
#  print('||||||||||||||||')
#  mockWoo.fun2('aaa')
#  mockWoo.fun2.assert_called_with('aaa')
#  mockWoo.fun2.assert_any_call('aaa')
#  mockWoo.fun2.assert_any_call('aba')
#
# #mock的管理方法:
# # attach_mock()将一个mock对象添加到另一个mock对象
#  class Qoo(object):
#      _value1=134
#      def fun3(self):
#          pass
#      def fun4(self,argValue):
#          pass
#  class Qoo2(object):
#      _value2=345
#      def fun5(self):
#          pass
#      def fun6(self,argValue):
#          pass
#
#  mockQoo1=Mock(spec=Qoo)#spec设置的事mock对象的属性
#  mockQoo2=Mock(spec=Qoo2)
#  print mockQoo1
#  print mockQoo2
# # #将mockQoo2添加到mockQoo1中，并命名为mock_att
# # mockQoo1.attach_mock(mockQoo2,'mock_att')
#  print mockQoo1
#  print mockQoo1
#  print mockQoo1.fun3()
#  print mockQoo1.mock_att
#  print mockQoo1.mock_att._value2
#  print mockQoo1.mock_att.fun5()
#  print mockQoo2.fun6()
# #configure_mock()：更改mock对象的return_value值
#  class Eoo(object):
#      _value=234
#      def fun1(self):
#          print 'call fun1'
#      def fun2(self,argValue):
#          print 'print fun2, argValue = ',argValue
#  mockEoo = Mock(spec=Eoo,return_value=14556)
#  print mockEoo()
#  mockEoo.configure_mock(return_value=778)
#  print mockEoo()
#  sooSpec={'fun1.return_value':'900','fun2.return_value':'800',
#           'fun2.side_effect':StandardError}
#  mockEoo.configure_mock(**sooSpec)
#  print mockEoo.fun1
#  print mockEoo.fun1()
#
# #mock_add_spec(aSpec,spec_set=Flase)：给mock对象添加一个新的属性，
# # mick对象原来的属性会被擦除，第二个参数是指属性是可读可写的，默认是支付
#  class Roo(object):
#      _value=123
#      def fun1(self):
#          pass
#      def fun2(self,argValue):
#          pass
#  def add_fun(self):
#      pass
#  class add_Roo(object):
#      _value1=134
#      def fun3(self):
#          pass
#      def fun4(self,argValue):
#          pass
#
#  mockRoo = Mock(spec=Roo)
#  print mockRoo._value
#  print mockRoo.fun1()
#  mockRoo.mock_add_spec(add_fun)
#  print mockRoo
# # #print mockRoo.add_fun()#报错原因：添加的属性要和mock对象原来的属性类型一致，
#                          # 是类都应该是类
#
#  mockRoo.mock_add_spec(add_Roo)
#  print mockRoo
#  print mockRoo.fun3()
# #mock统计
# #called：跟踪mock对象的任意调用的访问器
# def fun():
#     pass
# mockFoo=Mock(spec=fun)
# print mockFoo
# print mockFoo.called
# mockFoo()
# print mockFoo.called
#
# #call_count：mock对象被调用的次数
# print mockFoo.call_count
# mockFoo()
# print mockFoo.call_count
#
# #call_args:获取工厂调用时的参数（最近使用参数）
# print mockFoo.call_args
# #call_args_list：获取工厂调用的所有参数，是个list
# print mockFoo.call_args_list
# #method_calls：测试一个mock对象都调用了哪些方法，结果是一个list
# class Boo(object):
#     def func(self):
#         pass
# mockFoo = Mock(spec=Boo)
# mockFoo.func()
# print mockFoo.method_calls
#
# #mock_calls：显示工厂调用和方法调用
# print mockFoo.mock_calls
