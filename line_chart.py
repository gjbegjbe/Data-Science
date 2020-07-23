#!/usr/bin/env python
# coding: utf-8

# In[1]:


#coding:utf-8
import pandas as pd
import os
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})

dir_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/csv")
for dirs in  dir_list:    
    file_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/csv/"+dirs)
    result_likes = pd.DataFrame(columns = ['name'])
    result_followers = pd.DataFrame(columns = ['name'])
    num=0
    for file in file_list:
        with open("C:/Users/ThinkPad/Desktop/数据科学大作业/csv/"+dirs+"/{}".format(file),'r', encoding='UTF-8') as f:
            data=pd.read_csv(f)
            likes_data=data[['name','获赞总数']]
            followers_data=data[['name','粉丝数']]
            likes_data.columns=(['name','获赞总数'+str(num)])
            followers_data.columns=(['name','粉丝数'+str(num)])
            num+=1
            result_likes = pd.merge(result_likes,likes_data, how='outer', on=['name'])
            result_followers = pd.merge(result_followers,followers_data, how='outer', on=['name'])


    result_likes.set_index(["name"], inplace=True)
    result_likes=result_likes.T
    result_followers.set_index(["name"], inplace=True)
    result_followers=result_followers.T
    

    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


    from matplotlib import pyplot as plt
    get_ipython().run_line_magic('matplotlib', 'inline')
    for user in result_likes.columns:    
        plt.figure(figsize=(10, 5))
        if(dirs=='服装'):
            xList=['7.15','7.16','7.17','7.18','7.19','7.20']
        else:
            xList=['7.14','7.15','7.16','7.17','7.18','7.19','7.20']

        yList=result_likes[user]
        plt.plot(xList, yList, 'g*-')
        plt.title(user+'的获赞数')
        plt.xlabel('时间')
        plt.ylabel('获赞数')
        for x, y in zip(xList, yList):
                plt.text(x, y+0.3, str(y), ha='center', va='bottom', fontsize=10.5)
        plt.savefig(fname="C:/Users/ThinkPad/Desktop/数据科学大作业/likes_pic/"+dirs+"/"+user+".png",figsize=[10,10])
        plt.show()
    for user in result_followers.columns:    
        plt.figure(figsize=(10, 5))
        if(dirs=='服装'):
            xList=['7.15','7.16','7.17','7.18','7.19','7.20']
        else:
            xList=['7.14','7.15','7.16','7.17','7.18','7.19','7.20']

        yList=result_followers[user]
        plt.plot(xList, yList, 'b*-')
        plt.title(user+'的粉丝数')
        plt.xlabel('时间')
        plt.ylabel('粉丝数')
        for x, y in zip(xList, yList):
                plt.text(x, y+0.3, str(y), ha='center', va='bottom', fontsize=10.5)
        plt.savefig(fname="C:/Users/ThinkPad/Desktop/数据科学大作业/followers_pic/"+dirs+"/"+user+".png",figsize=[10,10])
        plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




