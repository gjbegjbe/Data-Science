#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#coding:utf-8

import os
import matplotlib.pyplot as plt
import librosa
import librosa.display
import sklearn
import numpy as np
import csv
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
            x, sr = librosa.load(f)
            
            #过零
            n0 = 1000
            n1 = 9100
            plt.figure(figsize=(14, 5))
            plt.plot(x[n0:n1])
            plt.title(user+'-'+wav)
            plt.grid()
            plt.title(user+'-'+wav)
            plt.savefig(fname="C:/Users/ThinkPad/Desktop/数据科学大作业/librosa_zero_crossings_without_voice_pic/"+dirs+"/"+user+'-'+wav+".png",figsize=[10,10])
            plt.show()

            zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False)

            #频率分贝
            X = librosa.stft(x)
            Xdb = librosa.amplitude_to_db(abs(X))   # 把幅度转成分贝格式
            plt.figure(figsize=(14, 5))
            librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
            plt.colorbar()
            plt.title(user+'-'+wav)
            plt.savefig(fname="C:/Users/ThinkPad/Desktop/数据科学大作业/librosa_amplitude_to_db_without_voice_pic/"+dirs+"/"+user+'-'+wav+".png",figsize=[10,10])
            plt.show()

            #频谱中心
            spectral_centroids = librosa.feature.spectral_centroid(x[:80000], sr=sr)[0]
            # Computing the time variable for visualization
            frames = range(len(spectral_centroids))
            t = librosa.frames_to_time(frames, sr=8000)
            # Normalising the spectral centroid for visualisation
            def normalize(x, axis=0):
                return sklearn.preprocessing.minmax_scale(x, axis=axis)
            #Plotting the Spectral Centroid along the waveform
            librosa.display.waveplot(x[:80000], sr=sr, alpha=0.4)
            plt.plot(t, normalize(spectral_centroids), color='r')
            plt.title(user+'-'+wav)
            plt.savefig(fname="C:/Users/ThinkPad/Desktop/数据科学大作业/librosa_spectral_centroids_without_voice_pic/"+dirs+"/"+user+'-'+wav+".png",figsize=[10,10])
            plt.show()

            #谱滚降
            spectral_rolloff = librosa.feature.spectral_rolloff(x[:80000], sr=sr)[0]
            librosa.display.waveplot(x[:80000], sr=sr, alpha=0.4)
            plt.plot(t, normalize(spectral_rolloff), color='r')
            plt.title(user+'-'+wav)
            plt.savefig(fname="C:/Users/ThinkPad/Desktop/数据科学大作业/librosa_spectral_rolloff_without_voice_pic/"+dirs+"/"+user+'-'+wav+".png",figsize=[10,10])
            plt.show()

            chroma_stft=librosa.feature.chroma_stft(y=x,sr=sr)
            spectral_cent=librosa.feature.spectral_centroid(y=x,sr=sr)
            spectral_bw=librosa.feature.spectral_bandwidth(y=x,sr=sr)
            rolloff=librosa.feature.spectral_rolloff(y=x,sr=sr)
            zcr=librosa.feature.zero_crossing_rate(x)
            mfcc=librosa.feature.mfcc(y=x,sr=sr)
            print(sum(zero_crossings),np.mean(chroma_stft),np.mean(spectral_cent),np.mean(spectral_bw),np.mean(rolloff),np.mean(zcr),np.mean(mfcc))

            filename="C:/Users/ThinkPad/Desktop/数据科学大作业/feature_csv/"+dirs+"/"+user+".csv"        
                    #newline的作用是防止每次插入都有空行 
            with open(filename, "a+", encoding='UTF-8',newline='') as csvfile:
                writer = csv.writer(csvfile)
                #以读的方式打开csv 用csv.reader方式判断是否存在标题。
                with open(filename, "r", encoding='UTF-8',newline='') as f:
                            reader = csv.reader(f)
                            if not [row for row in reader]:#空文件
                                #先写入每一列的标题
                                writer.writerow(["视频","过零点数量","色度频率","谱质心","谱宽度","谱滚降","过零率","梅尔频率倒谱系数"])
                                #再写入每一列的内容
                                writer.writerows([[wav,sum(zero_crossings),np.mean(chroma_stft),np.mean(spectral_cent),np.mean(spectral_bw),np.mean(rolloff),np.mean(zcr),np.mean(mfcc)]])
                            else:#非空文件
                                writer.writerows([[wav,sum(zero_crossings),np.mean(chroma_stft),np.mean(spectral_cent),np.mean(spectral_bw),np.mean(rolloff),np.mean(zcr),np.mean(mfcc)]])


# In[ ]:




