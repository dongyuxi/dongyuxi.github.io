---
layout: post
title: Redis学习笔记之一：简介和安装(Mac)
categories: 技术
tags: [redis,mac]
keywords: redis,setup,mac
date: 2016-03-18
permalink: Redis-1-Setup-Mac
---
### Redis简介 ###
[Redis](http://redis.io)是一个开源的内存中的数据结构存储系统，同时也是一个高性能的key-value数据库，和memory cache相比，Redis支持的value数据类型更多，包括字符串（strings），散列（hashes），列表（lists），集合（sets），有序集合（sorted sets）与范围查询，bitmaps，hyperloglogs和地理空间（geospatial）索引半径查询。为了保证效率，数据都是缓存在内存中。区别的是Redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，并且在此基础上实现了master-slave(主从)同步。
<!--more-->

#### Redis优势 ####
* **异常快速** Redis的速度非常快，读的速度是110000次/s,写的速度是81000次/s 。（2012年数据）
* **支持丰富的数据类型** Redis支持最大多数开发人员已经知道像列表，集合，有序集合，散列数据类型。可以保证适应各种情况。
* **操作都是原子性** 所有Redis操作是原子的，这保证了如果两个客户端同时访问的Redis服务器将获得更新后的值。

#### Redis劣势 ####
* 数据库容量受到物理内存的限制，不能用作海量数据的高性能读写，因此Redis适合的场景主要局限在较小数据量的高性能操作和运算上。

### Redis安装 ###
#### brew ####
```
➜ ~ brew install redis
==> Downloading https://homebrew.bintray.com/bottles/redis-3.0.6.yosemite.bottle.tar.gz
Already downloaded: /Library/Caches/Homebrew/redis-3.0.6.yosemite.bottle.tar.gz
==> Pouring redis-3.0.6.yosemite.bottle.tar.gz
==> Caveats
To have launchd start redis at login:
  ln -sfv /usr/local/opt/redis/*.plist ~/Library/LaunchAgents
Then to load redis now:
  launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
Or, if you don't want/need launchctl, you can just run:
  redis-server /usr/local/etc/redis.conf
==> Summary
🍺  /usr/local/Cellar/redis/3.0.6: 9 files, 876.4K
```
#### 源码安装 ####
```
wget http://download.redis.io/releases/redis-3.0.7.tar.gz
tar xzf redis-3.0.7.tar.gz
cd redis-3.0.7
make
```
