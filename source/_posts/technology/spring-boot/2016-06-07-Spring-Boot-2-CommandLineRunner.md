---
layout: post
title: Spring-Boot学习笔记之二：应用启动第一步CommandLineRunner
categories: 技术
tags: [spring-boot,mac]
keywords: spring-boot,mac,CommandLineRunner
date: 2016-06-07
permalink: Spring-Boot-2-CommandLineRunner
---
### CommandLineRunner简介 ###
在官网[Using the ApplicationRunner or CommandLineRunner](http://docs.spring.io/autorepo/docs/spring-boot/current/reference/htmlsingle/#boot-features-command-line-runner)中介绍了实现了CommandLineRunner接口的Component会在所有Spring Beans都初始化之后，SpringApplication.run()之前执行，非常适合在应用程序启动之初进行一些数据初始化的工作。
<!--more-->

### CommandLineRunner例子 ###
一个最简单的例子，在CommandLineRunner中打印出来一句话。
```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

@Component
@Order(value = 1)
public class StartupLogging1Runner implements CommandLineRunner {

    private final Logger logger = LoggerFactory.getLogger(StartupLogging1Runner.class);

    @Override
    public void run(String... strings) throws Exception {
        logger.info("startup 1 ......");
    }

}
```
在HelloController中添加构造函数打印出一条log，证明Bean已经被初始化。
```
@RestController
public class HelloController {

    private final Logger logger = LoggerFactory.getLogger(HelloController.class);

    public HelloController() {
        logger.info("HelloController created successfully.");
    }

}
```

### @Order确保执行顺序 ###
如果有多个CommandLineRunner有先后顺序执行，那么可以使用@org.springframework.core.annotation.Order进行标注，value越小越先执行。
```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

@Component
@Order(value = 1)
public class StartupLogging1Runner implements CommandLineRunner {

    private final Logger logger = LoggerFactory.getLogger(StartupLogging1Runner.class);

    @Override
    public void run(String... strings) throws Exception {
        logger.info("startup 1 ......");
    }

}
```
```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

@Component
@Order(value = 2)
public class StartupLogging2Runner implements CommandLineRunner {

    private final Logger logger = LoggerFactory.getLogger(StartupLogging2Runner.class);

    @Override
    public void run(String... strings) throws Exception {
        logger.info("startup 2 ......");
    }

}
```
最后启动的时候会显示如下log
```

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::        (v1.3.5.RELEASE)

2016-06-07 11:37:56.049  INFO 20611 --- [           main] com.dongyuxi.test.HelloApplication       : Starting HelloApplication on dongyuxideMacBook-Air.local with PID 20611 (/workspace/dongyuxi/spring-boot/dongyuxi-spring-boot/target/classes started by dongyuxi in /workspace/dongyuxi/spring-boot/dongyuxi-spring-boot)
2016-06-07 11:37:56.053  INFO 20611 --- [           main] com.dongyuxi.test.HelloApplication       : No active profile set, falling back to default profiles: default
2016-06-07 11:37:56.155  INFO 20611 --- [           main] ationConfigEmbeddedWebApplicationContext : Refreshing org.springframework.boot.context.embedded.AnnotationConfigEmbeddedWebApplicationContext@7ba18f1b: startup date [Tue Jun 07 11:37:56 CST 2016]; root of context hierarchy
2016-06-07 11:37:58.275  INFO 20611 --- [           main] s.b.c.e.t.TomcatEmbeddedServletContainer : Tomcat initialized with port(s): 8080 (http)
2016-06-07 11:37:58.296  INFO 20611 --- [           main] o.apache.catalina.core.StandardService   : Starting service Tomcat
2016-06-07 11:37:58.297  INFO 20611 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet Engine: Apache Tomcat/8.0.33
2016-06-07 11:37:58.436  INFO 20611 --- [ost-startStop-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2016-06-07 11:37:58.436  INFO 20611 --- [ost-startStop-1] o.s.web.context.ContextLoader            : Root WebApplicationContext: initialization completed in 2287 ms
2016-06-07 11:37:58.827  INFO 20611 --- [ost-startStop-1] o.s.b.c.e.ServletRegistrationBean        : Mapping servlet: 'dispatcherServlet' to [/]
2016-06-07 11:37:58.834  INFO 20611 --- [ost-startStop-1] o.s.b.c.embedded.FilterRegistrationBean  : Mapping filter: 'characterEncodingFilter' to: [/*]
2016-06-07 11:37:58.835  INFO 20611 --- [ost-startStop-1] o.s.b.c.embedded.FilterRegistrationBean  : Mapping filter: 'hiddenHttpMethodFilter' to: [/*]
2016-06-07 11:37:58.835  INFO 20611 --- [ost-startStop-1] o.s.b.c.embedded.FilterRegistrationBean  : Mapping filter: 'httpPutFormContentFilter' to: [/*]
2016-06-07 11:37:58.835  INFO 20611 --- [ost-startStop-1] o.s.b.c.embedded.FilterRegistrationBean  : Mapping filter: 'requestContextFilter' to: [/*]
2016-06-07 11:37:58.916  INFO 20611 --- [           main] c.d.test.controller.HelloController      : HelloController created successfully.
2016-06-07 11:37:59.222  INFO 20611 --- [           main] s.w.s.m.m.a.RequestMappingHandlerAdapter : Looking for @ControllerAdvice: org.springframework.boot.context.embedded.AnnotationConfigEmbeddedWebApplicationContext@7ba18f1b: startup date [Tue Jun 07 11:37:56 CST 2016]; root of context hierarchy
2016-06-07 11:37:59.308  INFO 20611 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/hello]}" onto public java.lang.String com.dongyuxi.test.controller.HelloController.hello(java.lang.String)
2016-06-07 11:37:59.312  INFO 20611 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/error]}" onto public org.springframework.http.ResponseEntity<java.util.Map<java.lang.String, java.lang.Object>> org.springframework.boot.autoconfigure.web.BasicErrorController.error(javax.servlet.http.HttpServletRequest)
2016-06-07 11:37:59.313  INFO 20611 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/error],produces=[text/html]}" onto public org.springframework.web.servlet.ModelAndView org.springframework.boot.autoconfigure.web.BasicErrorController.errorHtml(javax.servlet.http.HttpServletRequest,javax.servlet.http.HttpServletResponse)
2016-06-07 11:37:59.353  INFO 20611 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/webjars/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2016-06-07 11:37:59.354  INFO 20611 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2016-06-07 11:37:59.400  INFO 20611 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/**/favicon.ico] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2016-06-07 11:37:59.565  INFO 20611 --- [           main] o.s.j.e.a.AnnotationMBeanExporter        : Registering beans for JMX exposure on startup
2016-06-07 11:37:59.676  INFO 20611 --- [           main] s.b.c.e.t.TomcatEmbeddedServletContainer : Tomcat started on port(s): 8080 (http)
2016-06-07 11:37:59.680  INFO 20611 --- [           main] c.d.test.runner.StartupLogging1Runner    : startup 1 ......
2016-06-07 11:37:59.681  INFO 20611 --- [           main] c.d.test.runner.StartupLogging2Runner    : startup 2 ......
2016-06-07 11:37:59.682  INFO 20611 --- [           main] com.dongyuxi.test.HelloApplication       : Started HelloApplication in 4.304 seconds (JVM running for 4.78)
```
