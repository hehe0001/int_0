#!/user/bin/env python
#_*_ coding:utf-8 _*_
import requests
import json
fp = open("F:\hyj\pytho\interfance\operation_json.json")
data0 = json.load(fp)
data1 = data0['login']
print data1
data2={
    "Yb-Yh-Toke":"143da083f9da0bd35f4ac215fec30cf5",
    "t":"1525243080699",
    "Yb-Yh-Client":"0"
}
url = 'https://t.yh.120yibao.com/yb/im/getYTXAccountLoginStatus.do'
res = requests.get(url='https://t.yh.120yibao.com/yb/im/getYTXAccountLoginStatus.do',data=data2,verify=False)
print res
print res.text
r=requests.get('https://t.yh.120yibao.com/yb/im/getYTXAccountLoginStatus.do?'
               't=1525243080699&Yb-Yh-Client=0&Yb-Yh-Token=143da083f9da0bd35f4ac215fec30cf5',verify=False)
print r.text
fp.close()
data3={
       "t":"1525243080795",
       "Yb-Yh-Client":"0",
       "Yb-Yh-Token":"143da083f9da0bd35f4ac215fec30cf5",
        "start":"0"
       }
r1=requests.get(url='https://t.yh.120yibao.com/yb/serviceGroup/getConcernDoctorList.do',data=data3,verify=False)
print r1.text
r2=requests.get(url='https://t.yh.120yibao.com/yb/serviceGroup/getConcernDoctorList.do?t=1525243080795&Yb-Yh-Client=0&Yb-Yh-Token=143da083f9da0bd35f4ac215fec30cf5&start=0&size=10',verify=False)
print r2.text