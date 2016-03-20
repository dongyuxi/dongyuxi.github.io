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
### 基本命令 ###
* 官方命令文档：http://redis.io/commands
* RedisFans汉化文档：http://doc.redisfans.com

#### 服务端启动 ####
用brew安装的目录在/usr/local/Cellar/redis/3.0.6/bin/下面。
```
./redis-server
21133:C 16 Mar 10:46:01.578 # Warning: no config file specified, using the default config. In order to specify a config file use ./redis-server /path/to/redis.conf
21133:M 16 Mar 10:46:01.581 * Increased maximum number of open files to 10032 (it was originally set to 2560).
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 3.0.6 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 21133
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           http://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

21133:M 16 Mar 10:46:01.582 # Server started, Redis version 3.0.6
21133:M 16 Mar 10:46:01.582 * The server is now ready to accept connections on port 6379
21133:M 16 Mar 11:46:02.006 * 1 changes in 3600 seconds. Saving...
21133:M 16 Mar 11:46:02.009 * Background saving started by pid 22020
22020:C 16 Mar 11:46:02.013 * DB saved on disk
21133:M 16 Mar 11:46:02.114 * Background saving terminated with success
```
#### 客户端启动 ####
```
./redis-cli
```

### Redis和Tair对比 ###
* 优势：
 * 可以动态调整过期时间
 * 更加丰富的API，支持列表，集合，哈希等数据结构的基本操作
 * 内部使用文档中说明的是对内部使用免费
 * 如果列表和集合都是字符串，使用KVStore可以避免序列化的工作
* 劣势：
 * 如果列表和集合的元素都是需要序列化的对象，需要转成String后才能存入KVStore，带来大量的序列化和反序列化的消耗。

* 综合建议：
 * 对列表，集合和哈希等数据结构需要操作优先考虑KVStore。
 * 对元素都是String的数据可以优先考虑KVStore。
