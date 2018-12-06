
import logging ,json ,requests
import random
import pymysql
import time
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header

'''
    实现：
        1.数据库里如果存在则直接从数据库里取
        2.输入file可以从本地导入

'''
from config.Headers import jiedaibao_headers

class Jiedaibao_45:
    def __init__(self):
        self.conn = pymysql.Connect(host='localhost', user='root', password='yangfulong.',
                                    port=3306 ,database='p2p_items', charset='utf8')
        self.cursor = self.conn.cursor()
        self.headers = jiedaibao_headers()
        self.data = 'isForeground=1&sessionMode=1&accessToken=ACCESS_TOKEN5220484803798602451520320154486&JDBID=000000003af99e18ffffffffbf30fbdb&deviceID=354730010101230&type=overdueCheck&network=5&deviceType=SM-G955N&memberID=522048480379860245&clientVersion=2.9.8.1&apkSign=6F01335F52FCA82276CC99E2F9E65865&blackBox2=05213F31FF5D8B7D709A5A65498F1E74&fp=&platform=android&isHasCheatSoft=0&env=prod&udid=000000003af99e18ffffffffbf30fbdb&h=1280&w=720&traceID=b94e72e4134d45499b1860fafbd2d801&sysLaunchTimeInterval=66395&isRelease=1&systemVersion=4.4.2&manufacturer=samsung&proxyType=none&phoneVen=1&channel=3001a&appKey=fb371c48e9a9b2a1174ed729ae888513&number=%s&from=h5rrc'
        self.url = 'https://rrcapi.jiedaibao.com/zrrc/collector/user/getOverdue'
        self.tablename = 'jdb2'
    def start_requests(self):
        pass

    '''发起请求，再出现异常的时候，可以尝试更换data再次请求'''
    def get_data(self, Find_Number):
        if self.find_mysql_id(Find_Number) ==0:
            data = self.data % Find_Number
            response = requests.post(url=self.url, headers=self.headers, data=data)
            if response.status_code == 200:
                response_data = response.text
                self.parse_data(response_data, Find_Number)  # 将数据送到解析函数
                self.process_item(Find_Number ,response_data)  # 导入数据库(身份证，data)
        else:
            data = self.find_mysql_id(Find_Number)
            self.find_mysql_id(Find_Number)
            # print(data)


    '''解析response'''
    def parse_data(self, response_data, Find_Number):
        item_values = {}
        try:
            response_dict = json.loads(response_data)
            # if 'error' in response_dict.keys():
            item_values['查询状态'] = response_dict.get('error').get('returnUserMessage')
            # elif 'data' in response_dict.keys():
            datas = response_dict.get('data', '无个人信息：')
            item_values['借贷状态:'] = datas.get('message')
            item_values['姓名：'] = datas.get('info').get('name')
            item_values['年龄：'] = datas.get('info').get('age')
            item_values['身份证：'] = datas.get('info').get('cardId')
            item_values['相片URL：'] = datas.get('info').get('avatar_url')
            item_values['电话号码：'] = datas.get('info').get('phone')
            try:  # 尝试解析征信平台，没有则不返回
                credit = datas.get('credit_platform', '无征信信息')
                if len(credit) < 1:
                    print('没有征信信息！')
                else:
                    try:
                        item_values['征信平台1：'] = datas.get('credit_platform', '无')[1].values()
                        item_values['征信平台2：'] = datas.get('credit_platform', '无')[2].values()
                        item_values['征信平台3：'] = datas.get('credit_platform', '无')[3].values()
                    except:
                        item_values['传征信平台：'] = datas.get('credit_platform', '无征信信息')
            except Exception as e:
                logging.INFO(e)
        except:
            if isinstance(Find_Number, int):
                print('请检查输入是否有误！')
                print('请重新输入！')
            item_values['个人信息'] = '无'
        print('查询号码:{}'.format(Find_Number))
        for i, b in item_values.items():
            alldata = '{}{}'.format(i, b)
            print(alldata)


    '''从本地读取身份证号码自动查询，'''
    def open_file(self):
        while True:
            with open(u'd://data//2.txt', 'r') as f:
                origin = f.readlines()
                for i in origin:
                    content = i.strip()
                    sleep = random.randint(2 ,7)
                    print(content)

                    time.sleep(sleep)
                    print('请求延迟%d秒！ ' %sleep)
                    yield content

    '''创建数据库,如果导入表格不存在则调用此函数创建'''
    def open_spider(self ,table_name):
        # table_name = input('输入数据库名:')
        create_sql = 'CREATE TABLE IF NOT EXISTS %s(' \
                     'ID INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,' \
                     'FIND_TIME TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,' \
                     'INDEX_ID VARCHAR(255),' \
                     'ALL_DATA VARCHAR(5000))ENGINE = INNODB DEFAULT CHARSET=utf8'
        self.cursor.execute(create_sql % table_name)
        self.conn.commit()
        print('Create table ok!')

    '''执行mysql查询判断'''
    def see_mysql(self ,grammar):
        try:
            SeeMysql = '''desc %s'''
            self.cursor.execute(SeeMysql % grammar)
            # data = self.cursor.fetchall()
            self.conn.commit()
        except Exception as e:
            print('No tablename...%s ' %e)
            self.open_spider(grammar)



    def close_spider(self):
        self.cursor.close()
        self.conn.close()
        print('Close databases OK!!!')


    '''查询数据库内有没有idnumber有没有用户id,有则不抓取api端数据'''
    def find_mysql_id(self ,idnumber):
        SeeMysql = '''select * from %s where index_id=%s;'''
        self.cursor.execute(SeeMysql % (self.tablename ,idnumber))
        data = self.cursor.fetchall()
        print(data)
        if len(data) < 1:  # 如果查询结果小于1则执行抓取数据
            print('database is none!')
            return 0
        elif len(data) == 1:
            print('data in fo database !')
            #print(data)
            return data


    '''导入数据库'''
    def process_item(self, IDNumber, AllData):
        try:
            self.see_mysql(self.tablename)  # 检查有没有这个数据库，没有则创建
            insert_table = '''INSERT INTO %s(INDEX_ID,ALL_DATA)VALUES('%s','%s')''' % \
            (self.tablename, IDNumber, AllData)
            self.cursor.execute(insert_table)
            self.conn.commit()
        except Exception as e:
            print(e)

    '''持续查询'''

    def while_demo(self):
        items = Jiedaibao_45()
        try:
            while True:
                Find_Number = input('请输入查询参数(输入ESC退出！):')
                if Find_Number == 'file':
                    index_id = items.open_file()
                    for i in index_id:
                        items.get_data(i)
                Find_Number = Find_Number.strip()
                if Find_Number == 'esc':
                    break
                items.get_data(Find_Number)
        except Exception as e:
            print(e)

    '''主逻辑'''

    def main(self):
        # 执行查询
        self.while_demo()


if __name__ == '__main__':
    items = Jiedaibao_45()
    # items.see_mysql('demo5')
    items.main()
    # items.open_file()
    # items.find_mysql_id(1871198936)
    items.conn.close()
    items.cursor.close()
