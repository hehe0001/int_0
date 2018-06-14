#!/user/bin/env python
#_*_ coding:utf-8 _*_
import json
class OperationJson:
    def __init__(self):
        self.data=self.read_data()
    #读取json文件
    def read_data(self):
        # fp=open('F:\hyj\pytho\interfance\operation_json.json')
        # fp.close()
        #使用with，不需要再单独关闭fp
        with open('F:\hyj\pytho\interfance\operation_json.json') as fp:
            self.data=json.load(fp)
            return self.data
    #根据关键字获取数据
    def get_data(self,id):
        return self.data[id]
if __name__=='__main__':
    opjson=OperationJson()
    print opjson.get_data('phoneConsult')

