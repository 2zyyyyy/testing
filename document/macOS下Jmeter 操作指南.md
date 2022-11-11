## macOS下Jmeter 操作指南
以下操作是在 macOS 下进行的，windows 除了第一步安装的环境配置不同以外其他基本相同。
### 1.安装
首先确保系统安装了 homebrew，然后我们通过 homebrew 在做一个 jmeter 的下载安装（该方法比较方便，还有其他的安装方式）。
打开终端，输入命令，随后就是等待下载完成:
```bash
$ brew install jemeter
```
![image-20221110164037428](https://tva1.sinaimg.cn/large/008vxvgGly1h804g73nboj317m0u0qcz.jpg)
如果遇到以下错误信息：
```bash
fatal: not in a git directory
Error: Command failed with exit 128: git
# 这种情况就可以使用 brew -v命令 根据提示在终端输入命令即可
```
### 2.启动 Jmeter
```
# 直接终端执行 jmeter 命令即可
$ jmeter
```
jmeter启动之后默认的语言是英文，可以通过修改`jmeter.properties`文件中的 language 调整文简体中文。

![image-20221111133944118](../../../../Library/Application Support/typora-user-images/image-20221111133955283.png)

此时我们重新打开 jmeter 之后就是中文的了。

![image-20221111134056413](https://tva1.sinaimg.cn/large/008vxvgGly1h814v07qvkj30om0dsq40.jpg)


- Jmeter 常用功能
	- 接口测试
	- 压力测试
	- 分布式压力测试
- Jmeter 特性
	- 跨平台，支持 macOS、Windows、Linux（配置 Java 环境即可）
	- 支持查看 HTML 格式的测试报告
	- 支持HTML、JSON、XML 等文本格式的数据提取，满足上下游接口关联功能
	- 多线程框架允许通过多个线程进行并发采样，并通过单独的线程组同时对不同的方法进行采样
	- 可以对测试结果进行缓存和离线分析、离线重放
- Jmeter 拓展性
	-   脚本化的采样器【BeanShell、Groovy】
	-   随意增删的采样器
	-   负载统计信息可以增删定时器
	-   数据分析和可视化插件提供了出色的扩展性和个性化
	-   jmeter自带方法可以向测试计划提供动态输入或数据处理能力
	-   通过针对Maven，Gradle和Jenkins的第三方开源库轻松进行持续集成

### 3.测试计划（test plan）

**测试计划是什么**

- 在使用 jmeter 时，创建的一系列动作
- 完整的测试计划包含了一个或多个`线程组、逻辑控制器、采样器、监听器、定时器、断言和配置元素`

**添加测试计划的元件**

![image-20221111134837676](https://tva1.sinaimg.cn/large/008vxvgGly1h8152zyycij30ee080q38.jpg)

**删除测试计划的原件**

![image-20221111134912095](https://tva1.sinaimg.cn/large/008vxvgGly1h8153ljxusj30ax09owem.jpg)

**执行测试计划**

这里有个坑，在执行测试计划之前需要先保存创建的测试计划，但有可能会保存失败，提示一下错误：

```java
java.lang.NoClassDefFoundError: Could not initialize class org.apache.jmeter.gui.util.FileDialoger
```

解决这个错误需要以下 2 步骤：

1. 选项-语言-简体中文

   ![image-20221111141304386](https://tva1.sinaimg.cn/large/008vxvgGly1h815sd3glbj30do0bkt9b.jpg)

2. 选项-外观-Nimbus

   ![image-20221111140945653](https://tva1.sinaimg.cn/large/008vxvgGly1h815p0kiy0j30fm0913z2.jpg)

   修改完成后退出重新打开，就可以正常保存测试计划了。

   