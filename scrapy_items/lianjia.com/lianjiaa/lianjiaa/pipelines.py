# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class LianjiaaPipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(host='x',user='x',password='x',database='x',port=3306,charset='utf8')
        self.cursor=self.conn.cursor()

    def open_spider(self,spider):
        crate_sql = 'CREATE TABLE IF NOT EXISTS LIANJIA17(ID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,TYPE VARCHAR(500),LINK VARCHAR(255),PRICE CHAR(50),URL VARCHAR(500))ENGINE=MYISAM DEFAULT CHARSET=UTF8; '
        self.cursor.execute(crate_sql)

    def process_item(self, item, spider):
        type = item.get('host_type','N/A')
        link = item.get('host_link','N/A')
        price = item.get('host_price','N/A')
        url = item.get('host_url')
        sql = "INSERT INTO lianjia17(TYPE,LINK,PRICE,URL)VALUES(%s,%s,%s,%s);"
        data =  (type,link,price,url)
        self.cursor.execute(sql,data)
        self.conn.commit()

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()


