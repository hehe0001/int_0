#!/user/bin/env python
#_*_ coding:utf-8 _*_
import mock
#mock方法封装
def mock_test(mock_method,request_data,response_data,url,method):
    mock_method=mock.Mock(return_value=response_data)
    res=mock_method(url,method,request_data)
    return res

