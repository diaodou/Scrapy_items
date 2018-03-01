

'''
    1.实现
        1.自动发送邮件提醒
        2.多进程(multiprocessing)




    2.参数
    70108338381532
    huitongkuaidi

'''

import os
import requests
class UrlApi:
    #CMD = input('请输入:')
    NU = input('输入单号:')
    methad ='get'

    #构建请求


    def start_requests(self):
        if self.methad == 'get':
            url = 'http://api.kuaidi100.com/api?id=94eb250be18600db&com=huitongkuaidi&nu={NU}&show=0&muti=1&order=desc'.format(NU=self.NU)
            response = requests.get(url)
        elif self.methad == 'post':
            url = 'http://api.kuaidi100.com/api?id=94eb250be18600db&com=huitongkuaidi&nu={NU}&show=0&muti=1&order=desc'.format(NU=self.NU)
            response = requests.post(url)
        return response

    #识别快递公司(可以放在附文件内)
    def descarn_company(self,company):
        if company == 'huitongkuaidi':
            companyname = '百世汇通(百世快递）'
            return companyname
        elif company == 'auspost':
            companyname = '澳大利亚邮政'
            return companyname
        elif company == 'fengxingtianxia':
            companyname = '风行天下'
            return companyname
        elif company == 'yuantong':
            companyname = '圆通速递'
            return companyname

    #解析json
    def parse_json(self,jsondata):
        if isinstance(jsondata,str)== True:
            jsondatas = eval(jsondata)
            dict_data =jsondatas['data']
            company_name = jsondatas['com']
            company = self.descarn_company(company=company_name)
            return {'dict_data':dict_data,'company':company}

    #集合函数
    def mains(self):
        result = self.start_requests()
        data = self.parse_json(jsondata=result.text)
        #print(data)
        print('您使用的快递是:%s'% data['company'])
        print('快递单号:%s'% self.NU)
        for s in data['dict_data']:
            start_data = s.get('context')
            time_data = s.get('time')+','+start_data
            print(time_data)

def main():
    u = UrlApi()
    u.mains()


if __name__ == '__main__':
    main()