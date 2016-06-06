---
layout: post
title: Docker学习笔记之二：运行并创建镜像(Mac)
categories: 技术
tags: [docker,mac]
keywords: docker,mac,install,create
date: 2016-05-29
permalink: Docker-Run-And-Create-Image-Mac
---
### Docker运行镜像 ###
在上一篇[Docker学习笔记之一：简介和安装(Mac)](/2016-03-16/Docker-Setup-Mac.html)文章中里面提到了运行
```
docker run hello-world
```
实际上这时已经运行了hello-world这个镜像，其他的镜像可以在[Docker Hub](https://hub.docker.com/)中寻找，首先需要注册账号，然后搜索镜像名称，比如[docker/whalesay](https://hub.docker.com/r/docker/whalesay/)，这个是官方网站的一个demo。
```
$ docker run docker/whalesay cowsay boo
     _____
    < boo >
     -----
            \
             \
                \     
                                            ##        .            
                                ## ## ##       ==            
                         ## ## ## ##      ===            
                 /""""""""""""""""___/ ===        
        ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~   
                 \______ o          __/            
                    \    \        __/             
                        \____\______/
```

<!--more-->

### 建立自己的镜像 ###
以下内容参考：
* [Find and run the whalesay image](https://docs.docker.com/mac/step_three/)
* [Build your own image](https://docs.docker.com/mac/step_four/)
* [Create a Docker Hub account & repository](https://docs.docker.com/mac/step_five/)
* [Tag, push, and pull your image](https://docs.docker.com/mac/step_six/)
#### 建立本地镜像 ####
新建Docker Workspace
```
mkdir dongyuxi-say
```
新建DockerFile
```
vim Dockerfile
FROM docker/whalesay:latest

RUN apt-get -y update && apt-get install -y fortunes

CMD /usr/games/fortune -a | cowsay
```
执行docker build，读取“.”文件夹下面的DockerFile文件，依次执行文件中的3条命令，同时在本地build名字为“dongyuxi-say”的镜像。
```
docker build -t dongyuxi-say .
```
执行docker images，会发现本地的镜像库多了dongyuxi-say。
```
➜  dongyuxi-say docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
dongyuxi-say        latest              5f84a894d254        7 minutes ago       274.6 MB
hello-world         latest              690ed74de00f        7 months ago        960 B
docker/whalesay     latest              6b362a9f73eb        12 months ago       247 MB
```
#### 发布镜像 ####
在[hub.docker.com](https://hub.docker.com/)中申请个人账号，可以发现本地的镜像中是不带namespace，所谓namespace就是自己的Docker Hub的username，使用命令
```
docker tag [image_id] [username]/[image_name]:[version_tag]
docker tag 5f84a894d254 dongyuxi/dongyuxi-say:latest
```
此时查看本地镜像会发现多了一条相同ID的镜像。
```
➜  dongyuxi-say docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
dongyuxi-say            latest              5f84a894d254        14 minutes ago      274.6 MB
dongyuxi/dongyuxi-say   latest              5f84a894d254        14 minutes ago      274.6 MB
hello-world             latest              690ed74de00f        7 months ago        960 B
docker/whalesay         latest              6b362a9f73eb        12 months ago       247 MB
```
设置Docker Hub信息
```
docker login --username=yourhubusername --email=youremail@company.com
```
使用Push命令发布到Docker Hub(和Git的命令真是接近啊)
```
docker push dongyuxi/dongyuxi-say
```
删除本地镜像，重新Pull刚刚Push的镜像
```
docker rmi -f 5f84a894d254
docker run dongyuxi/dongyuxi-say
```
