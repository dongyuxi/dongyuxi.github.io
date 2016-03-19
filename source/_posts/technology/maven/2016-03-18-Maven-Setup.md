---
layout: post
title: Maven笔记之一：简介和安装(Mac和Windows)
categories: 技术
tags: [maven,java]
keywords: maven,java
date: 2016-03-18
permalink: Maven-Setup
---
### Maven简介 ###
[Maven](https://maven.apache.org)基于项目对象模型(POM)java项目管理和构建自动化工具，默认的配置有极高的复用性，避免了jar包的拷贝和重复。
<!--more-->

#### Maven安装 ###
#### Mac版本 ####
强烈推荐使用homebrew安装，命令如下：
```
	brew install maven
```
如果还没有安装homebrew，请使用如下命令安装：
```
	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

如果真的想要通过安装包安装的话，请到[Maven Download 页面](https://maven.apache.org/download.cgi)下载最新版本。然后使用命令：
```
	unzip apache-maven-3.3.9-bin.zip
```
或者
```
	tar xzvf apache-maven-3.3.9-bin.tar.gz
```
再将**bin目录**添加到**path路径**。
#### Windows版本 ####
* 请到[Maven Download 页面](https://maven.apache.org/download.cgi)下载最新版本，解压到任意路径
* 添加系统变量M2_HOME为maven根目录
* 添加%M2_HOME%\bin添加到环境变量Path

#### 安装成功验证 ####
使用命令
```
➜  ~ mvn -v
Apache Maven 3.3.9 (bb52d8502b132ec0a5a3f4c09453c07478323dc5; 2015-11-11T00:41:47+08:00)
Maven home: /usr/local/Cellar/maven/3.3.9/libexec
Java version: 1.8.0_66, vendor: Oracle Corporation
Java home: /Library/Java/JavaVirtualMachines/jdk1.8.0_66.jdk/Contents/Home/jre
Default locale: zh_CN, platform encoding: UTF-8
OS name: "mac os x", version: "10.10.5", arch: "x86_64", family: "mac"
```

#### 更新setting.xml文件 ####
Maven分为公共仓库，私有仓库（局域网仓库）和本地仓库。由${user.home}/.m2/settings.xml控制。
* 对于Mac用户，是/Users/${user.home}.m2/settings.xml
* 对于Windows用户，是C:\Users\${user.home}\.m2\settings.xml
通过maven下载的jar统一在相同目录的repository下面。

如果没有.m2文件，执行命令：
```
    mvn help:system
```

### Maven基本概念 ###
Maven项目是以坐标（groupId， artifactId和version）进行唯一确定项目：
* groupId：项目的分组，同一个项目组最好使用同一个
* artifactId：项目的名字
* version：项目的版本号
其中项目版本号分为：
* SNAPSHOT版本
 * 用于保存开发过程中的不稳定版本。
 * 依赖snapshot，如果不改变版本号，直接编译打包时，maven会自动从镜像服务器上下载最新的快照版本。
* RELEASE版本
 * 保存稳定的发行版本。
 * 依赖release，如果不改变版本号，编译打包时如果本地已经存在该版本的模块则不会主动去镜像服务器上下载。

### Maven新建项目 ###
#### 使用Maven命令 ####
这个命令执行时间比较长。
```
	mvn archetype:generate -DgroupId=com.dongyuxi.test -DartifactId=dongyuxi-maven-demo -Dpackage=com.dongyuxi.test.maven.demo -Dversion=0.0.1-SNAPSHOT
```
连按3次回车确认就可以了。
#### 使用Eclipse开发工具（推荐） ####
![maven-eclipse-1.png](/img/technology/maven-eclipse-1.png)
![maven-eclipse-2.png](/img/technology/maven-eclipse-2.png)
![maven-eclipse-3.png](/img/technology/maven-eclipse-3.png)
#### Maven项目目录结构 ####
| 目录                         | 目的                       |
|:---------------------------:|:---------------------------|
|${basedir}                   |存放 pom.xml和所有的子目录     |
|${basedir}/src/main/java     |项目的 java源代码         	   |
|${basedir}/src/main/resources|项目的资源，比如说 property文件	|
|${basedir}/src/test/java     |项目的测试类，比如说 JUnit代码  |
|${basedir}/src/test/resources|测试使用的资源                |
|${basedir}/target/classes    |编译后的class文件位置         |
|${basedir}/target            |编译后的jar文件位置           |

#### Maven项目编译执行 ####
进入maven项目文件夹，执行
```
	mvn clean package
```
在${basedir}/target下会生成jar文件，执行jar文件即可
```
	java -cp target/dongyuxi-maven-demo-0.0.1-SNAPSHOT.jar com.dongyuxi.test.maven.demo.App
```

### Maven项目发布 ###
#### 本地发布 ####
本地发布可以将jar包发布到本地，本机上的其他项目可以依赖该项目，但是其他人无法使用，命令如下
```
	mvn clean install
```
#### 发布仓库 ####
将本地库发布到maven仓库，大家就都可以使用该项目了，命令如下：
```
	mvn deploy
```
