#!/user/bin/env python
#_*_ coding:utf-8 _*_
import requests

url = 'https://t.yh.120yibao.com/yb/shopCenter/saveOrder.do'
data = {
"t":"1525760513417",
"Yb-Yh-Client":"0",
"Yb-Yh-Token":"3b95651d5e8f7dee47d877f58e6e4f01",
"isFree":"0",
"catType":"10",
"priceId":"4090",
"refer":"1",
"patientId":"1769",
"commodityId":"11282",
"processInstanceId":"12205",
"isAnonymousDisplay":"1"
}
res= requests.post(url=url,data=data,verify = False)
#requests.packages.urllib3.disable_warnings()
print res.text