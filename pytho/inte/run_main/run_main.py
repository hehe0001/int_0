#!/user/bin/env python
#_*_ coding:utf-8 _*_
import requests
import json
class Run_main:
    def __init__(self,url,method,data=None):
        self.res = self.run_main(url,method,data)
    def send_post(self,url,data):
        self.res = requests.post(url, data, verify=False)
        return self.res
    def send_get(self,url,data):
        self.res = requests.get(url, data, verify=False)
        return self.res
    def run_main(self,url,method,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res
if __name__ == '__main__':
    url = 'https://t.yh.120yibao.com/yb/im/resetUnreadMsgCount.do'
    data = {
        "t": "1527134081498",
        "Yb-Yh-Client": "0",
        "Yb-Yh-Token": "3b95651d5e8f7dee47d877f58e6e4f01",
        "conversationId": "6194"
    }
    run = Run_main(url,'POST',data)
    print run.res.text