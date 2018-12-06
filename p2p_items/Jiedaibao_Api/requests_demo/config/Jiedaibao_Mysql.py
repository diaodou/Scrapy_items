import logging

import pymysql


class JDB_Mysql:
    def __init__(self):
        self.conn = pymysql.Connect(host='localhost', user='root', password='yangfulong.', port=3306,
                                    database='p2p_items', charset='utf8')
        self.cursor = self.conn.cursor()


    '''创建数据库,如果导入表格不存在则调用此函数创建'''
    def open_spider(self,table_name):
        #table_name = input('输入数据库名:')
        create_sql = 'CREATE TABLE IF NOT EXISTS %s(' \
              'ID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,' \
              'FIND_TIME TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,' \
              'ID_NUMBER VARCHAR(255),' \
              'ALL_DATA VARCHAR(255),' \
              'ALL_DATA VARCHAR(255),' \
              'ALL_DATA VARCHAR(255),' \
              'ALL_DATA VARCHAR(255),' \
              'ALL_DATA VARCHAR(255),' \
              'ALL_DATA VARCHAR(255),' \
              'ALL_DATA VARCHAR(255),' \
              'E VARCHAR(255))ENGINE = INNODB DEFAULT CHARSET=utf8'
        self.cursor.execute(create_sql%table_name)
        self.conn.commit()
        print('Create table ok!')
        #self.close_spider()


    '''导入数据库'''
    def process_item(self,IDNumber,AllData):
        #table_name = input('输入数据库名 or see table or drop table')
        table_name = 'jiedaibao_data'

        self.open_spider(table_name)
        #insert_table ='''INSERT INTO %s(ID_NUMBER,ALL_DATA)VALUES('name','yangfulong')'''#%(table_name,index_number,all_data)
        insert_table ='''INSERT INTO %s(ID_NUMBER,ALL_DATA)VALUES('%s','%s')'''%(table_name,IDNumber,AllData)
        self.cursor.execute(insert_table)
        self.conn.commit()
        print('Insert table ok!')
        if table_name == 'drop table':
            #table_name.strip()
            self.drop_table()
        if table_name == 'see table':
            #table_name.strip()
            self.see_mysql()

        self.close_spider()

    '''关闭数据库'''
    def close_spider(self):
        self.cursor.close()
        self.conn.close()
        print('Close databases OK!!!')

    '''删除表格'''
    def drop_table(self):
        while True:
            tablename = input('请输入需要删除的表：esc退出:')
            tablename = tablename.strip()
            if tablename == 'esc':
                break
            try:
                drop_table = '''DROP TABLES %s'''
                self.cursor.execute(drop_table%tablename)
                self.conn.commit()
                print('delete table %s ok！'%drop_table)
            except:
                print('输入错误请重新输入:')
            finally:
                self.close_spider()

    '''使用mysql语法查看数据库'''
    def see_mysql(self):
        while True:
            try:
                grammar= input('请输入查询参数：')
                grammar = grammar.strip()
                if grammar == 'esc':
                    self.close_spider()
                    break

                #SeeMysql = '''%s'''
                SeeMysql = '''select * from demo1 where id_number=%s;'''
                self.cursor.execute(SeeMysql%grammar)
                data = self.cursor.fetchall()
                print(data)
                if len(data) < 1:
                    print('数据库里没有')
                    return len(data)
                else:
                    print('数据库里有！')

            except:
                print('请检查输入参数是否有误！')


M=JDB_Mysql()
#M.insert_mysql()
#M.open_spider()
#M.drop_table()
M.see_mysql()