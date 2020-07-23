#!/usr/bin/env python
# coding: utf-8

# In[16]:


#coding:utf-8

import os
import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def extract_features_song(f):
    y, sr = librosa.load(f)
    mfccs=librosa.feature.mfcc(y)
    mfccs/=np.amax(np.absolute(mfccs))
    if(f.find("服装")!=-1):
        return np.ndarray.flatten(mfccs)[:5000]
    if(f.find("食物")!=-1):
        return np.ndarray.flatten(mfccs)[:5000]
    return np.ndarray.flatten(mfccs)[:16000]

def generate_features_and_labels():
    
    item_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/wav_without_voice")
    
    for item in item_list:
        all_features=[]
        all_labels=[]

        user_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/wav_without_voice/"+item)

        for user in user_list:
            user_features=[]
            wavdir_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/wav_without_voice/"+item+"/"+user)
            wav_list=[]
            for wavdir in wavdir_list:
                wav_list.append("C:/Users/ThinkPad/Desktop/数据科学大作业/wav_without_voice/"+item+"/"+user+"/"+wavdir+"/accompaniment.wav")
            print("Processing %d wavs in %s user..."%(len(wav_list),user))

            for wav in wav_list:
                features=extract_features_song(wav)
                user_features.append(features)

            user_features_ave=np.array(user_features).mean(axis=0)
            plt.title(user)
            plt.plot(user_features_ave)
            plt.savefig(fname="C:/Users/ThinkPad/Desktop/数据科学大作业/librosa_mfcc_average_pic/"+item+"/"+user+".png",figsize=[10,10])
            plt.show()
            all_features.append(user_features_ave)

        all_features_ave=np.array(all_features).mean(axis=0)
        plt.title(item)
        plt.plot(all_features_ave)
        plt.savefig(fname="C:/Users/ThinkPad/Desktop/数据科学大作业/librosa_mfcc_average_pic/"+item+"/average"+item+".png",figsize=[10,10])
        plt.show()    
    
generate_features_and_labels()


# In[ ]:





# In[ ]:




