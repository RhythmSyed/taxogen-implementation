# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 17:00:07 2018

@author: gaoha
"""


import re
import jieba
from langconv import *


# 将繁体转换成简体
def tradition2simple(line):
    line = Converter('zh-hans').convert(line)
    return line


 # 中文的编码范围是：\u4e00到\u9fa5
def translate(str):
    p2 = re.compile(u'[^\u4e00-\u9fa5]')  
    zh = " ".join(p2.split(str)).strip()
    zh = " ".join(zh.split())
    return zh


with open('raw_papers.txt') as f:
    with open("papers.txt", "w") as f2:
        for line in f:
            line_cut = jieba.cut(line, cut_all=False)
            outStr = translate(" ".join(line_cut))
            Simple_Str = tradition2simple(outStr)
            if(Simple_Str != "" and Simple_Str != "更 多" and Simple_Str != None):
                f2.writelines(Simple_Str+"\n")
                