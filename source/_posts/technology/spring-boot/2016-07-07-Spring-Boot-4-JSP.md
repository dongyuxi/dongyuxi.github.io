---
layout: post
title: Spring-Boot学习笔记之四：支持JSP
categories: 技术
tags: [spring-boot,jsp,mac]
keywords: spring-boot,mac,jsp
date: 2016-07-07
permalink: Spring-Boot-4-JSP
---
Spring Boot默认情况下（只依赖spring-boot-starter-web）不支持jsp，支持jsp需要如下步骤。
<!--more-->

#### 步骤一：添加JSP相关依赖 ####
在pom.xml文件中添加依赖tomcat-embed-jasper和jstl。
```
<dependency>
    <groupId>org.apache.tomcat.embed</groupId>
    <artifactId>tomcat-embed-jasper</artifactId>
    <scope>provided</scope>
</dependency>
<dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>jstl</artifactId>
</dependency>
```

#### 步骤二：添加MVC配置 ####
在application.properties文件中添加
```
spring.mvc.view.prefix=/WEB-INF/jsp/
spring.mvc.view.suffix=.jsp
```

#### 步骤三：创建jsp文件和对应的实体类 ####
添加实体类。
```
package com.dongyuxi.test.model;

import lombok.Data;

@Data
public class JSPDemoModel {

    private String name;

}
```
添加jsp文件。
```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page
    import="com.dongyuxi.test.model.JSPDemoModel"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Spring Boot JSP Demo</title>
</head>
<body>
<%
    final JSPDemoModel model = (JSPDemoModel)request.getAttribute("jspDemoModel");
    if (model != null) {
%>
        Hello <%=model.getName() %>
<%
    }
%>
</body>
</html>
```

#### 步骤四：创建测试Controller类 ####
```
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.dongyuxi.test.model.JSPDemoModel;

@Controller
public class JSPDemoController {

    @RequestMapping("/jsptest")
    public ModelAndView test(@RequestParam(value = "name", required = false) final String name) {
        if (name == null) {
            return new ModelAndView("demo");
        } else {
            final JSPDemoModel model = new JSPDemoModel();
            model.setName(name);
            return new ModelAndView("demo", "jspDemoModel", model);
        }
    }

}
```

#### 步骤五：访问测试页面 ####
访问http://localhost:8080/jsptest?name=dongyuxi，看到
```
Hello dongyuxi
```
