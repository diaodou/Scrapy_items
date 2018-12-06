# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

import pymysql
from wangdaizhijia.smtp_email import SMTP_Email

class WangdaizhijiaPipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(host='localhost',user='root',password='yangfulong.',database='company_data',port=3306,charset='utf8')
        self.cursor = self.conn.cursor()
    def open_spider(self,spider):
       # create_sql = 'CREATE TABLE IF NOT EXISTS P2PCOMPANY3(ID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,COMPANYNAME VARCHAR(255),COMPANYLINK VARCHAR(500))ENGIND=INNODB DEFAULT CHARSET=utf8'

        create_sql ='CREATE TABLE IF NOT EXISTS P2PCOMPANY6(ID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,COMPANYNAME VARCHAR(255),COMPANYLINK VARCHAR(500))ENGINE=MYISAM DEFAULT CHARSET=utf8;'

        self.cursor.execute(create_sql)
                   # 'CREATE TABLE IF NOT EXISTS P2PCOMPANY1(ID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,COMPANYNAME VARCHAR(255),COMPANYLINK VARCHAR(500))ENGINE=MYISAM DEFAULT CHARSET=utf8;'

    def process_item(self, item,spider):
        error_email = SMTP_Email()
        companyname = item.get('company_name')
        companylink = item.get('company_link')
        try:
            insert_sql = 'INSERT INTO P2PCOMPANY6(COMPANYNAME,COMPANYLINK)VALUES({},{});'#.format(companyname,companylink)
            #data = (companyname,companylink)
            self.cursor.execute(insert_sql.format(companyname,companylink))

            self.conn.commit()
        except Exception as e:
            logging.debug('===出现异常===%s'%e)

            error_email.main('这是一封邮件，请查收','异常是%s'%e)        #发送错误异常到邮件


    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

