#!/user/bin/env python
#_*_ coding:utf-8 _*_
import requests

url1 = 'https://t.yh.120yibao.com/yb/cache/put.do'
para = {
    "t":"1525760513417",
    "Yb-Yh-Client":"0",
    "Yb-Yh-Token":"3b95651d5e8f7dee47d877f58e6e4f01",
    "key":"mall_service_apply_form",
    "data":{
        "orderType":"10",
        "priceId":"4090",
        "doctor":
            {
                "name":"呵呵测试",
                "imgPath":"https://ognvoq0qy.qnssl.com/doctor-man.png-mini",
                "itemName":"营养科",
                "titleName":"主治医师",
                "hospitalName":"浙江大学附属第一医院",
                "userId":"141273"
            },
        "hasPriceFavorable":"0",
        "processDefinitionId":"11408",
        "prevPage":"consult_my",
        "commodityId":"11282"
        }
}

res1=requests.post(url=url1,data=para,verify=False)
print res1.text