import json
import logging
import random
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header
import requests
import time

from config.mysql_2_0 import Mysql_wuyou
from config.wuyou_headers import WuyouHeaders
from multiprocessing import Pool

'''
    此类功能：
        1.对无忧借条使用身份证进行查询违约记录
        2.通过改变data的{"args":["45de5b6bd782ccc810de37737d7e33f2","411324199106280916"]    值进行身份查询
    可实现：
        1.手动输入查询
        2.短信方式提醒
        3.异步请求提升，可大规模请求
    问题：
        1.对无忧借到的查询限制数量，未做判断
        2.未知app是否会进行怎样的反爬虫措施，针对被反爬虫，需要对应实际情况解决

'''
#from config.mysql_demo import Mysql_IDNumber


class IDNumber:
    #411324199106280916
    def __init__(self):
        self.IDNmber_id = input('请输入查询信息:')
        self.mysql_function = Mysql_wuyou()
        self.headers = WuyouHeaders()
        self.data = 'json={"args":["45de5b6bd782ccc810de37737d7e33f2","%s"],"argsclass":["java.lang.String","java.lang.String"],"methodName":"findDishonestUserV2ByYxbIdOrIdCardNo","proxy":"CreditCenterManagerV2"}' % self.IDNmber_id
        self.url = 'https://www.51jt.com/api.jsp'

    '''开始判断，数据库内有没有对应值'''

    def start_requests(self):
        find_mysql_data = self.mysql_function.find_mysql_id(self.IDNmber_id)  # 判断数据库内有没有这个id
        if find_mysql_data < 1:  # 抓取数据
            self.get_response()
        elif find_mysql_data == 1:  # 已存在从数据库中取
            print('从数据库中取')


    '''开始'''
    def get_response(self):
        self.mysql_function.see_mysql2()
        try:
            response = requests.post(url=self.url, data=self.data, headers=self.headers)
            if response.status_code == 200:
                alldata = response.text
                self.mysql_function.process_item(self.IDNmber_id, alldata)  # 存入mysql
                self.parse_response(alldata)
                return alldata
            elif response.status_code != 200:
                print(response.status_code)
        except Exception as e:
            raise TypeError('is error %s' % e)



    '''解析response'''
    def parse_response(self, alldata):
        alldatas = json.loads(alldata)
        for i, b in alldatas.items():
            print(i, b)

    '''多进程'''
    def mutilprocess_pool(self):
        pass


    '''email异常推送'''
    def send_email(self, subject, content):
        smtp_host = 'smtp.163.com'
        from_addr = 'AfterShipOne@163.com'
        password = '*'
        to_addrs = '993294959@qq.com'
        email_client = SMTP(smtp_host)
        email_client.login(from_addr, password)
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = 'AfterShipOne@163.com'
        msg['To'] = '993294959@qq.com'
        email_client.sendmail(from_addr, to_addrs, msg.as_string())
        email_client.quit()

    '''读取本地文件参数'''

    def local_file(self):
        filename = input('请输入d:/data/(文件名)')
        with open(u'd://data//%s.txt' % filename, 'r') as f:
            s = f.readlines()
            lens = len(s)
            for i in s:
                content = i.strip()
                sleep = random.randint(1,10)
                time.sleep(sleep)
                yield content

    '''主逻辑'''
    def main(self):
        try:
            self.start_requests()
        except Exception as e:
            self.send_email('这是来自无忧2.0脚本的错误！','error is :%s'%e)
            

if __name__ == '__main__':
    id = IDNumber()
    id.main()




