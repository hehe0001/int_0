#!/user/bin/env python
#_*_ coding:utf-8 _*_
import requests
import json

class RunMain():
    def __init__(self,url,method,data=None,verify=False):
        self.res=self.run_main(url,method,data=None)

    def send_post(self,url, data):
        res = requests.post(url=url, data=data,verify=False)
        return res.text

    def send_get(self,url, data):
        res = requests.get(url=url, data=data,verify=False)
        #return json.dumps(res, indent=2, sort_keys=True)
        return res.text

    def run_main(self,url, method, data=None):
        res = None
        if method == 'GET':
                res=self.send_get(url,data)
        else:
                res=self.send_post(url,data)
        return res
if __name__=='__main__':
    data = {'t':'1525315800007',
            'Yb-Yh-Client':'0',
            'Yb-Yh-Token': '143da083f9da0bd35f4ac215fec30cf5',
          }
    url = 'https://t.yh.120yibao.com/yb/im/getYTXAccountLoginStatus.do'
    run = RunMain(url,'GET',data,verify=False)
    print run.res





