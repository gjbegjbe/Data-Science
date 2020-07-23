# 抖音02——anaconda安装和pip包安装（以librosa为例）

## 1 anaconda 安装

1. 官网下载https://www.continuum.io
2. 进入安装程序，到显示下图时。如图，如果系统只有一个用户选择默认的第一个即可，如果有多个用户而且都要用到 Anaconda ，则选择第二个选项。

![img](https://img-blog.csdnimg.cn/20181112220714826.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI4MDEzNzUx,size_16,color_FFFFFF,t_70)

3. 两个默认就好，第一个是加入环境变量，第二个是默认使用 Python 3.5。

![img](https://img-blog.csdnimg.cn/20181112220829822.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI4MDEzNzUx,size_16,color_FFFFFF,t_70)

4. 安装需要一段时间，等待安装完成即可。需要占用空间大约 1.8 G左右。

## 2 pip代理配置

1. 完成安装后，如果你是在windows上操作，按下面图打开 Anaconda Prompt，就是类似windows的命令窗口这个。

![img](https://pic1.zhimg.com/80/v2-277eb51b454066e3571800815719ea7c_1440w.jpg)

2. 先添加国内镜像源，推荐阿里云，快速：https://mirrors.aliyun.com/pypi/simple/

``` 
conda config --add channels https://mirrors.aliyun.com/pypi/simple/
```

3. 查看添加的镜像： 

``` 
conda config --get channels
```

![image-20200701002321560](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701002321560.png)

4. 设置可以使用pip访问包管理，执行如下命令：

``` 
conda config --set use_pip True
```

5. 修改anaconde的配置文件.condarc，一般在如下目录：

   C:\Users\\\<你的计算机用户名>\\\.condarc

6. 将如下内容写入.condarc文件，直接在下面加，上面的不能去掉

   其中这里的ip地址是cmd用ipconfig获取的地址，上一个文件已经说明，我是192.168.1.2

``` js proxy_servers:
  https: https://192.168.1.2:1808
  http: http://192.168.1.2:1808
```

7. 如果未进行以上操作就会报以下错误

![image-20200630225321656](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200630225321656.png)

## 3 pip安装librosa包

1. 首先要保证你的电脑fidder是关闭的，否则就会出现下图黄色字的错误

![image-20200630233749722](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200630233749722.png)

2. 然后输入以下命令回车：

``` 
pip install -i https://mirrors.aliyun.com/pypi/simple/ librosa
```

3. 如果报以下错误：

![image-20200701003134698](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701003134698.png)

4. 安装时候忽略掉这个已安装的包就好

```
pip install -i https://mirrors.aliyun.com/pypi/simple/ librosa  --ignore-installed llvmlite
```

5. 安装中：

![image-20200701003305223](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701003305223.png)

6. 安装完成，输入以下命令就能在列表看见你新安装的包了

```
pip list
```

![image-20200701003432204](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701003432204.png)

7. 之后的jupyter中会用到它