## macOS下Jmeter 操作指南
以下操作是在 macOS 下进行的，windows 除了第一步安装的环境配置不同以外其他基本相同。
### 1.安装
首先确保系统安装了 homebrew，然后我们通过 homebrew 在做一个 jmeter 的下载安装（该方法比较方便，还有其他的安装方式）。
打开终端，输入命令，随后就是等待下载完成:
```bash
$ brew install jemeter
```
![image-20221110164037428](https://tva1.sinaimg.cn/large/008vxvgGly1h804g73nboj317m0u0qcz.jpg)
如果遇到一下错误信息：
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