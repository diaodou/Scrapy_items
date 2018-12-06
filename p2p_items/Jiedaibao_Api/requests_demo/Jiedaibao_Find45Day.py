
import logging,json,requests
import random
import pymysql
import time
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header
from requests_demo.config.Jiedaibao_Mysql import JDB_Mysql
#from Jiedaibao_Api.requests_demo.config.Jiedaibao_Mysql import Jiedaibao
'''
    说明：
        此类负责查询借贷宝45天逾期记录：
    功能：
        1.手动输入身份证或电话号进行违约查询
        2.使用本地文件大量查询
        
    问题：
        1.未知借贷宝允许当个用户的查询数量限制
        
    解决方法：
        1.要是借贷号被反爬虫
            1.更换代理
            2.通过注册新号输入账号密码
    欠缺：
        1.保存到数据库
        2.使用flask实现接口
        3.使用random调用随机接口查询
            
'''

class Jiedaiba_45Day:
    #Find_Number= '#'      #可以手动输入
    #Find_Number= input('请输入需要查询的信息：')     #可以手动输入
    def __init__(self):
        self.conn = pymysql.Connect(host='localhost', user='root', password='yangfulong.',
                                    port=3306,database='p2p_items', charset='utf8')
        self.cursor = self.conn.cursor()

    '''从本地读取身份证号码自动查询，'''
    def open_file(self):
        while True:
            with open(u'd://data//1.txt','r') as f:
                origin = f.readlines()
                for i in origin:
                    content = i.strip()
                    sleep = random.choice()
                    time.sleep(3)
                    yield content

    '''异常时发送邮件提醒：邮件服务地址，发送邮箱，密码，接受邮箱，主题，内容'''
    def send_email(smtp_host='smtp.163.com', from_addr='AfterShipOne@163.com', password='*',
                   to_addrs='993294959@qq.com', subject=None, content=None):
        email_client = SMTP(smtp_host)
        email_client.login(from_addr, password)
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = 'AfterShipOne@163.com'
        msg['To'] = '993294959@qq.com'
        email_client.sendmail(from_addr, to_addrs, msg.as_string())

    '''创建数据库,如果导入表格不存在则调用此函数创建'''
    def open_spider(self, table_name):
        # table_name = input('输入数据库名:')
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
        self.cursor.execute(create_sql % table_name)
        self.conn.commit()
        print('Create table ok!')

    '''导入数据库'''
    def process_item(self, IDNumber, AllData):
        # table_name = input('输入数据库名 or see table or drop table')
        table_name = 'jiedaibao_data'

        self.open_spider(table_name)
        # insert_table ='''INSERT INTO %s(ID_NUMBER,ALL_DATA)VALUES('name','yangfulong')'''#%(table_name,index_number,all_data)
        insert_table = '''INSERT INTO %s(ID_NUMBER,ALL_DATA)VALUES('%s','%s')''' % (table_name, IDNumber, AllData)
        self.cursor.execute(insert_table)
        self.conn.commit()

    '''发起请求，再出现异常的时候，可以尝试更换data再次请求'''
    def get_data(self,Find_Number):
        headers = {
        'Host':'rrcapi.jiedaibao.com',
        'Connection':'keep-alive',
        'Content-Length':'660',
        'Accept':'application/json, text/plain, */*',
        #'Origin:file':'//',
        'User-Agent':'Mozilla/5.0 (Linux; Android 4.4.2; SM-G955N Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
        'Accept-Encoding':'gzip,deflate',
        'Accept-Language':'zh-CN,en-US;q=0.8',
        'X-Requested-With':'com.rrh.jdb',}
        data = 'isForeground=1&sessionMode=1&accessToken=ACCESS_TOKEN5220484803798602451520320154486&JDBID=000000003af99e18ffffffffbf30fbdb&deviceID=354730010101230&type=overdueCheck&network=5&deviceType=SM-G955N&memberID=522048480379860245&clientVersion=2.9.8.1&apkSign=6F01335F52FCA82276CC99E2F9E65865&blackBox2=05213F31FF5D8B7D709A5A65498F1E74&fp=&platform=android&isHasCheatSoft=0&env=prod&udid=000000003af99e18ffffffffbf30fbdb&h=1280&w=720&traceID=b94e72e4134d45499b1860fafbd2d801&sysLaunchTimeInterval=66395&isRelease=1&systemVersion=4.4.2&manufacturer=samsung&proxyType=none&phoneVen=1&channel=3001a&appKey=fb371c48e9a9b2a1174ed729ae888513&number=%s&from=h5rrc'% Find_Number
        url = 'https://rrcapi.jiedaibao.com/zrrc/collector/user/getOverdue'
        response= requests.post(url=url,headers=headers,data=data)
        if response.status_code == 200:
            response_data = response.text
            self.parse_data(response_data,Find_Number)      #将数据送到解析函数

    '''解析response'''
    def parse_data(self,response_data,Find_Number):
        item_values = {}
        try:
            response_dict = json.loads(response_data)
            #if 'error' in response_dict.keys():
                #item_values['status_code'] = response_dict.get('error').get('returnUserMessage')
            item_values['查询状态'] = response_dict.get('error').get('returnUserMessage')
            #elif 'data' in response_dict.keys():
            datas = response_dict.get('data','无个人信息：')
            item_values['借贷状态:'] = datas.get('message')[0]
            item_values['姓名：'] = datas.get('info').get('name')
            item_values['年龄：'] = datas.get('info').get('age')
            item_values['身份证：'] = datas.get('info').get('cardId')
            item_values['相片URL：'] = datas.get('info').get('avatar_url')
            item_values['电话号码：'] = datas.get('info').get('phone')
            try:                                                                        #尝试解析征信平台，没有则不返回
                credit = datas.get('credit_platform','无征信信息')
                if len(credit)<1:
                    print('没有征信信息！')
                else:
                    try:
                        item_values['征信平台1：'] = datas.get('credit_platform','无')[1].values()#.get('platform_name')+datas.get('credit_platform','无征信信息')[1].get('upload_time')
                        item_values['征信平台2：'] = datas.get('credit_platform','无')[2].values()#.get('platform_name')+datas.get('credit_platform','无征信信息')[2].get('upload_time')
                        item_values['征信平台3：'] = datas.get('credit_platform','无')[3].values()#.get('platform_name')+datas.get('credit_platform','无征信信息')[3].get('upload_time')
                    except:
                        item_values['传征信平台：'] = datas.get('credit_platform', '无征信信息')
            except Exception as e:
                logging.INFO(e)
                print(datas.items())

        except:
            if isinstance(Find_Number,int):
                print('请检查输入是否有误！')
                print('请重新输入！')
            item_values['个人信息'] = '无'
        print('查询号码:{}'.format(Find_Number))
        #i = {}
        for i,b in item_values.items():
            alldata = '{}{}'.format(i,b)
            print(alldata)
            #self.insert_data.insert_mysql(alldata=alldata)     #导入index_data,alldata
        #item_data = json.dumps(item_values.items())
        #self.JDBMysql.process_item(Find_Number,item_data)

    def main(self):
        pass




j = Jiedaiba_45Day()
while True:
    try:
        Find_Number= input('请输入查询参数(输入ESC退出！):')
        Find_Number = Find_Number.strip()
        if Find_Number == 'ESC':
            break
        j.get_data(Find_Number)
    except Exception as e:
        j.send_email(subject='借贷宝脚本出现异常！！！',content='Error is %s '% e)      #异常邮件提醒


