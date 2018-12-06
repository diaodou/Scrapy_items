import json
import logging

import requests
from config.mysql_demo import Mysql_Phone
from config.wuyou_headers import get_data_headers



'''
    此类功能：
        1.对无忧借条使用电话号查询用户信息
    可实现：
        1.手动输入查询
        2.短信方式提醒
        3.异步请求提升，可大规模请求
    问题：
        1.对无忧借到的查询限制数量，未做判断
'''
class Find_data:
    #phone = '17376115618'
    phone = input('请输入查询电话号码:')
    
    
    

    
    
    '''改变yxbao_13165430000，进行查询好友！'''
    def find_data_object(self):
        #insert_mysql = Mysql_Phone()
        headers = get_data_headers()        #导入config文件中的headers
        try:
            response = requests.post(url=self.url,data=self.data,headers=headers,timeout=5)
            if response.status_code == 200:
                node = response.text
                node_dict = json.loads(node)
                print(type(node_dict))
                if isinstance(node_dict,dict):
                    for i,b in node_dict.items():
                        print(i,b)
                else:
                    print('is no dict')
            else:
                print('状态码:%s'%response.status_code)
        except Exception as e:
            logging.DEBUG('error is :%s'%e)

    data = 'json={"args":["%s"],"argsclass":["java.lang.String"],"methodName":"searchFriend","proxy":"UserManager"}'% phone
    url = 'https://www.51jt.com/api.jsp'


f = Find_data()
f.find_data_object()