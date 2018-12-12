# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 21:39:27 2018

@author: gaoha
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

import jieba.posseg as pseg

from collections import Counter

paper_list = []

with open('papers.txt') as f:
    for line in f:
        paper_list.append(line)
        
print(len(paper_list))



# =============================================================================
# tfidf = TfidfVectorizer()
# weight = tfidf.fit_transform(paper_list).toarray()
# word = tfidf.get_feature_names()
# 
# 
# # 打印每个文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一个文本下的词语权重
# for i in range(len(weight)): 
#     print ("-------这里输出第", i, "个文本的词语tf-idf权重------")
#     for j in range(len(word)):
#         if(weight[i][j]>0):
#             #第i个文本中，第j个词的tfidf值
#             print(word[j], weight[i][j]) 
# =============================================================================
            


# token_pattern指定统计词频的模式, 不指定, 默认如英文, 不统计单字
vectorizer = CountVectorizer(token_pattern='\\b\\w+\\b')
# norm=None对词频结果不归一化
# use_idf=False, 因为使用的是计算tfidf的函数, 所以要忽略idf的计算
transformer = TfidfTransformer(norm=None, use_idf=False)
tf = transformer.fit_transform(vectorizer.fit_transform(paper_list))
word = vectorizer.get_feature_names()
weight = tf.toarray()

print(len(word))
print(len(weight))
print(len(weight[0]))


word_dict = {}
for i in range(len(word)) :
    words = pseg.cut(word[i])
    for wor,flag in words:
        if(flag=="ns"):
            #print("%s  %s"%(wor, flag))
            sum = 0
            for j in range(len(weight)):
                sum += weight[j][i]
            word_dict[word[i]] = sum
            #print(i,sum)
            break
    
print(len(word_dict))

word_dict_sort = sorted(word_dict.items(),key = lambda x:x[1],reverse = True)

print(word_dict_sort)

with open("key_words.txt", "w") as f:
    for i in range(len(word_dict_sort)) :
        f.writelines(word_dict_sort[i][0]+ "\t" + str(word_dict_sort[i][1]) +"\n")