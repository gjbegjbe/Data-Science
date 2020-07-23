#!/usr/bin/env python
# coding: utf-8

# In[19]:


# -*- coding:utf-8 -*- 
import os
import json
import pandas as pd
import csv
import time

user_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/comment_data/化妆品")

for user in user_list:
    json_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/comment_data/化妆品/"+user)
    
    for jsons in json_list:        
        with open("C:/Users/ThinkPad/Desktop/数据科学大作业/comment_data/化妆品/{}/{}".format(user,jsons),'r', encoding='UTF-8') as f:
                load_dict = json.load(f)
                json1=jsons[:-5]
                namelist=json1.split()
                s = json.dumps(load_dict,ensure_ascii=False)
                # 将 JSON 对象转换为 Python 字典
                params_json = json.loads(s)
                for item in params_json['comments']:
                    filename="C:/Users/ThinkPad/Desktop/数据科学大作业/comment_csv/化妆品/"+user+".csv"        
                    #newline的作用是防止每次插入都有空行 
                    with open(filename, "a+", encoding='UTF-8',newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        #以读的方式打开csv 用csv.reader方式判断是否存在标题。
                        with open(filename, "r", encoding='UTF-8',newline='') as f:
                            reader = csv.reader(f)
                            if not [row for row in reader]:#空文件
                                #先写入每一列的标题
                                writer.writerow(["用户名","视频编号","点赞数","评论数","评论"])
                                #再写入每一列的内容
                                writer.writerows([[user,namelist[0],namelist[1],namelist[2],item['text']]])
                            else:#非空文件
                                writer.writerows([[user,namelist[0],namelist[1],namelist[2],item['text']]]) 


# In[ ]:




