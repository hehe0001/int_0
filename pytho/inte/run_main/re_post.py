#!/user/bin/env python
#_*_ coding:utf-8 _*_
import requests

def send_post(url,data):
    res = requests.post(url,data,verify = False)
    return res
if __name__ == "__main__":
    url = 'https://t.yh.120yibao.com/yb/im/resetUnreadMsgCount.do'
    data = {
        "t":"1527134081498",
        "Yb-Yh-Client":"0",
        "Yb-Yh-Token":"3b95651d5e8f7dee47d877f58e6e4f01",
        "conversationId":"6194"
    }
    res = send_post(url=url,data = data)
    print res.text

