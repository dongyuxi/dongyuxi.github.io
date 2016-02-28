---
layout: post
title: 删除linux文件中^M
categories: 技术
tags: [经验,linux,vim]
keywords: linux,vim,dos2unix
date: 2016-02-28
permalink: Remove-Linux-M
---
在linux下打开windows编辑过的文件会出现^M符号，这是因为windows下的编辑器和linux编辑器对文件行末的回车符处理不一致.
<!--more-->

回车符在下面3个平台分别为：
>windows：0D0A 
>unix\linux: 0A 
>MAC: 0D 

具体去除方法：
### dos2unix命令
```
	dos2unix filename
```
### vi/vim命令
#### 设置文件格式
```
	vi filename
	:set fileformat=unix
```
#### 替换文件
```
	vi filename
	:1,$ s/^M//g
```
### sed命令
```
	sed -i 's/^M//g' filename
```
### tr命令
```
	cat filename |tr -d '/r' > newfile
```