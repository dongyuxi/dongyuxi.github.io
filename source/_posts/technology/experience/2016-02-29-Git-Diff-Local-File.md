---
layout: post
title: 使用Git命令对比本地文件
categories: 技术
tags: [经验,linux,git]
keywords: linux,vim,git
date: 2016-02-29
permalink: Git-Diff-Local-File
---
有时候需要比较2个本地文件的差异，我们都知道git diff可以查看本地文件的改动，自然我们也可以使用该命令对本地文件进行比较，具体命令如下：
```
    git diff --no-index fileA fileB
```