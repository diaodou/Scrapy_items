import logging

import requests
import json
import logging
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header
import requests
from config.mysql_demo import Mysql_IDNumber
from config.wuyou_headers import WuyouHeaders

class IDNumber:
    headers = {
        'User-Agent' :'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)',
        'Connection' :'Keep-Alive',
        'x-phoneType' :'android',
        'x-YxbCookie' :'447675745|8689164b3b88c729cdb12c80b69f9608',
        'x-version' :'3.35',
        'x-osVersion' :'4.4.2',
        'x-phoneModel' :'dream2lteks',
        'x-imsi' :'460071012344126',
        'x-channeId' :'9999',
        'x-HWUserToken' :'45de5b6bd782ccc810de37737d7e33f2',
        'x-imei' :'354730010101230',
        'x-simNumber' :'',
        'x-deviceToken' :'',
        'x-androidDeviceToken' :'xvO61bqPJHOES62kG5PcKMTJWgdIag8hTxMvSL3fcBM=',
        'x-guid' :'26dbdd214790a1010adf15d85e926cb9',
        'x-udid' :'ee42a0e31e418ff6637d256d8b8808db201803081818531c31be393d879d49dd49f4c7b4ae3fb2',
        'x-device' :'SM-G955N',
        'x-uniqueId' :'39d1f5e87748f596f95bd162908979606d6522785839ef50',
        'Content-Type' :'application/x-www-form-urlencoded',
        'Host' :'www.51jt.com',
        'Accept-Encoding' :'gzip',
        'Content-Length' :'207',}
    #data = 'json={"args":["45de5b6bd782ccc810de37737d7e33f2","431124199412116332"],"argsclass":["java.lang.String","java.lang.String"],"methodName":"findDishonestUserV2ByYxbIdOrIdCardNo","proxy":"CreditCenterManagerV2"}'
    url = 'https://www.51jt.com/api.jsp'
    data = 'json={"args":["45de5b6bd782ccc810de37737d7e33f2","431124199412116332"],"argsclass":["java.lang.String","java.lang.String"],"methodName":"findDishonestUserV2ByYxbIdOrIdCardNo","proxy":"CreditCenterManagerV2"}'
   # url = 'https://www.51jt.com/api.jsp'
    # def get_data(self):
    #     try:
    #         response = requests.post(url=self.url,data=self.data,headers=self.headers)
    #         print(response.text)
    #         if  response.status_code == 200:
    #             print(response.text)
    #         if response.status_code != 200:
    #             print(response.status_code)
    #     except Exception as e :
    #         raise TypeError('is error %s'%e)



    def get_data(self):
        response = requests.post(url=self.url,data=self.data,headers=self.headers)
        print(response.text)
        if  response.status_code == 200:
            print(response.text)
        if response.status_code != 200:
            print(response.status_code)
            logging.DEBUG()



    def send_email(self, subject,content):
        smtp_host = 'smtp.163.com'
        from_addr = 'AfterShipOne@163.com'
        password = '*'
        to_addrs = '993294959@qq.com'
        email_client = SMTP(smtp_host,25)
        email_client.login(from_addr, password)
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = 'AfterShipOne@163.com'
        msg['To'] = '993294959@qq.com'
        email_client.sendmail(from_addr,to_addrs,msg.as_string())
        #email_client.quit()


i = IDNumber()
i.send_email('这是一封邮件，请查收！','are you gointo baijin and shanghai or hunana?')