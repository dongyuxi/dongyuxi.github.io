---
layout: post
title: Tensorflow学习笔记之一：安装、Hello World配置和运行(Mac)
categories: 技术
tags: [tensorflow,mac]
keywords: tensorflow,mac,setup
date: 2016-10-08
permalink: Tensorflow-Setup-Mac
---
### Tensorflow简介 ###
[Tensorflow Github](https://github.com/tensorflow/tensorflow)的介绍是最权威的，我这里就不再过多介绍了。
<!--more-->

### Tensorflow安装 ###
其实[Tensorflow Setup](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/g3doc/get_started/os_setup.md)文档写的也是相当权威，我这里只是把我遇到的问题列出来。

我用到的是Python 2.7.11和pip进行Tensorflow安装。
使用命令
```
$ sudo pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.11.0rc0-py2-none-any.whl
```
这里可能遇到2个问题：
* whl文件的链接可能无法触碰，这个可以自己想办法
* 下载过程中如果中断可能会从头开始

这2个问题都可以通过直接下载文件解决（可以使用迅雷或者浏览器下载），之后执行命令
```
sudo pip install --upgrade tensorflow-0.11.0rc0-py2-none-any.whl
```

### Tensorflow验证 ###
```
$ python
...
>>> import tensorflow as tf
>>> hello = tf.constant('hello, world')
>>> sess = tf.Session()
>>> print(sess.run(hello))
hello, world
>>> a = tf.constant(10)
>>> b = tf.constant(20)
>>> print(sess.run(a + b))
30
```
