---
layout: post
title: Ubuntu 12.04安装JDK8 
categories: linux
tags: linux ubuntu jdk
keywords: linux,ubuntu,jdk,命令,参数
tagline: Supporting tagline
---
在Ubuntu 12.04上安装jdk8，直接写下步骤吧：

Step 1. 访问http://www.oracle.com/technetwork/java/javase/downloads/index.html按照提示下载JDK，我现在下载的版本是JDK8u20，文件名jdk-8u20-linux-i586.tar.gz。

Step 2. 进入下载文件的目录，执行命令
<pre>tar -zxf jdk-8u20-linux-i586.tar.gz</pre>
解压得到目录jdk1.8.0_20。

Setp 3. 执行命令
<pre>sudo mkdir /opt/java</pre>
在/opt目录下面建立java目录，执行命令
<pre>sudo mv jdk1.8.0_20 /opt/java/</pre>
将解压出来的文件夹移动到/opt/java文件夹下面（注：此处目录不是固定的，也可以使用/usr/local/）。

Step 4. 将如下代码加入到~/.bashrc文件中
<pre># Set jdk environment
export JAVA_HOME=/opt/java/jdk1.8.0_20
export export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar</pre>

Step 5. 执行命令
<pre>source ~/.bashrc</pre>

Step 6. 执行命令
<pre>java -version</pre>
可以得到如下jdk信息：
<pre>java version "1.8.0_20"
Java(TM) SE Runtime Environment (build 1.8.0_20-b26)
Java HotSpot(TM) Server VM (build 25.20-b23, mixed mode)</pre>

安装完成！
