---
layout: post
title: Nginx返回静态内容的2种方式
categories: 技术
tags: [web,nginx,fastcgi,linux]
keywords: web,nginx,fastcgi,linux
date: 2016-11-20
permalink: Nginx-FastCGI-Static-Content
---

在[Nginx Setup](http://dongyuxi.top/2016-10-28/Nginx-FastCGI-Setup.html)已经成功启动Nginx，接下来就是配置显示一些很简单的静态内容，这在测试接口，mock数据的时候很重要。
<!--more-->

### 基本配置 ###
Nginx的默认配置文件在/usr/local/nginx/conf/nginx.conf，基本配置：
```
http {
    ......
    server {
        listen       80;
        server_name  localhost;

        location / {
            root   html;
            index  index.html index.htm;
        }
        ......
    }
    ......
}
```
当访问http://localhost:80或者http://localhost(80是默认端口)访问的就是默认的index.html页面。

### 添加静态内容配置 ###
#### 直接配置内容 ####
在server中加入新的location配置：
```
        location /static_1 {
            return 200 "static_content_1";
        }
```
此时访问http://localhost/static_1就会得到"static_content_1"。
#### 使用静态页面配置
和默认根目录访问类似，配置相应的index.html文件即可：
```
        location /static_2 {
            root   /home/dongyuxi/workplace/nginx-content;
            index  index.html;
        }
```
同时在/home/dongyuxi/workplace/nginx-content文件夹下面建立static_2/index.html文件，内容为static_content_2,。
此时访问http://localhost/static_2就会得到"static_content_2"。
### 备注 ###
#### 修改配置生效 ####
```
sudo /usr/local/nginx/sbin/nginx -s reload
```
#### root和alias的区别 ####
```
        location /static_2 {
            [root|alias]   /workplace/nginx-content;
            index  index.html;
        }
```
* root后面的路径是相对路径的前缀，例子中的文件会从/workplace/nginx-content/static_2开始找index.html。
* alias后面的路径是相对路径的前缀，例子中的文件会从/workplace/nginx-content开始找index.html。
