#!/user/bin/env python
#_*_ coding:utf-8 _*_
import json
class CommonUtil:
    def is_contain(self,str_one,str_two):

        '''
        判断一个字符串是否包含在另一个字符串中
        :param str_one:查找的字符串
        :param str_two:被查找的字符串
        :return:
        '''
        flag = None
        #if isinstance(str_one,unicode):
            #str_one=str_one.encode("unicode-escape").decode("string-escape")
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

if __name__=="__main__":
    com=CommonUtil()
    re= '"info":"获取会话成功!"'
    res="info"
    data={"status": 0,' \
         '"info": "获取会话成功!"}

    print com.is_contain(res,data)