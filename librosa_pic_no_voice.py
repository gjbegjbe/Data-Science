#!/usr/bin/env python
# coding: utf-8

# In[2]:


#coding:utf-8

import os
import matplotlib.pyplot as plt
import librosa
import librosa.display
get_ipython().run_line_magic('matplotlib', 'inline')

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

dir_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/wav_without_voice")
for dirs in  dir_list: 
    user_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/wav_without_voice/"+dirs)
    for user in user_list:
        wav_list=os.listdir("C:/Users/ThinkPad/Desktop/数据科学大作业/wav_without_voice/"+dirs+"/"+user)
        for wav in wav_list:
            f="C:/Users/ThinkPad/Desktop/数据科学大作业/wav_without_voice/"+dirs+"/"+user+"/"+wav+"/accompaniment.wav"
            y, sr = librosa.load(f, sr=None)
            plt.figure()
            librosa.display.waveplot(y,sr)
            plt.title(user+'-'+wav)
            plt.savefig(fname="C:/Users/ThinkPad/Desktop/数据科学大作业/librosa_waveplot_without_voice_pic/"+dirs+"/"+user+'-'+wav+".png",figsize=[10,10])
            plt.show()


# In[ ]:




