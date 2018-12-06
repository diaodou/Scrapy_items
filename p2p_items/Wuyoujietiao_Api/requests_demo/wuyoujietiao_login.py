import json
import logging

import requests

'''
    此类为无忧借条的登录功能：
        1.实现无忧借条登录
'''
class Wuyoujietiao_Login:

    def login_Api(self):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)',
            'Connection': 'Keep-Alive',
            'x-phoneType': 'android',
            'x-YxbCookie': '',
            'x-version': '3.35',
            'x-osVersion': '4.4.2',
            'x-phoneModel': 'dream2lteks',
            'x-imsi': '460071012344126',
            'x-channeId': '9999',
            'x-HWUserToken': '',
            'x-imei': '354730010101230',
            'x-simNumber': '',
            'x-deviceToken': '',
            'x-androidDeviceToken': 'xvO61bqPJHOES62kG5PcKMTJWgdIag8hTxMvSL3fcBM=',
            'x-guid': '26dbdd214790a1010adf15d85e926cb9',
            'x-udid': 'ee42a0e31e418ff6637d256d8b8808db201803081818531c31be393d879d49dd49f4c7b4ae3fb2',
            'x-device': 'SM-G955N',
            'x-uniqueId': '39d1f5e87748f596d62863f189c4ca76ba3d6784c5577084',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'www.51jt.com',
            'Accept-Encoding': 'gzip',
            'Content-Length': '197',
        }

        data = 'json={"args":["13252088648","4bc11160b796c42d81595409c976b947","1"],"argsclass":["java.lang.String","java.lang.String","java.lang.String"],"methodName":"userLoginGetUserInfo","proxy":"UserManager"}'
        print(type(data))
        url = 'https://www.51jt.com/api.jsp'
        response = requests.post(url, data=data, headers=headers)
        print(response.text)
        if response.status_code == 200:
            print(response.text)
        else:
            logging.debug('')
            print(response.status_code)
            print('login error!!!')


w = Wuyoujietiao_Login()
w.login_Api()























