#!/user/bin/env python
#_*_ coding:utf-8 _*_
import requests
import json
url0='https://t.yh.120yibao.com/yb/im/getImMsgTemplateInfo.do'
data0={
    't':'1524193658241',
     'Yb-Yh-Client':'0',
     'Yb-Yh-Token':'143da083f9da0bd35f4ac215fec30cf5',
     'key':'chat_room'
    }
res=requests.get(url=url0,params=data0,verify=False)
print res.text

url1 = 'https://t.yh.120yibao.com/yb/im/getConversationInfo.do'
data1 = {    'Yb-Yh-Token': '143da083f9da0bd35f4ac215fec30cf5',
             'conversationId': '6199',
             't': '1525341848643',
            'Yb-Yh-Client': '0',
            'isFirst': '1'}
res=requests.get(url=url1,params=data1,verify=False)
print res.text
res=requests.get('https://t.yh.120yibao.com/yb/im/getConversationId?t=1525417939649&Yb-Yh-Client=0&'
                 'Yb-Yh-Token=143da083f9da0bd35f4ac215fec30cf5&doctorUserId=141273&patientId=534',verify=False)
print res.text


url2='https://t.yh.120yibao.com/yb/im/getHistoryMsgByMsgTime.do'
data2 = {
            'Yb-Yh-Token': '143da083f9da0bd35f4ac215fec30cf5',
             'conversationId': '6199',
             't': '1525341848819',
            'Yb-Yh-Client': '0',
            'num': '20',
            'voip':'80002500000131',
            'msgTime':'-1',
            'patientId':'534'
}
res=requests.get(url=url2,params=data2,verify=False)
print res.text
