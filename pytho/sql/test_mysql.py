#!/user/bin/env python
#_*_ coding:utf-8 _*_
import mysql.connector
db = mysql.connector.connect(host = 'localhost',
                             user = 'root',
                             passwd = '123456',
                             db = 'my_python',
                             charset='utf8')
cur = db.cursor()

sql1 = 'INSERT INTO user_info (ID,user_id,username,Qpingyin) VALUES (%s,%s,%s,%s)'
para1 = ('2','1002','李四','lisi')
r1 = cur.execute(sql1,para1)
#r1 = cur.fetchall()
db.commit()
print r1
effect_row = cur.execute('select * from user_info')
effect_row = cur.fetchall()
db.commit()
print effect_row
cur.close()
db.close

