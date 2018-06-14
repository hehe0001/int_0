#!/user/bin/env python
#_*_ coding:utf-8 _*_
import requests
import json
class RunMethod:
    def post_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header,verify = False)
        else:
            res = requests.post(url=url,data= data,verify = False)
        #res = json.dumps(res.text, ensure_ascii=False)
        return res.json()
    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,params=data,headers=header,verify = False)
        else:
            res = requests.get(url=url,params= data,verify = False)
        #res = json.dumps(res.text, ensure_ascii=False)
        return res.json()
    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'POST':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
            return json.dumps(res, ensure_ascii=False, indent=2, sort_keys=False)#json转换，同时保留中文
if __name__ == '__main__':
    run = RunMethod()
