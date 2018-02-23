

import hashlib
import json

import urllib.parse
import urllib.request

import requests
import base64



APP_id = '1266271'
APP_key = '7526a46e-3a2a-4f5b-8659-d72f361e3386'

'''datasign:把(请求内容（未编码）+appkey)进行MD5加密，然后Base64编码'''
def parse_datasign(origin_data,appkey):
    m = hashlib.md5()
    m.update((origin_data+appkey).encode('utf8'))
    encodestr = m.hexdigest()
    base64_text = base64.b64encode(encodestr.encode(encoding='utf-8'))
    return base64_text

'''对url发送带表单的post请求'''
def requests_post(url,datas):
    header = {
        "Accept": "application/x-www-form-urlencoded;charset=utf-8",
        "Accept-Encoding": "utf-8"
    }
    # postdata = urllib.parse.urlencode(datas).encode('utf-8')
    # req = urllib.request.Request(url, postdata, header)
    # get_data = (urllib.request.urlopen(req).read().decode('utf-8'))

    get_data = requests.post(url,data=datas,headers=header).text
    return get_data




'''获取快递单号的快递公司代码和名称'''
def get_company(logistic_code,appid,appkey,url):
    data1 = {'LogisticCode':logistic_code}
    d1 = json.dumps(data1,sort_keys=True)
    requestsdata = parse_datasign(d1,appkey)
    post_data = {
        'RequestData':d1,
        'EBusinessID':appid,
        'RequestType':'2002',
        'DataType':'2',
        'DataSign':requestsdata.decode()
    }
    print('get_company')
    json_data = requests_post(url,post_data)
    sort_data = json.loads(json_data)
    return sort_data

'''查询接口，支持按照运单号查询（单个查询）'''
def get_traces(logistic_code,shipper_code,appid,appkey,url):
    data1 ={'LogisticCode':logistic_code,'ShipperCode':shipper_code}
    d1 = json.dumps(data1,sort_keys=True)
    requestdata = parse_datasign(d1,appkey)
    post_data = {'RequestData':d1,
                 'EBusinessID':appid,
                 'RequestType':'1002',
                 'DataType':'2',
                 'DataSign': requestdata.decode()
                 }
    print('get_traces')
    json_data = requests_post(url,post_data)
    sort_data = json.loads(json_data)
    return sort_data

'''输出数据'''
def recognise(expresscode):
    url = 'http://api.kdniao.cc/Ebusiness/EbusinessOrderHandle.aspx'
    data = get_company(expresscode,APP_id,APP_key,url)      #查询到的快递公司

    if not any(data['Shippers']):
        print('未查到信息，请检查快递单号是否有误！')
    else:
        print('已经查到',str(data['Shippers'][0]['ShipperName'])+"("+str(data['Shippers'][0]['ShipperCode'])+")",expresscode)
            #expresscode：用户输入的单号
        trace_data = get_traces(expresscode,data['Shippers'][0]['ShipperCode'],APP_id,APP_key,url)
        '''                         查看一下这块的data['shipper'][0]['shippercode']是怎么用的'''
        print(trace_data.items())
        if trace_data['Success'] == 'false' or not any(trace_data['Traces']):
            print('未查询到该快递的物流轨迹')
        else:
            str_state = '问题件'
            if trace_data['State'] == '2':
                str_state = '在途中'
            elif trace_data['State'] == '3':
                str_state ='已签收'
            print('目前的状态:'+ str_state)
            trace_data = trace_data['Traces']
            item_no = 1
            for item in trace_data:
                print(str(item_no)+':',item['AcceptTime'],item['AcceptTime'],item['AcceptStation'])
                item_no +=1
            print('\n')
    return

#while True:
    # code = input('请输入快递单号(esc:退出)')
    # code = code.strip()
    # if code == 'esc':
    #     break
recognise('888159158224563512')



