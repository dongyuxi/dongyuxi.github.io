---
layout: post
title: Intellij Idea导出jar文件
categories: 技术
tags: [java,Intellij]
keywords: java,Intellij,jar
date: 2016-06-12
permalink: intellij-export-jar
---
这几天使用Intellij进行开发，真是不太习惯，上来export jar文件就折腾了一阵子。下面简单说下整个了流程和遇到的问题吧。
<!--more-->

#### 导出可执行jar文件 ####
* Step 1 新建HelloWorld项目
* Step 2 File -> Project Structure进入项目设置（mac下快捷键“Command + ;”）
![intellij_export_step_2.png](/img/technology/intellij_export_step_2.png)
* Step 3 设置Artifacts，点击“+” -> jar -> From Modules with Dependencies，选择Main Class，之后选择jar文件名字和路径，并点击OK结束。
![intellij_export_step_3_1.png](/img/technology/intellij_export_step_3_1.png)
![intellij_export_step_3_2.png](/img/technology/intellij_export_step_3_2.png)
* Step 4 Build -> Build Artifacts选择自己的Artifact即可。
![intellij_export_step_4.png](/img/technology/intellij_export_step_4.png)
* Step 5 使用java -jar HelloWorld.jar执行

#### 导出maven jar文件问题 ####
在导出Maven项目的时候使用默认配置出现了问题，找了好久，终于在[stackoverflow](http://stackoverflow.com/questions/20952713/wrong-manifest-mf-in-intellij-idea-created-jar)上找到了答案。
现象就是在执行的时候会报：
```
***.jar中没有主清单属性
或者
no main manifest attribute, in ***.jar
```
解决方案就是：
```
确保MANIFEST.MF文件在
src/main/resources/META_INF/
而不是
src/main/java/META_INF/
