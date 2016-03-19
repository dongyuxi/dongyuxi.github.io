---
layout: post
title: Maven笔记之二：依赖基础
categories: 技术
tags: [maven,java]
keywords: maven,java
date: 2016-03-05
permalink: Maven-Dependency-Basic
---
这篇笔记主要记录一下Maven的依赖。
<!--more-->

## 依赖格式 ##
```
<project>
  ...
  <dependencies>
    <dependency>
      <groupId>...</groupId>
      <artifactId>...</artifactId>
      <version>...</version>
      <type>...</type>
      <scope>...</scope>
      <optional>...</optional>
      <exclusions>
        <exclusion>
          <groupId>...</groupId>
          <artifactId>...</artifactId>
        </exclusion>
      </exclusions>
    </dependency>
  </dependencies>  
</project>
```
### groupdId ###
依赖坐标的groupId。
### artifactId ###
依赖坐标的artifactId。
### version ###
依赖坐标的version。
### type ###
依赖的类型，默认为jar。
### scope ###
依赖的范围，用来控制依赖和编译、测试和运行的classpath的关系。
#### complie ####
编译依赖范围，scope的默认值，在编译、测试和运行都需要。
#### test ####
测试依赖范围，只有在编译和运行测试代码的时候才需要。
#### runtime ####
运行时依赖范围，在运行测试和运行项目的时候才有效。
#### provided ####
已提供范围依赖，只对编译和测试有效，但是对运行时无效，该依赖需要在容易里面已经提供了，无需重复。
#### system ####
系统范围依赖，和provided完全一致。不是通过Maven仓库婕曦，一般与本机系统绑定。
#### 系统依赖表 ####
| Scope    | 编译class | 测试classpath | 运行时classpath | 例子             |
|:--------:|:--------:|:-------------:|:--------------:|:----------------:|
| complie  | Y        | Y             | Y              | spring-core      |
| test     | N        | Y             | N              | JUnit            |
| runtime  | N        | Y             | Y              | JDBC             |
| provided | Y        | Y             | N              | tomcat-websocket |
| system   | Y        | Y             | N              | 本地jar包         |
### optional ###
可选依赖标志。在依赖传递部分会讲到。
### exclusions ###
排除该依赖的传递依赖，只需要提供groupId和artifactId就可以，因为Maven解析之后不会出现version不同的情况。

## 依赖传递 ##
### 传递性依赖 ###
依赖具有传递性，如果A依赖于B，B依赖于C，那么A也将依赖于C。
### 依赖调解 ###
我们用A->B表示A依赖于B，假设A->B->C->E(1.0)，同时A->D->E(2.0)，那么路径短优先，使用E(2.0)。如果长度相同，那么就以先声明者优先。
### 可选依赖 ###
使用optional元素可以表示该依赖为可选依赖，就是说该依赖只对当前项目有效，对依赖于当前项目的其他项目无效。比如B->C(optional=true)，A->B，但是A不会依赖于C。
### 排除依赖 ###
使用exclusions就可以排除当前依赖的传递依赖。比如A->B->C->E(1.0)，同时A->D(E exclusion in D)->E(2.0)，A还是会依赖E(1.0)版本。

## 依赖命令 ##
### mvn dependency:list ###
将项目下的所有依赖以列表的形式展示出来。
### mvn dependency:tree ###
将项目下的所有依赖以树的形式展示出来。
### mvn dependency:analyze ###
分析项目下的依赖是否有问题。
