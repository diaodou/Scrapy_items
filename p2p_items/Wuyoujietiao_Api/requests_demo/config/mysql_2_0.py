





import pymysql
import logging

'''通过身份证号码保存'''
class Mysql_wuyou:
    def __init__(self):
        self.conn = pymysql.Connect(host='localhost', user='root', password='yangfulong.', port=3306,
                                    database='p2p_items', charset='utf8')
        self.cursor = self.conn.cursor()
        self.tablename = 'wuyou1'

    '''创建数据库,如果导入表格不存在则调用此函数创建'''
    def open_spider(self, table_name):
        # table_name = input('输入数据库名:')
        create_sql = 'CREATE TABLE IF NOT EXISTS %s(' \
                     'ID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,' \
                     'FIND_TIME TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,' \
                     'ID_NUMBER VARCHAR(255),' \
                     'ALL_DATA VARCHAR(255),' \
                     'E VARCHAR(255))ENGINE = INNODB DEFAULT CHARSET=utf8'
        self.cursor.execute(create_sql % table_name)
        self.conn.commit()
        print('Create table ok!')
        
        
    '''导入数据库'''
    def process_item(self ,IDNumber ,AllData):
        # table_name = input('输入数据库名 or see table or drop table')
        
        #self.see_mysql2(self.tablename)  # 执行查询，没有这个数据库则创建
        # self.open_spider(table_name)
        # insert_table ='''INSERT INTO %s(ID_NUMBER,ALL_DATA)VALUES('name','yangfulong')'''#%(table_name,index_number,all_data)
        insert_table ='''INSERT INTO %s(ID_NUMBER,ALL_DATA)VALUES('%s','%s')''' % (self.tablename, IDNumber, AllData)
        self.cursor.execute(insert_table)
        self.conn.commit()
        print('Insert table ok!')

        
    '''关闭数据库'''
    def close_spider(self):
        self.cursor.close()
        self.conn.close()
        print('Close databases OK!!!')


    '''查看数据库，没有则创建'''
    def see_mysql2(self):
        try:
            # grammar = input('请输入查询语句：')
            SeeMysql = '''desc %s'''
            self.cursor.execute(SeeMysql % self.tablename)
            data = self.cursor.fetchall()

            self.conn.commit()
        except:
            self.open_spider(self.tablename)
            print('open_spider_create_table_ok!')



    '''查询数据库内有没有idnumber有没有用户id,有则不抓取api端数据'''
    def find_mysql_id(self, idnumber):
        SeeMysql = '''select * from demo1 where id_number=%s;'''
        self.cursor.execute(SeeMysql % idnumber)
        data = self.cursor.fetchall()
        if len(data) < 1:  # 如果查询结果小于1则执行抓取数据
            print('database is none!')
            return 0
        else:
            print('data in fo database !')
            print(data)
            return data