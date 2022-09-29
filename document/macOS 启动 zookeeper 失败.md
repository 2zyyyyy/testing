#### 1、问题描述

macOS 在终端启动 zookeeper。使用以下命令：

```powershell
/usr/local/Cellar/kafka/3.1.0/bin/zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties &
```

如果出现以下的错误信息：

```powershell
/usr/local/Cellar/kafka/3.1.0/libexec/bin/kafka-run-class.sh: line 342: /Users/gilbert/@@HOMEBREW_JAVA@@/bin/java: No such file or directory
```

![image-20220316112945991](https://tva1.sinaimg.cn/large/e6c9d24ely1h0bkcho2nij21t8060acy.jpg)

#### 2、原因分析

- 找到错误信息中对应的文件
- 打开文件，找到对应的第 342 行
  - ![image-20220316113234927](https://tva1.sinaimg.cn/large/e6c9d24ely1h0bkfff54cj21uc05wq51.jpg)

- 结合错误原因应该是 exec 对应的命令失败了，于是找对对应的$JAVA 变量对应的定义。

  - ![image-20220316113719661](https://tva1.sinaimg.cn/large/e6c9d24ely1h0bkkd4uevj214w06u758.jpg)

  - 看到$JAVA_HOME可以想到与其相关的环境变量相关的(图中我修改了红框中的值)
  - 终端输入`echo $JAVA_HOME`,查看对应的环境变量具体的路径
    - 执行失败可能就是这个 zookeeper-server-start 中 $JAVA_HOME 和系统环境变量中JAVA_HOME值没有对应上

####3、解决方案

上一张截图中的红框原先的值是JAVA_HOME变量（ JAVA="$JAVA_HOME/bin/java"）,为了解决这个问题可以使用系统环境变量的常量来替换这个变量（具体的值根据自己环境变量配置来修改）。

**获取系统环境变量 $JAVA_HOME**

打开终端，输入`$JAVA_HOME`，如下图所示：

![image-20220316134642600](https://tva1.sinaimg.cn/large/e6c9d24ely1h0boazfhjnj20py02sq35.jpg)

最后将这个值替换掉即可，最后就可以成功启动 zookeeper 了。

![image-20220316134808629](https://tva1.sinaimg.cn/large/e6c9d24ely1h0bocjfgmxj21s60t4wuv.jpg)