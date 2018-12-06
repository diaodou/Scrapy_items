#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 19:38
# @Author  : lys
# @File    : read_xls.py
import xlrd
import xlwt
from datetime import date, datetime


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\\Users\\99329\\Desktop\\待测试数据.xls')
    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(0)  # sheet索引从0开始
    
    try:
        i = 0
        while True:
            #获取整行和整列的值（数组）
            i+=1
            rows = sheet2.row_values(i)  # 获取第四行内容
            #cols = sheet2.col_values(2)  # 获取第三列内容
            #print(rows[1])
            print(rows[2])
            print(rows[3])
            #print(cols)
            print('*' * 100)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    read_excel()
