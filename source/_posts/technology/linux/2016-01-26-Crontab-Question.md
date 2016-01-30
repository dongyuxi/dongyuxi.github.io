---
layout: post
title: Crontab中问号?的作用
categories: 技术
tags: [linux,ubuntu,crontab]
keywords: linux,ubuntu,crontab,命令,参数
date: 2016-01-26
permalink: Crontab-Question
---
在工作中遇到了一个小问题，关于crontab中的星号*和问号？之间的区别。因为平时用到星号是最多的，所以对问号突然一时想不起来了，因为这个东西和正则表达式要是和正则表达式混在一起记忆就很难理解。
<!--more-->

其实这个东西非常简单，平时绝大部分时间我们用到的都是星号，表示不受限制，只受那些有数字的限制。问号的作用就是解决那些有矛盾的。

先看下官方文档：
> The '?' character is allowed for the day-of-month and day-of-week fields. It is used to specify 'no specific value'. This is useful when you need to specify something in one of the two fileds, but not the other. See the examples below for clarification.

我稍微解释下就是：
> '?'是为了解决日期和星期之间的互斥性，因为如果设置成每个月一号同时设置每个星期一执行任务的话，任务便会不知道该哪天执行。所以当日期或者星期中一个有值的时候，另一个就应该用'?'。