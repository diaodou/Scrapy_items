


import requests

'''
    {
    'OrderCode':'',	
    'ShipperCode':'',	
    'LogisticCode':''
    }                   #需要经过转码后填入：RequestData


'''

def start_request():
    url = 'http://sandboxapi.kdniao.cc:8080/kdniaosandbox/gateway/exterfaceInvoke.json'
    data ={
        'RequestData':'',
        'EBusinessID':'efed4dd2-9846-4a71-8da6-41a0dfd30121',       #自己的秘钥
        'RequestType':'1002',
        'DataSign':'',
        'DataType':'2',
    }
