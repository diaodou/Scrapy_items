

import random
import re

import time

'''随机写入本地'''
def random_randint():
    next = 1
    while True:
        next+=1
        with open('d://data//1.txt','a') as f:
            n = random.randint(4**4,9**9)
            f.write('%d\n'%n)
            if next == 1000:
                break
        print('写入成功')


'''读取本地文件'''
def read_random(filename):
    # while True:
    with open(u'd://data//%s.txt'%filename,'r') as f:
        s = f.readlines()
        #print(len(s))
        for i in s:
            content = i.strip()
            print(content)
            time.sleep(0.5)
            yield content
            #time.sleep(3)
#read_random()
#random_randint()

def demo():
    a = read_random(1)
    for i in a:
        print(i)
demo()
#read_random(1)

