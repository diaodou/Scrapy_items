


from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header
'''邮件服务地址，发送邮箱，密码，接受邮箱，主题，内容'''

class  SMTP_Email:

    def send_email(self,smtp_host,from_addr,password,to_addrs,subject,content):
        email_client = SMTP(smtp_host)
        email_client.login(from_addr,password)
        msg = MIMEText(content,'plain','utf-8')
        msg['Subject'] = Header(subject,'utf-8')
        msg['From'] = 'AfterShipOne@163.com'
        msg['To'] = '993294959@qq.com'
        email_client.sendmail(from_addr,to_addrs,msg.as_string())

    def main(self,subject,content):
        self.send_email('smtp.163.com','AfterShipOne@163.com','*','993294959@qq.com',subject,content)

# s = SMTP_Email()
# s.main('这是一封邮件，请不要查收，谢谢','hello  这里出现了xxx异常，请过来查收')

