#!/usr/bin/env python
# coding: utf-8

# In[4]:


#coding:utf-8

import os
import numpy as np
import csv
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


dir_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/feature_csv")
for dirs in  dir_list: 
    user_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/feature_csv/"+dirs)
    for user in user_list:
           
            filename="C:/Users/ThinkPad/Desktop/数据科学大作业/feature_csv/"+dirs+"/"+user        
                    #newline的作用是防止每次插入都有空行 
            mean=pd.Series()
            with open(filename,'r', encoding='UTF-8') as f:
                data=pd.read_csv(f)
                mean=data.mean()
            with open(filename, "a+", encoding='UTF-8',newline='') as csvfile:
                
                writer = csv.writer(csvfile)
                #以读的方式打开csv 用csv.reader方式判断是否存在标题。
                with open(filename, "r", encoding='UTF-8',newline='') as f:
                            reader = csv.reader(f)
                            if not [row for row in reader]:#空文件
                                #先写入每一列的标题
                                writer.writerow(["视频","过零点数量","色度频率","谱质心","谱宽度","谱滚降","过零率","梅尔频率倒谱系数"])
                                #再写入每一列的内容
                                writer.writerows([['平均值',mean[0],mean[1],mean[2],mean[3],mean[4],mean[5],mean[6]]])
                            else:#非空文件
                                writer.writerows([['平均值',mean[0],mean[1],mean[2],mean[3],mean[4],mean[5],mean[6]]])

