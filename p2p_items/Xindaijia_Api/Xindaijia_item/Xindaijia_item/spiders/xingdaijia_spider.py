# -*- coding: utf-8 -*-
import json

from scrapy import Request,Spider,FormRequest
from Xindaijia_item.server.server_demo import http_method_example
class XingdaijiaSpiderSpider(Spider):
    name = 'xingdaijia_spider'
    #allowed_domains = ['www.xingdaijia.com']
    #start_urls = ['http://www.xingdaijia.com/']
    Xindaijia_all_data = {}
    def start_requests(self):
        post_url = 'http://api.huijieapp.com/iou-site/api/loanManager/find_orders_by_tags_cities.json?ver=3.3.0'
        set = 'data_json=%7B%22city%22%3A%22%22%2C%22orderGrab%22%3A0%2C%22tags%22%3A%220%22%7D&common_json=%7B%22c_id%22%3A%22pp%22%2C%22d_bd%22%3A%22Xiaomi%22%2C%22d_id%22%3A%2257801d27-e765-4352-95ca-ff3841497c25%22%2C%22d_ml%22%3A%22MI+PAD+2%22%2C%22from%22%3A%22com.huijiemanager%22%2C%22lat%22%3A%2222.69188700000000125100996228866279125213623046875%22%2C%22lng%22%3A%22113.796640999999993937308317981660366058349609375%22%2C%22location%22%3A%22%E6%B7%B1%E5%9C%B3%E5%B8%82%22%2C%22p%22%3A%22android%22%2C%22sensors%22%3A%7B%22anonymous_id%22%3A%2227b5baada2121094%22%2C%22carrier%22%3A%22%22%2C%22module%22%3A%22%22%2C%22network_type%22%3A%22wifi%22%2C%22os%22%3A%22android%22%2C%22os_version%22%3A%225.1%22%2C%22product%22%3A%22%E4%BF%A1%E8%B4%B7%E5%AE%B6%22%2C%22screen_height%22%3A2048%2C%22screen_width%22%3A1536%2C%22utm_source%22%3A%22pp%22%2C%22wifi%22%3Atrue%7D%2C%22specific_address%22%3A%22%E6%B7%B1%E5%9C%B3%E5%B8%82%E5%AE%9D%E5%AE%89%E5%8C%BA%E7%A6%8F%E6%B0%B8%E6%A1%A5%E5%92%8C%E8%B7%AF86%E5%8F%B7%22%2C%22timestemp%22%3A%221520170462367%22%2C%22token%22%3A%22fe105d912e597c0632b859071678f9cf%22%2C%22u_id%22%3A%223ba9b3e3f9777bb86d10104bfd7904db%22%2C%22ver%22%3A%223.3.0%22%7D&page_json=%7B%22page_size%22%3A20%2C%22start_row%22%3A0%7D&'
        yield FormRequest.from_response(url=post_url,formdata= set,callback=self.parse)
    def parse(self, response):
        if response.status == 200:
            response_data = json.loads(response.text)
            dict_data = response_data['data']
            for tag in dict_data.items():
                data = [tag for tag in tag]
                for i in data:
                    if type(i) == dict:
                        item_orders = i['orders']
                        for orders in item_orders:
                            print(type(orders))
                            print(orders.keys())
                            print(orders)
                            self.Xindaijia_all_data['items'] = orders
                for i in self.Xindaijia_all_data:
                    http_method_example(i)
                
