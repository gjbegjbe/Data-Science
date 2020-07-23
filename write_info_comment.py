#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding:utf-8 -*- 
import os
import json
import pandas as pd
import csv
import time

#文件夹所有json文件列表 
json_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/data")

for jsons in json_list:
    with open("C:/Users/ThinkPad/Desktop/数据科学大作业/data/{}".format(jsons),'r', encoding='UTF-8') as f:
        load_dict = json.load(f)
   
        s = json.dumps(load_dict,ensure_ascii=False)
        # 将 JSON 对象转换为 Python 字典
        params_json = json.loads(s)

        name=params_json["user"]["nickname"]
        city=params_json["user"]["city"]
        follower_count=params_json["user"]["follower_count"]
        total_favorited=params_json["user"]["total_favorited"]
        
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    filename="C:/Users/ThinkPad/Desktop/数据科学大作业/csv/化妆品/"+now+".csv"
        
    #newline的作用是防止每次插入都有空行 
    with open(filename, "a+", encoding='UTF-8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        #以读的方式打开csv 用csv.reader方式判断是否存在标题。
        with open(filename, "r", encoding='UTF-8',newline='') as f:
            reader = csv.reader(f)
            if not [row for row in reader]:#空文件
                #先写入每一列的标题
                writer.writerow(["name","city","粉丝数","获赞总数"])
                #再写入每一列的内容
                writer.writerows([[name,city,follower_count,total_favorited]])
            else:#非空文件
                writer.writerows([[name,city,follower_count,total_favorited]])  

