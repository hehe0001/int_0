#!/user/bin/env python
#_*_ coding:utf-8 _*_
import requests
import json
url1 = 'https://t.yh.120yibao.com/yb/im/getYTXAccountLoginStatus.do'
data1= {
        "t":"1528443229734",
        "Yb-Yh-Client":"0",
        "Yb-Yh-Token":"379772e16a86c93ce238f642b2e72bf6"
        }
res = requests.get(url = url1,params= data1,verify = False)
print res.text
url2 = 'https://t.yh.120yibao.com/yb/serviceGroup/getConcernDoctorList.do'
data2 ={
        "t":"1528443642753",
        "Yb-Yh-Client":"0",
        "Yb-Yh-Token":"379772e16a86c93ce238f642b2e72bf6",
        "start":"0",
        "size":"10"
        }
res1 = requests.get(url=url2,params=data2,verify = False)
print res1.text
url3 = 'https://t.yh.120yibao.com/yb/shopCenter/getOnLineCommodityDetail'
data3 = {
        "t":"1528702731939",
        "Yb-Yh-Client":"0",
        "Yb-Yh-Token":"379772e16a86c93ce238f642b2e72bf6",
        "doctorUserId":"141273",
        "serviceType":" 2"
        }
r3 = requests.get(url=url3,params=data3,verify = False)
print r3.text
url4 = 'https://t.yh.120yibao.com/yb/cache/get.do'
data4 = {
        "t":"1528444241012",
        "Yb-Yh-Client":"0",
        "Yb-Yh-Token":"379772e16a86c93ce238f642b2e72bf6",
        "key":"mall_service_apply_form"
        }
r4 = requests.get(url=url4,params=data4,verify = False)
print r4.text
r = json.loads(r4.text)
data = r['data']
data = json.loads(data)
orderType = data['orderType']
priceId = data['priceId']
processDefinitionId = data['processDefinitionId']
commodityId = data['commodityId']
url5 = 'https://t.yh.120yibao.com/yb/shopCenter/process/initForm.do'
data5 ={
        "t":"1528444241148",
        "Yb-Yh-Client":"0",
        "Yb-Yh-Token":"379772e16a86c93ce238f642b2e72bf6",
        "processDefinitionId":""
        }
data5['processDefinitionId']=processDefinitionId
r5 = requests.get(url=url5,params=data5,verify = False)
print r5.text
url6 = 'https://t.yh.120yibao.com/yb/patient/getPatientlist.do'
data6 = {
        "t":"1528444241196",
        "Yb-Yh-Client":"0",
        "Yb-Yh-Token":"379772e16a86c93ce238f642b2e72bf6",
        "pageSize":"1000",
        "pageNum":"0"
        }
r6 = requests.get(url=url6,params=data6,verify = False)
print r6.text
url7 = 'https://t.yh.120yibao.com/yb/process/pre'
data7 = {
        "t":"1528446622505",
        "Yb-Yh-Client":"0",
        "Yb-Yh-Token":"379772e16a86c93ce238f642b2e72bf6",
        "commodityId":"",
        "doctorUserId":"141273",
        "patientId":"1805"
        }
data7['commodityId'] =commodityId
r7 = requests.get(url=url7,params=data7,verify = False)
print r7.text
url8 = 'https://t.yh.120yibao.com/yb/shopCenter/process/startProcess.do'
header8 = {
        "Yb-Yh-Token":"379772e16a86c93ce238f642b2e72bf6",
        "Content-Type":"application/json"
        }
data8 = {

        "catType":"","priceId":"","patientId":"1805","commodityId":"","processDefinitionId":"",
         "formInstance":{"templateId":659,"templateName":"基础服务在线咨询预约信息单",
                         "fieldInstanceList":[{"componentId":17,"fieldId":7540,"fieldTypeId":3,
                                               "fieldValueName":"甘特图过二十广东省高第三方 反而","fieldValueId":""},
                                              {"fieldId":7541,"fieldTypeId":9,"fieldValueName":"","fieldValueId":""}]}}
data8['catType'] = orderType
data8['priceId'] = priceId
data8['commodityId'] = commodityId
data8['processDefinitionId'] = processDefinitionId
r8 = requests.post(url=url8,data=json.dumps(data8),headers = header8,verify = False)
print r8.text
s = json.loads(r8.text)
ds = s['data']
processInstanceId = s['data']['processInstanceId']
url9 = 'https://t.yh.120yibao.com/yb/shopCenter/saveOrder.do'
# header9 = {
#         "Yb-Yh-Token":"379772e16a86c93ce238f642b2e72bf6"
#         }
data9 = {
        "Yb-Yh-Token":"379772e16a86c93ce238f642b2e72bf6",
        "isFree":"0",
        "catType":"",
        "priceId":"",
        "referer":"1",
        "patientId":"1805",
        "commodityId":"",
        "processInstanceId":"",
        "isAnonymousDisplay":"1"
        }
data9['catType'] = orderType
data9['priceId'] = priceId
data9['commodityId'] = commodityId
data9['processInstanceId'] = processInstanceId
r9 = requests.post(url=url9,data=data9,verify = False)
print r9.text
