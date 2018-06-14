#!/user/bin/env python
#_*_ coding:utf-8 _*_
import requests
import json
class RunMethod:
    def post_main(self,url,data,header=None):
        res=None
        if header!= None:
            res = requests.post(url=url,data=data,headers=header,verify=False)
        else:
            res = requests.post(url=url,data=data,verify=False)
            print res.status_code
        return res.json()
    def get_main(self,url,data=None,header=None):
        res = None
        if header!= None:
            res = requests.get(url=url,params=data,headers=header,verify=False)
        else:
            res = requests.get(url=url,params=data,verify=False)
            print res.status_code
        return res.json()
    def run_main(self,method,url,data=None,header=None):
        res=None
        if method=='POST':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dumps(res,ensure_ascii=False,indent=2,sort_keys=False)
if __name__=='__main__':
    run = RunMethod()
    url1='https://t.yh.120yibao.com/yb/im/getConversationInfo.do'
    data1={
        't':'1525341848643',
        'Yb-Yh-Client':'0',
        'Yb-Yh-Token':'379772e16a86c93ce238f642b2e72bf6',
        'conversationId':'6199',
        'isFirst':'1'
          }
    method1 ="GET"

    #res = run.run_main(method1,url1,data1,header=None)
    #print res
    r=requests.get(url=url1,params=data1,verify=False)
    print r.text
    re=requests.get('https://t.yh.120yibao.com/yb/im/getConversationInfo.do?t=1525341848643&Yb-Yh-Client=0'
                    '&Yb-Yh-Token=379772e16a86c93ce238f642b2e72bf6&conversationId=6199&isFirst=1',verify=False)
    print re.text

