#!/usr/bin/env python
# coding: utf-8

# In[1]:


import jieba


# In[4]:


words=jieba.lcut('说完jieba库，我们要开始统计词频了，如何统计？步骤和统计英文相似，不过有了jieba的加持，这变得更为简单：')


# In[5]:


words


# In[70]:


# -*- coding:utf-8 -*- 
import jieba
import csv
import os
import pandas as pd
import re

def comp(x):
    return x[1]

dir_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/comment_csv")
for dirs in dir_list:
    user_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/comment_csv/"+dirs)
    for user in user_list:    
        with open("C:/Users/ThinkPad/Desktop/数据科学大作业/comment_csv/"+dirs+"/"+user,'r', encoding='UTF-8') as f:
            print(user)
            data=pd.read_csv(f)
            string=""

            if(dirs=='服装'):
                for index, row in data.iterrows():
                    string=string+str(row['01'])+'.'+str(row['02'])+'.'+str(row['03'])+'.'+str(row['04'])+'.'+str(row['05'])+'.'+str(row['06'])+'.'+str(row['07'])+'.'+str(row['08'])+'.'+str(row['09'])+'.'+str(row['10'])+'.'
            elif(dirs=='食物'):
                for index, row in data.iterrows():
                    string=string+str(row['评论'])
            else:
                for index, row in data.iterrows():
                    string=string+str(row['评论'] )          


            string = re.sub(u"\[.*?]", "", string)
            string = string.replace("..","")
            words=jieba.lcut(string)
            counts={}
            for x in words:                   
                if len(x)==1:
                    continue
                else:
                    counts[x]=counts.get(x,0)+1
            items=list(counts.items())
            items.sort(key=comp,reverse=True)


            for i in range(len(items)):
                key,value = items[i]
                print("{0} {1}".format(key,value))
                filename="C:/Users/ThinkPad/Desktop/数据科学大作业/comment_csv_frequency/"+dirs+"/"+user       
                #newline的作用是防止每次插入都有空行 
                with open(filename, "a+", encoding='UTF-8',newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        #以读的方式打开csv 用csv.reader方式判断是否存在标题。
                        with open(filename, "r", encoding='UTF-8',newline='') as f:
                            reader = csv.reader(f)
                            if not [row for row in reader]:#空文件
                                #先写入每一列的标题
                                writer.writerow(["词语","出现次数"])
                                #再写入每一列的内容
                                writer.writerows([[key,value]])
                            else:#非空文件
                                writer.writerows([[key,value]]) 


                


# In[64]:





# In[ ]:




