---
layout: post
title: 使用Google QR API 生成当前网站的二维码
categories: 技术
tags: [经验,api]
keywords: google,api,二维码,命令,参数
date: 2014-11-02
permalink: Google-QR-API
---
今天突然突发奇想，想在自己的网站的每一篇博客的某个位置加上一个跟风的“二维码”，虽然本来traffic就不大，加上能用的人更是几乎为0，但是还是想知道怎么弄。查了一会儿资料，发现Google有个API直接解决了所有问题......
<!--more-->

Google QR API：
```
    https://chart.googleapis.com/chart?cht=qr&chs=<width>x<height>&chl=<data>

    cht=qr - 声明这是二维码图形
    chs=<width>x<height> - 二维码图形的大小
    chl=<data> - 二维码图形的源数据
```
例如我的首页的网站就是可以这样获得
```
    https://chart.googleapis.com/chart?cht=qr&chs=200x200&chl=http://dongyuxi.top
```
![Yuxi Top Blog - 董玉玺的个人博客](https://chart.googleapis.com/chart?cht=qr&chs=200x200&chl=http://dongyuxi.top)

但是貌似杯具了，我在我的测试环境完全没问题，而且在我的电脑访问也没问题，但是在3G手机上和公司网络都不可以，我突然意识到，我们之间隔了一道墙。
