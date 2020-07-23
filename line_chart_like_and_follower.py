#!/usr/bin/env python
# coding: utf-8

# In[30]:


#coding:utf-8
import pandas as pd
import os
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})

get_ipython().run_line_magic('matplotlib', 'inline')

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



    for user in result_likes.columns:        
        fig,ax1 = plt.subplots()
        ax2 = ax1.twinx()

        if(dirs=='服装'):
            xList=['7.15','7.16','7.17','7.18','7.19','7.20']
        else:
            xList=['7.14','7.15','7.16','7.17','7.18','7.19','7.20']

        yList=result_likes[user]
        yList1=result_followers[user]

        ax1.plot(xList, yList, 'g*-')
        ax2.plot(xList, yList1, 'r*-')
        plt.title(user+'的获赞数与粉丝数')
        ax1.set_xlabel('时间')
        ax1.set_ylabel('获赞数',color = 'g')
        ax2.set_ylabel('粉丝数',color = 'r')
        for x, y in zip(xList, yList):
                ax1.text(x, y+0.3, str(y), ha='center', va='bottom', fontsize=10.5)
        for x, y in zip(xList, yList1):
                ax2.text(x, y+0.3, str(y), ha='center', va='top', fontsize=10.5)
        leg=ax1.legend(['获赞数'])
        leg1=ax2.legend(['粉丝数'],loc='lower right')
        plt.savefig(fname="C:/Users/ThinkPad/Desktop/数据科学大作业/likes_and_followers_pic/"+dirs+"/"+user+".png",figsize=[10,10])


# In[ ]:





# In[ ]:




