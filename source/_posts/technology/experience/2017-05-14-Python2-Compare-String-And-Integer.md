---
layout: post
title: Python2比较字符串和整型
categories: 技术
tags: [经验,python]
keywords: python,string,integer
date: 2017-05-14
permalink: Python2-Compare-String-And-Integer
---
在上周遇到的一个线上问题，最后定位到Python2在比较String和Integer的时候和预期不一致，示例如下：
```
    Python 2.7.11 (default, Jan 22 2016, 08:28:37)
    [GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 6 < '4'
    True
```
还是依靠神器stackoverflow，直接找到答案[http://stackoverflow.com/questions/3270680/how-does-python-compare-string-and-int](http://stackoverflow.com/questions/3270680/how-does-python-compare-string-and-int)

Python2官方解答：[https://docs.python.org/2/library/stdtypes.html#comparisons](https://docs.python.org/2/library/stdtypes.html#comparisons)

英文的解释如下：
>CPython implementation detail: Objects of different types except numbers are ordered by their type names; objects of the same types that don’t support proper comparison are ordered by their address.

中文翻译
>非数字类型的不同类型的实例进行比较顺序依赖于类型的名字（例如Integer < String）；不支持比较的相同类型的实例比较顺序依赖于实例的地址

好在Python3的时候禁止了这种比较，不同类型之间不能进行比较。