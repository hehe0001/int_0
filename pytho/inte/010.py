#!/user/bin/env python
#_*_ coding:utf-8 _*_
import requests
import json
url1 = 'https://t.yh.120yibao.com/yb/im/getConversationId'
data1 = {
    "t":"1528189798697",
    "Yb-Yh-Client":"0",
    "Yb-Yh-Token":"379772e16a86c93ce238f642b2e72bf6",
    "patientId":"532",
    "doctorUserId":"141273"
    }
res1 = requests.get(url=url1,params=data1,verify = False)
print res1.text
conversationId = json.loads(res1.text)['data']['conversationId']
print conversationId
