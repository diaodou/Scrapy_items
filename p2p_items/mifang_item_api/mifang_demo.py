import requests
from bs4 import BeautifulSoup


class Mifang:

    def get_url(self,page=0):
        post_url = 'http://118.178.192.232/sift/siftRecord'
        #get_url = 'http://118.178.192.232/hotRoomRecord?pageNum=2&position=%E6%B8%A9%E5%B7%9E%E5%B8%82 '
        get_url = 'http://118.178.192.232/hotRoomRecord?pageNum=2&position=北京市  '
        headers = {
                'Host':'118.178.192.232',
                'Accept':'text/html, */*; q=0.01',
                'Proxy-Connection':'keep-alive',
                'X-Requested-With':'XMLHttpRequest',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-cn',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                #'Origin:http': 'http://118.178.192.232',
                'Content-Length': '173',
                'Connection':'keep-alive',
                'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202',
                'Referer': 'http://118.178.192.232/sift' }
        while True:
            page+=1
            data1 = {
                'pageNum':'3',
                'address':'溫州市'

            }
            data = 'isGroup=&isHot=&isDistrict=&pageNum={page}&pointWord=&address=%E6%B8%A9%E5%B7%9E&district=-1&district_id=0&minArea=0&maxArea=0&minPrice=0&maxPrice=0&minAll=0&maxAll=0&handTime=-1'.format(page=page)
            response = requests.post(url=post_url,headers=headers,data=data)
            #response = requests.get(url=get_url,headers=headers)
            if response.status_code ==200:
                #print(response.text)
                self.parse_response(response.text)

    def parse_response(self,response):

        items = BeautifulSoup(response,'lxml')
        host_name = [host_name.get_text().strip() for host_name in items.find_all('span',class_='f15 name')]
        host_price = [host_price.get_text().strip() for host_price in items.find_all('span',class_='lineFont')]
        host_location = [host_location.get_text().strip() for host_location in items.find_all('p',class_='f12 cGray address')]
        for name,price,location in zip(host_name,host_price,host_location):
            print(name,price,location)
            import time
        #time.sleep(3)

        #host_city = items.find('p',class_='')



m = Mifang()
m.get_url()
