import json
import logging
import random
import urllib

import requests
import urllib3
from requests.packages import urllib3
from Xindaijia_api.Headers import  Headers
urllib3.disable_warnings()

def get_xingdaijia():
    headers = Headers()
    post_url = 'http://api.huijieapp.com/iou-site/api/loanManager/find_orders_by_tags_cities.json?ver=3.3.0'
    # data_json={"city":"","orderGrab":0,"tags":"0"}&common_json={"c_id":"pp","d_bd":"Xiaomi","d_id":"57801d27-e765-4352-95ca-ff3841497c25","d_ml":"MI PAD 2","from":"com.huijiemanager","lat":"22.69188700000000125100996228866279125213623046875","lng":"113.796640999999993937308317981660366058349609375","location":"深圳市","p":"android","sensors":{"anonymous_id":"27b5baada2121094","carrier":"","module":"","network_type":"wifi","os":"android","os_version":"5.1","product":"信贷家","screen_height":2048,"screen_width":1536,"utm_source":"pp","wifi":true},"specific_address":"深圳市宝安区福永桥和路86号","timestemp":"1520170462367","token":"fe105d912e597c0632b859071678f9cf","u_id":"3ba9b3e3f9777bb86d10104bfd7904db","ver":"3.3.0"}
    # page_json={"page_size":20,"start_row":0}
    set ='data_json=%7B%22city%22%3A%22%22%2C%22orderGrab%22%3A0%2C%22tags%22%3A%220%22%7D&common_json=%7B%22c_id%22%3A%22pp%22%2C%22d_bd%22%3A%22Xiaomi%22%2C%22d_id%22%3A%2257801d27-e765-4352-95ca-ff3841497c25%22%2C%22d_ml%22%3A%22MI+PAD+2%22%2C%22from%22%3A%22com.huijiemanager%22%2C%22lat%22%3A%2222.69188700000000125100996228866279125213623046875%22%2C%22lng%22%3A%22113.796640999999993937308317981660366058349609375%22%2C%22location%22%3A%22%E6%B7%B1%E5%9C%B3%E5%B8%82%22%2C%22p%22%3A%22android%22%2C%22sensors%22%3A%7B%22anonymous_id%22%3A%2227b5baada2121094%22%2C%22carrier%22%3A%22%22%2C%22module%22%3A%22%22%2C%22network_type%22%3A%22wifi%22%2C%22os%22%3A%22android%22%2C%22os_version%22%3A%225.1%22%2C%22product%22%3A%22%E4%BF%A1%E8%B4%B7%E5%AE%B6%22%2C%22screen_height%22%3A2048%2C%22screen_width%22%3A1536%2C%22utm_source%22%3A%22pp%22%2C%22wifi%22%3Atrue%7D%2C%22specific_address%22%3A%22%E6%B7%B1%E5%9C%B3%E5%B8%82%E5%AE%9D%E5%AE%89%E5%8C%BA%E7%A6%8F%E6%B0%B8%E6%A1%A5%E5%92%8C%E8%B7%AF86%E5%8F%B7%22%2C%22timestemp%22%3A%221520170462367%22%2C%22token%22%3A%22fe105d912e597c0632b859071678f9cf%22%2C%22u_id%22%3A%223ba9b3e3f9777bb86d10104bfd7904db%22%2C%22ver%22%3A%223.3.0%22%7D&page_json=%7B%22page_size%22%3A20%2C%22start_row%22%3A0%7D&'
    #set= 'data_json=%7B%22city%22%3A%22%22%2C%22orderGrab%22%3A0%2C%22tags%22%3A%220%22%7D&common_json=%7B%22c_id%22%3A%22pp%22%2C%22d_bd%22%3A%22Xiaomi%22%2C%22d_id%22%3A%2257801d27-e765-4352-95ca-ff3841497c25%22%2C%22d_ml%22%3A%22MI+PAD+2%22%2C%22from%22%3A%22com.huijiemanager%22%2C%22lat%22%3A%2222.69188700000000125100996228866279125213623046875%22%2C%22lng%22%3A%22113.796640999999993937308317981660366058349609375%22%2C%22location%22%3A%22%E6%B7%B1%E5%9C%B3%E5%B8%82%22%2C%22p%22%3A%22android%22%2C%22sensors%22%3A%7B%22anonymous_id%22%3A%2227b5baada2121094%22%2C%22carrier%22%3A%22%22%2C%22module%22%3A%22%22%2C%22network_type%22%3A%22wifi%22%2C%22os%22%3A%22android%22%2C%22os_version%22%3A%225.1%22%2C%22product%22%3A%22%E4%BF%A1%E8%B4%B7%E5%AE%B6%22%2C%22screen_height%22%3A2048%2C%22screen_width%22%3A1536%2C%22utm_source%22%3A%22pp%22%2C%22wifi%22%3Atrue%7D%2C%22specific_address%22%3A%22%E6%B7%B1%E5%9C%B3%E5%B8%82%E5%AE%9D%E5%AE%89%E5%8C%BA%E7%A6%8F%E6%B0%B8%E6%A1%A5%E5%92%8C%E8%B7%AF86%E5%8F%B7%22%2C%22timestemp%22%3A%221520170462367%22%2C%22token%22%3A%22fe105d912e597c0632b859071678f9cf%22%2C%22u_id%22%3A%223ba9b3e3f9777bb86d10104bfd7904db%22%2C%22ver%22%3A%223.3.0%22%7D&page_json=%7B%22page_size%22%3A20%2C%22start_row%22%3A0%7D&'
    #data = 'data_json={"city":"","orderGrab":0,"tags":"0"}&common_json={"c_id":"pp","d_bd":"Xiaomi","d_id":"57801d27-e765-4352-95ca-ff3841497c25","d_ml":"MI PAD 2","from":"com.huijiemanager","lat":"22.69188700000000125100996228866279125213623046875","lng":"113.796640999999993937308317981660366058349609375","location":"深圳市","p":"android","sensors":{"anonymous_id":"27b5baada2121094","carrier":"","module":"","network_type":"wifi","os":"android","os_version":"5.1","product":"信贷家","screen_height":2048,"screen_width":1536,"utm_source":"pp","wifi":true},"specific_address":"深圳市宝安区福永桥和路86号","timestemp":"1520170462367","token":"fe105d912e597c0632b859071678f9cf","u_id":"3ba9b3e3f9777bb86d10104bfd7904db","ver":"3.3.0"}&page_json={"page_size":20,"start_row":0}&'
    response = requests.post(post_url,headers=headers.headers(),data=set)
    response_data = json.loads(response.text)
    #item= response_data.items()
    dict_data = response_data['data']
    orders_dict = {}
    for tag in dict_data.items():
        data = [tag for tag in tag]
        for i in data:
            if type(i) == dict:
                item_orders = i['orders']
                for orders in item_orders:
                    print(type(orders))
                    print(orders.keys())

                    # try:
                    #     orders_dict['orderType'] = orders ['orderType']
                    #     orders_dict[         'locationInfo'] = orders ['locationInfo']
                    #     orders_dict[                 'city'] = orders ['city']
                    #     orders_dict[             'discount'] = orders ['discount']
                    #     orders_dict[      'curHasCollected'] = orders ['curHasCollected']
                    #     orders_dict[           'zhiMaScore'] = orders ['zhiMaScore']
                    #     orders_dict[         'zhongAnLevel'] = orders ['zhongAnLevel']
                    #     orders_dict[  'operationActivityId'] = orders ['operationActivityId']
                    #     orders_dict[             'province'] = orders ['province']
                    #     orders_dict[          'displayTags'] = orders ['displayTags']
                    #     orders_dict[          'userLogoUrl'] = orders ['userLogoUrl']
                    #     orders_dict[           'incomeInfo'] = orders ['incomeInfo']
                    #     orders_dict[           'loanStatus'] = orders ['loanStatus']
                    #     orders_dict[            'zhimaRank'] = orders ['zhimaRank']
                    #     orders_dict[          'loanPurpose'] = orders ['loanPurpose']
                    #     orders_dict[                   'id'] = orders ['id']
                    #     orders_dict[           'canCollect'] = orders ['canCollect']
                    #     orders_dict[           'curHasScan'] = orders ['curHasScan']
                    #     orders_dict[            'cycleTime'] = orders ['cycleTime']
                    #     orders_dict[       'userCreditInfo'] = orders ['userCreditInfo']
                    #     orders_dict['ManyPeopleHasCollected'] = orders ['howManyPeopleHasCollected']
                    #     orders_dict[           'assetsInfo'] = orders ['assetsInfo']
                    #     orders_dict[            'orderStar'] = orders ['orderStar']
                    #     orders_dict[ 'thirdCertifyImageUrl'] = orders ['thirdCertifyImageUrl']
                    #     orders_dict[ 'howManyPeopleHasScan'] = orders ['howManyPeopleHasScan']
                    #     orders_dict[          'loan_amount'] = orders ['loan_amount']
                    #     orders_dict[           'updateTime'] = orders ['updateTime']
                    #     orders_dict[             'userDesc'] = orders ['userDesc']
                    #     orders_dict[               'userId'] = orders ['userId']
                    #     orders_dict[             'zhiMaUrl'] = orders ['zhiMaUrl']
                    #     orders_dict[                 'tags'] = orders ['tags']
                    #     orders_dict[           'createTime'] = orders ['createTime']
                    #     orders_dict[             'district'] = orders ['district']
                    #     orders_dict[        'verifiedZhiMa'] = orders ['verifiedZhiMa']
                    #     orders_dict[       'loanStatusDesc'] = orders ['loanStatusDesc']
                    #     orders_dict[       'jobIdentityUrl'] = orders ['jobIdentiorders_dict']
                    #     print(orders_dict.items())
                    # except Exception as e:
                    #     logging.debug(e)

