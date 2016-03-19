---
layout: post
title: Maven笔记之三：聚合与继承
categories: 技术
tags: [maven,java]
keywords: maven,java
date: 2016-03-12
permalink: Maven-Aggregation-Inheritance
---
这篇笔记主要记录一下Maven的聚合与继承。
<!--more-->

## Maven的聚合 ##
聚合就是把若干个模块一起构建。具体格式：
```
<project>
	<modelVersion>4.0.0</modelVersion>
	<groupId>...</groupId>
	<artifactId>...</artifactId>
	<version>...</version>
	<packaging>pom</packaging>
	<name>...</name>
	 <modules>
		<module>...</module>
		<module>...</module>
	 </modules>
</project>
```
需要注意的是<packaging>类型是pom，<model>的路径是从当前路径下开始。

## Maven的继承 ##
继承和java中的继承关系类似，继承自同一个父模块的子模块不需要重复定义公共信息，比如依赖版本号等。
例如父模块：
```
<project>
	<modelVersion>4.0.0</modelVersion>
	<groupId>...</groupId>
	<artifactId>xxx-parent</artifactId>
	<version>1.0.0-SNAPSHOT</version>
	<packaging>pom</packaging>
	<name>...</name>
</project>
```
子模块：
```
<project>
	<modelVersion>4.0.0</modelVersion>

	<parent>
		<groupId>...</groupId>
		<artifactId>xxx-parent</artifactId>
		<version>1.0.0-SNAPSHOT</version>
	</parent>

	<artifactId>xxx-child1</artifactId>
</project>
```
需要注意的是<artifactId>是不可以继承的，否则坐标（groupId，artifactId和version）全部相同就会产生冲突。

## Maven的聚合与继承关系 ##
### 聚合与继承本质区别 ###
+ 聚合：协同构建
+ 继承：消除重复
+ 聚合模块和继承模块的父模块可以是同一个模块，但是也可以是在不同的模块

### 聚合与继承相同点 ###
+ 聚合pom和父pom的<packaging>都是pom
+ 聚合模块和父模块除了pom没有实际内容

### 聚合与继承不同点 ###
+ 对于聚合，聚合模块知道被聚合模块的信息，被聚合的模块不知道聚合模块
+ 对于继承，父模块不知道继承自它的子模块，子模块知道父模块的信息
