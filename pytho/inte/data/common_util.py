#!/user/bin/env python
#_*_ coding:utf-8 _*_
import json
class CommonUtil:
    def is_contain(self,str_one,str_two):
        '''
        判断一个字符串是否在另一个字符串中
        :param str_one:查找的字符串
        :param str_two:被查找的字符串
        :return:
        '''
        flag = None
        #if isinstance(str_one,unicode):
            #str_one = str_one.encode('unicode-escape').decode('string_escape')
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
if __name__ == '__main__':
    str1 = "请求成功"
    str = '{"status":0,"info":"请求成功","data":{"conversationId":6194},"timeStamp":1528194494409}'
    print type(str)
    str2 = json.dumps(str,ensure_ascii=False)#用json转义之后，编码格式发生变化，中文在字典和json转换之后的编码方式不一样
    print type(str2)
    com = CommonUtil()
    r = com.is_contain(str1,str2)
    print r
    if r:
        print 'pass'
    else:
        print 'error'
