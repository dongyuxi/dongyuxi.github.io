---
layout: post
title: Spring-Boot学习笔记之三：持久化数据存储之Mysql
categories: 技术
tags: [spring-boot,mysql,mac]
keywords: spring-boot,mac,mysql
date: 2016-06-20
permalink: Spring-Boot-3-Mysql
---
### Spring Boot持久化数据存储 ###
Spring Boot利用配置信息和starter简化了访问数据的流程，下面简介访问Mysql数据的步骤。
<!--more-->

#### 步骤一：添加数据库相关依赖 ####
为了访问Mysql数据，需要引入
* spring-boot-starter-data-jpa：JPA(Java Persistence API)是Sun官方提出的Java持久化规范。它为Java开发人员提供了一种对象/关联映射工具来管理Java应用中的关系数据。
* mysql-connector-java：访问Mysql数据库的驱动。
```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
```

#### 步骤二：添加数据库配置 ####
为了测试我们需要在mysql中加入一些测试数据，使用springboot的用户名创建表springboot_test.student，并插入测试数据。
```
create table student
(
  id varchar(20) primary key,
  name varchar(20)
);
```
```
insert into student values("1001", "abc");
insert into student values("1002", "def");
```

在src/main/resources目录下添加application.properties文件并加入数据库配置，其中
* springboot_test：数据库名字
* springboot：用户名 （当然也可以使用root）
```
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/springboot_test?useSSL=false
spring.datasource.username=springboot
spring.datasource.password=
```

#### 步骤三：建立映射实体类 ####
建立和Student表想对应的实体类
```
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
@Entity
public class Student {

    @Id
    private String id;

    @Column(nullable = false)
    private String name;

    protected Student() {
    }

}
```

#### 步骤四：继承CrudRepository类 ####
CrudRepository实现了数据库的CRUD操作，详情可以查看http://docs.spring.io/spring-data/data-commons/docs/1.6.1.RELEASE/reference/html/repositories.html
```
import org.springframework.data.repository.CrudRepository;

import com.dongyuxi.test.db.mysql.Student;

public interface StudentRepository extends CrudRepository<Student, String> {

    Student findStudentById(String id);

}
```

#### 步骤五：新建Controller检验数据库操作 ####
在加入Controller之前，可以先写一个CommandLineRunner读取Student表的总行数。
```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import com.dongyuxi.test.db.mysql.repository.StudentRepository;

import lombok.extern.slf4j.Slf4j;

@Slf4j
@Component
@Order(value = 3)
public class StudentCountRunner implements CommandLineRunner {

    @Autowired
    private StudentRepository studentRepository;

    @Override
    public void run(String... strings) throws Exception {
        log.info("Student table has {} records.", studentRepository.count());
    }

}
```
加入StudentController进行操作
```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.alibaba.fastjson.JSON;
import com.dongyuxi.test.db.mysql.Student;
import com.dongyuxi.test.db.mysql.repository.StudentRepository;

import lombok.extern.slf4j.Slf4j;

@Slf4j
@RestController
@RequestMapping("/student")
public class StudentController {

    @Autowired
    private StudentRepository studentRepository;

    @RequestMapping("/add")
    public String addStudent(@RequestParam(value = "id", required = true) final String id,
            @RequestParam(value = "name", required = true) final String name) {
        final Student student = new Student(id, name);
        studentRepository.save(student);
        log.info("add new student by id {} and name {}", id, name);
        return "add student " + JSON.toJSONString(student);
    }

    @RequestMapping("/query")
    public String queryStudentById(@RequestParam(value = "id", required = true) final String id) {
        final Student student = studentRepository.findStudentById(id);
        log.info("find student {} by id {}", JSON.toJSONString(student), id);
        return JSON.toJSONString(student);
    }

    @RequestMapping("/update")
    public String updateStudent(@RequestParam(value = "id", required = true) final String id,
            @RequestParam(value = "name", required = true) final String name) {
        final Student student = studentRepository.findStudentById(id);
        if (student != null) {
            student.setName(name);
            studentRepository.save(student);
            log.info("update new student by id {} and name {}", id, name);
        } else {
            log.info("student with id {} doesn't exist", id);
        }
        return "update student by id " + id;
    }

    @RequestMapping("/delete")
    public String deleteStudent(@RequestParam(value = "id", required = true) final String id) {
        studentRepository.delete(id);
        log.info("delete student by id {}", id);
        return "delete student by id " + id;
    }

}
```
