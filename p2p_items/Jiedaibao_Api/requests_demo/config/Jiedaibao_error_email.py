

from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header
'''邮件服务地址，发送邮箱，密码，接受邮箱，主题，内容'''
def send_email(smtp_host='smtp.163.com',from_addr='AfterShipOne@163.com',password='*',to_addrs='993294959@qq.com',subject='hello tiid emali!',content='导致出现554情况，更改了后就好了。'):
    email_client = SMTP(smtp_host)
    email_client.login(from_addr,password)
    msg = MIMEText(content,'plain','utf-8')
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = 'AfterShipOne@163.com'
    msg['To'] = '993294959@qq.com'
    email_client.sendmail(from_addr,to_addrs,msg.as_string())
    email_client.quit()
#send_email('smtp.163.com','AfterShipOne@163.com','*','993294959@qq.com','只是一封邮件，请查收2','hello how are you doing? ')
#send_email(subject='hello this is error email!',content='are you going to beijin ？')
send_email()