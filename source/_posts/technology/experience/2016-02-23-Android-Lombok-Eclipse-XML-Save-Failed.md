---
layout: post
title: Eclipse安装Lombok和Android后保存xml文件失败
categories: 技术
tags: [经验,eclipse]
keywords: eclipse,lombok,android,xml
date: 2016-02-23
permalink: Eclipse-Lombok-Android-XML-Failed
---
[Android SDK](http://developer.android.com/sdk/index.html)和[Lombok](https://projectlombok.org/)都是好东西，但是在Eclipse安装了这2个插件之后貌似会出现一些问题。
<!--more-->

具体问题就是在保存xml文件的时候会出现如下错误：
>Save failed.
>Could not initialize class com.android.tools.lint.checks.BuiltinIssueRegistry

查了半天终于在一个[西班牙文的网页](http://www.dosmweb.com/blog/index.php?post/2015/07/05/Project-Lombok%3A-Android)上找到了正解：
>Eclipse->Preferences->Android->Lint Error Checking->uncheck "When saving files, check for errors"
