#!/user/bin/env python
#_*_ coding:utf-8 _*_
import smtplib
from email.header import Header
from email.mime.text import MIMEText

class SendEmail:
    global send_user
    global email_host
    global password
    send_user = "15990148703@163.com"
    email_host = "smtp.163.com"
    password = "hehe080065"
    def send_mail(self,user_list,sub,content):
        user = ""+"<"+send_user+">"
        message = MIMEText(content,_subtype='plain',_charset='utt-8')
        message['Subject'] = Header(sub,'utf-8')
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

    def send_main(self,pass_list,error_list):
        pass_num = float(len(pass_list))
        error_num = float(len(error_list))
        count_num = pass_num + error_num
        #统计百分比
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        error_result = "%.2f%%" % (error_num / count_num * 100)

        sub = "接口自动化测试报告"
        user_list = ['15990148703@163.com']
        content = "此次一共运行接口个数为%s个，通过数量为%s个，失败数量为%s个" \
                  "通过率为%s，失败率为%s" % (count_num,pass_num,error_num,pass_result,error_result)
        self.send_mail(user_list,sub,content)

if __name__ == "__main__":
    sen = SendEmail()
    sen.send_main([1,2,3,4,5,1,2,3,4,5,2,3,4,2],[2,3,4])
