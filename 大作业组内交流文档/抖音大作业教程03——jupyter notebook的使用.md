# 抖音大作业教程03——jupyter notebook的使用

## 1 jupyter的安装与启动

1. 在anaconda prompt中pip list，查看已安装包。如果没有jupyter，安装。
2. 安装完成后，点击开始菜单中的jupyter notebook启动。

## 2 jupyter初步操作

1. 新建一个文件

![image-20200701144403377](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701144403377.png)

2. 选择python 3

![img](https://upload-images.jianshu.io/upload_images/3410141-a2cecb75e2550a65.png?imageMogr2/auto-orient/strip|imageView2/2/w/994/format/webp)

3. 可以进行python代码编写了

![img](https://upload-images.jianshu.io/upload_images/3410141-3b43ea7db744a979.png?imageMogr2/auto-orient/strip|imageView2/2/w/978/format/webp)

4. 每次写完一段代码后，点击上方的运行按钮，就能看见效果了。如果你的代码有问题，就会报错。

![image-20200701145546741](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701145546741.png)

## 3 import包的操作和纠错

1. 现在import一个包试一试，以numpy包为例。

![image-20200701150139720](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701150139720.png)

2. 如果你在输入这段import代码后，没有什么提示，说明import正常。

3. 如果出现了一些错误提示，说明出问题了。

4. 出现了这个问题，可能是你包安装出了问题。

   ![image-20200701150354431](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701150354431.png)

5. 进入anaconda prompt，pip uninstall <你要删除的包名>

6. 如果不能删除，进入以下目录，找到你要删除的包名，手动删，注意手动删除之前要把anaconda prompt和jupyter关掉。

```
C:\Users\<计算机用户名>\Anaconda3\Lib\site-packages
```

7. 重新进入anaconda prompt，pip list，发现此包已经不在，说明删除成功。

8. 重新安装此包。比如重新安装numpy。

pip install -i https://mirrors.aliyun.com/pypi/simple/ numpy

9. 重新进入jupyter notebook

   ``` python
   import numpy
   ```

10. 然后import librosa，发现这样的问题。

![image-20200701151435173](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701151435173.png)

11. 在网上找到了同样的问题。应该是因为报错里指出的numba模块问题。网上所说：是新版的numba模块缺少了decorators，导致依赖librosa运行的librosa无法正常运作 。

![image-20200701142350436](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701142350436.png)



12. 因此要先卸载新版numba，回到旧版。重复上面的5-7点，删除新版。
13. 然后安装旧版numba。

![image-20200701151820947](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701151820947.png)

14. pip list可以看到安装了 旧版（0.48）。

![image-20200701151914592](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701151914592.png)

15. 回到jupyter notebook，import librosa可以看到安装成功。
16. 输入help(包名称)可以获得此包的帮助文档，注意在help前要先把包import上。（上面是错误例子，下面是正确的）

![image-20200701154541216](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701154541216.png)

## 4 import常用包

![image-20200701155350653](C:\Users\ThinkPad\AppData\Roaming\Typora\typora-user-images\image-20200701155350653.png)

NumPy提供了ndarray对象，可以用py高效的存储和操作大型数组。

Pandas提供了DataFrame对象，可以高效存储和操作带标签的/列式数据。

Matplotlib提供了许多数据可视化功能。

Scikit-Learn为重要的机器学习算法提供了高效整洁的python版实现。

## 5 推荐书籍

《python数据科学手册》

![Python数据科学手册](https://file.ituring.com.cn/SmallCover/1801d23b5a67d7ae5e74)

https://jakevdp.github.io/PythonDataScienceHandbook/，这是英文版。

中文版会发在群文件里面

