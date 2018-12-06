#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 10:57
# @Author  : lys
# @File    : ome.py
import re
import time,json

import  requests
import  random
def open_file():
    with open('C:\\Users\\99329\\Desktop\\4.txt', 'r') as f:
        origin = f.readlines()
        return origin

def send_url(img):
    data={'channel':'abc','picturl':img}
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    response =requests.post(url='http://api.qhweidai.com/api/topicture',data=data,headers=headers)
    return response.text


def parse_response():
    for i in open_file():
        print(i.strip())
        r = send_url(i.strip())
        jr = json.loads(r)
        print(jr)
        for s in jr.items():
            for j in s:
                print(j)
            time.sleep(2)

def save_file(url):
    with open('C:\\Users\\99329\\Desktop\\save_10.txt', 'a') as f:
        f.write(url + '\n')
        print('成功写入！')


def open_files():
    with open('C:\\Users\\99329\\Desktop\\parse_json.txt', 'r') as f:
        origin = f.readlines()
        return origin

parse_response()










