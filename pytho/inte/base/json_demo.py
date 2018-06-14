#!/user/bin/env python
#_*_ coding:utf-8 _*_
import json
fp = open('F:\hyj\pytho\inte\data_config\data.json')
data = json.load(fp)
print data['getPatientMedicalRecordList']
fp.close()