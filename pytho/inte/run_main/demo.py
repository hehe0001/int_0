#!/user/bin/env python
#_*_ coding:utf-8 _*_
import requests
# urll = 'https://t.yh.120yibao.com/yb/serviceGroup/getConcernDoctorList.do'
# data = {
#     "t":"1527128460976",
#     "Yb-Yh-Client":"0",
#     "Yb-Yh-Token":"3b95651d5e8f7dee47d877f58e6e4f01",
#     "start":"0",
#     "size":"10"
# }
# url = 'https://t.yh.120yibao.com/yb/serviceGroup/getConcernDoctorList.do'
# data = {
# "t":"1528182005840",
# "Yb-Yh-Token":"379772e16a86c93ce238f642b2e72bf6",
# "Yb-Yh-Client":"0",
# "size":"10",
# "start":"0"
#    }
# r = requests.get(url = url,params = data, verify = False)
# print r.text
#
# res = requests.get(url = 'https://t.yh.120yibao.com/yb/serviceGroup/getConcernDoctorList.do?t=1528182005840&Yb-Yh-Client=0'
#                    '&Yb-Yh-Token=379772e16a86c93ce238f642b2e72bf6&start=0'
#                    '&size=10',verify = False)
# print res.text

url = 'https://t.assistant.120yibao.com/yb/assistant/homepage/info'
data = {
    "t":"1528187006611"
    # "yb-assitant-token":"ff5c8cc6583791dc1d7e906df21d205c",
    # "yb_assistant_client":"0"
}
res= requests.post(url=url,data = data,verify = False)
print res.text

r = requests.post('https://t.assistant.120yibao.com/yb/assistant/homepage/info?'
                  't=1528187006611'
                  '&yb-assitant-token=ff5c8cc6583791dc1d7e906df21d205c'
                  '&yb_assistant_client=0',verify = False)
print r.text

