---
layout: post
title: Nginx + FastCGI
categories: 技术
tags: [web,nginx,fastcgi,linux]
keywords: web,nginx,fastcgi,linux
date: 2016-10-28
permalink: Nginx-FastCGI-Setup
---

<!--more-->

### 安装 ###
#### 安装PCRE ####
```
wget http://downloads.sourceforge.net/project/pcre/pcre/8.39/pcre-8.39.tar.gz
tar -zxf pcre-8.39.tar.gz
cd pcre-8.39
./configure
sudo make
sudo make install
```

#### 安装zlib ####
```
wget http://jaist.dl.sourceforge.net/project/libpng/zlib/1.2.8/zlib-1.2.8.tar.gz
tar -zxf zlib-1.2.8.tar.gz
cd zlib-1.2.8
./configure
sudo make
sudo make install
```

#### 安装Nginx ####
```
wget http://nginx.org/download/nginx-1.10.2.tar.gz
tar -zxf nginx-1.10.2.tar.gz
cd nginx-1.10.2
./configure
sudo make
sudo make install
```

### 验证 ###
#### 启动 ####
```
sudo /usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf
```
#### 访问 ####
```
curl http://localhost:80
```
如果没有问题，会得到如下结果：
```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

#### 查询进程 ####
查询本地线程：
```
ps -ef | grep nginx
root     125458      1  0 17:28 ?        00:00:00 nginx: master process /usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf
nobody   125459 125458  0 17:28 ?        00:00:00 nginx: worker process
```
pid应该和nginx.pid中记录的一样
```
cat /usr/local/nginx/logs/nginx.pid
125458
```
#### 停止 ####
```
sudo /usr/local/nginx/sbin/nginx -s stop
```
查询nginx进程已经不在

### 问题 ###
#### libpcre.so.1 ####
* Question：
```
/usr/local/nginx/sbin/nginx: error while loading shared libraries: libpcre.so.1: cannot open shared object file: No such file or directory
```
* Answer：
```
ldd $(which /usr/local/nginx/sbin/nginx)
	linux-vdso.so.1 =>  (0x00007fff0b3ff000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fafcec05000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fafce9e8000)
	libcrypt.so.1 => /lib/x86_64-linux-gnu/libcrypt.so.1 (0x00007fafce7ae000)
	libpcre.so.1 => not found
	libssl.so.1.0.0 => /lib/x86_64-linux-gnu/libssl.so.1.0.0 (0x00007fafce550000)
	libcrypto.so.1.0.0 => /lib/x86_64-linux-gnu/libcrypto.so.1.0.0 (0x00007fafce173000)
	libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007fafcdf5c000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fafcdb9e000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fafcee13000)
```
发现libpcre.so.1无法找到，可以手动建立软连接
```
sudo ln -s /usr/local/lib/libpcre.so.1 /lib/x86_64-linux-gnu/libpcre.so.1
```