get_xingdaijia()





    # if 'data' in response_data:
    #     print(item.get('data'))
        # item_data = item.get('data').get('detail').get('orders')
        # for ordirs in item_data:
        #     print(ordirs)
        #     print(type(ordirs))
        #     print(ordirs.keys())





get_xingdaijia()
#ok



def urllib_posr():


    post_url = 'http://api.huijieapp.com/iou-site/api/loanManager/find_orders_by_tags_cities.json?ver=3.3.0{}'

    # data_json={"city":"","orderGrab":0,"tags":"0"}&common_json={"c_id":"pp","d_bd":"Xiaomi","d_id":"57801d27-e765-4352-95ca-ff3841497c25","d_ml":"MI PAD 2","from":"com.huijiemanager","lat":"22.69188700000000125100996228866279125213623046875","lng":"113.796640999999993937308317981660366058349609375","location":"深圳市","p":"android","sensors":{"anonymous_id":"27b5baada2121094","carrier":"","module":"","network_type":"wifi","os":"android","os_version":"5.1","product":"信贷家","screen_height":2048,"screen_width":1536,"utm_source":"pp","wifi":true},"specific_address":"深圳市宝安区福永桥和路86号","timestemp":"1520170462367","token":"fe105d912e597c0632b859071678f9cf","u_id":"3ba9b3e3f9777bb86d10104bfd7904db","ver":"3.3.0"}
    # page_json={"page_size":20,"start_row":0}
    data = 'data_json=%7B%22city%22%3A%22%22%2C%22orderGrab%22%3A0%2C%22tags%22%3A%220%22%7D&common_json=%7B%22c_id%22%3A%22pp%22%2C%22d_bd%22%3A%22Xiaomi%22%2C%22d_id%22%3A%2257801d27-e765-4352-95ca-ff3841497c25%22%2C%22d_ml%22%3A%22MI+PAD+2%22%2C%22from%22%3A%22com.huijiemanager%22%2C%22lat%22%3A%2222.69188700000000125100996228866279125213623046875%22%2C%22lng%22%3A%22113.796640999999993937308317981660366058349609375%22%2C%22location%22%3A%22%E6%B7%B1%E5%9C%B3%E5%B8%82%22%2C%22p%22%3A%22android%22%2C%22sensors%22%3A%7B%22anonymous_id%22%3A%2227b5baada2121094%22%2C%22carrier%22%3A%22%22%2C%22module%22%3A%22%22%2C%22network_type%22%3A%22wifi%22%2C%22os%22%3A%22android%22%2C%22os_version%22%3A%225.1%22%2C%22product%22%3A%22%E4%BF%A1%E8%B4%B7%E5%AE%B6%22%2C%22screen_height%22%3A2048%2C%22screen_width%22%3A1536%2C%22utm_source%22%3A%22pp%22%2C%22wifi%22%3Atrue%7D%2C%22specific_address%22%3A%22%E6%B7%B1%E5%9C%B3%E5%B8%82%E5%AE%9D%E5%AE%89%E5%8C%BA%E7%A6%8F%E6%B0%B8%E6%A1%A5%E5%92%8C%E8%B7%AF86%E5%8F%B7%22%2C%22timestemp%22%3A%221520170462367%22%2C%22token%22%3A%22fe105d912e597c0632b859071678f9cf%22%2C%22u_id%22%3A%223ba9b3e3f9777bb86d10104bfd7904db%22%2C%22ver%22%3A%223.3.0%22%7D&page_json=%7B%22page_size%22%3A20%2C%22start_row%22%3A0%7D&'

    # url = post_url
    # http= urllib3.PoolManager()
    # r = http.request('POST',url,headers=headers)
    print(post_url.format(data))
    #d = json.loads(r.data.decode('utf-8'))


#urllib_posr()


def requests_post():
    post_url = 'http://api.huijieapp.com/iou-site/api/loanManager/find_orders_by_tags_cities.json?ver=3.3.0{}'
    data = {
        'data_json':'{"city":"","orderGrab":0,"tags":"0"}',
        'common_json':'{"c_id":"pp","d_bd":"Xiaomi","d_id":"57801d27-e765-4352-95ca-ff3841497c25","d_ml":"MI PAD 2","from":"com.huijiemanager","lat":"22.69188700000000125100996228866279125213623046875","lng":"113.796640999999993937308317981660366058349609375","location":"深圳市","p":"android","sensors":{"anonymous_id":"27b5baada2121094","carrier":"","module":"","network_type":"wifi","os":"android","os_version":"5.1","product":"信贷家","screen_height":2048,"screen_width":1536,"utm_source":"pp","wifi":true},"specific_address":"深圳市宝安区福永桥和路86号","timestemp":"1520170462367","token":"fe105d912e597c0632b859071678f9cf","u_id":"3ba9b3e3f9777bb86d10104bfd7904db","ver":"3.3.0"}'
        ,'page_json':'{"page_size":20,"start_row":0}'
    }
    response= requests.post(post_url,data,headers=headers)
    print(response.status_code)
