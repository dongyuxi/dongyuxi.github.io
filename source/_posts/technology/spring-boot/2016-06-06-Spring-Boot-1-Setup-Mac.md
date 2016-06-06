---
layout: post
title: Spring-Boot学习笔记之一：简介、Hello World配置和运行(Mac)
categories: 技术
tags: [spring-boot,mac]
keywords: spring-boot,mac,setup
date: 2016-06-16
permalink: Spring-Boot-Setup-Mac
---
### Spring-Boot简介 ###
[spring-boot](http://projects.spring.io/spring-boot/)帮助开发人员省略了spring的大量配置（很多是重复的），可以快速开发微服务。
* 创建独立的Spring应用
* 内嵌了Tomcat，Jetty等服务器，不需要部署war包等
* pom集成了大量依赖的starter，方便开发者进行配置
* 自动配置Spring
* 启动速度非常快
* ...
<!--more-->

### Spring-Boot开发 ###
以下内容是基于Maven的，相关配置请参考[Maven笔记之一：简介和安装(Mac和Windows)](/2016-03-18/Maven-Setup.html)
一切都要从[start.spring.io](http://start.spring.io/)开始，它给了你一个很好的起步。
![spring-boot-startup.png](/img/technology/spring-boot-startup.png)
* 填写GroupId和ArtifactId
* 添加Web Starter（在Dependencies中输入Web）
* 点击“Generate Project”
* 解压zip压缩包
* 以Maven项目导入Eclipse
可以看到在HelloApplication类里面有我们熟悉的main方法，同时有@SpringBootApplication，这是spring-boot的入口标志。
```
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HelloApplication {

    public static void main(String[] args) {
        SpringApplication.run(HelloApplication.class, args);
    }

}
```
添加新的Controller类，通过@RequestMapping添加访问路径关系
```
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @RequestMapping("/hello")
    public String hello(@RequestParam(value = "name") final String name) {
        return "hello " + name;
    }

}
```
此时可以在命令行中执行
```
mvn spring-boot:run
```
或者在Eclipse执行main函数。
访问[http://localhost:8080/hello?name=dongyuxi](http://localhost:8080/hello?name=dongyuxi)出现了
```
hello dongyuxi
```
