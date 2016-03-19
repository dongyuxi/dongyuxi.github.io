---
layout: post
title: Docker学习笔记之一：简介和安装(Mac)
categories: 技术
tags: [docker,mac]
keywords: docker,mac,setup
date: 2016-03-16
permalink: Docker-Setup-Mac
---
### Docker安装 ###
[Install Docker Toolbox on Mac OS X](https://docs.docker.com/mac/step_one/)
<!--more-->

#### Docker Toolbox安装 ####
下载[Docker Toolbox](https://www.docker.com/products/docker-toolbox)，默认安装做了如下工作：
* installs binaries for the Docker tools in /usr/local/bin
* makes these binaries available to all users
* installs VirtualBox; or updates any existing installation

#### Docker Toolbox启动 ####
启动*Docker Quickstart Terminal*，当你看到这艘传的时候你就成功了。
```
Running pre-create checks...
Creating machine...
(default) Copying /Users/dongyuxi/.docker/machine/cache/boot2docker.iso to /Users/dongyuxi/.docker/machine/machines/default/boot2docker.iso...
(default) Creating VirtualBox VM...
(default) Creating SSH key...
(default) Starting the VM...
(default) Check network to re-create if needed...
(default) Found a new host-only adapter: "vboxnet0"
(default) Waiting for an IP...
Waiting for machine to be running, this may take a few minutes...
Detecting operating system of created instance...
Waiting for SSH to be available...
Detecting the provisioner...
Provisioning with boot2docker...
Copying certs to the local machine directory...
Copying certs to the remote machine...
Setting Docker configuration on the remote daemon...
Checking connection to Docker...
Docker is up and running!
To see how to connect your Docker Client to the Docker Engine running on this virtual machine, run: /usr/local/bin/docker-machine env default

                      ##         .
                ## ## ##        ==
             ## ## ## ## ##    ===
         /"""""""""""""""""\___/ ===
    ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
         \______ o           __/
           \    \         __/
            \____\_______/

```
#### Docker Hub的hello-world验证####
执行命令时候要多做几次尝试。
```
➜  ~ docker run hello-world
Unable to find image 'hello-world:latest' locally
docker: Error response from daemon: Get https://registry-1.docker.io/v2/library/hello-world/manifests/latest: Get https://auth.docker.io/token?scope=repository%3Alibrary%2Fhello-world%3Apull&service=registry.docker.io: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers).
See 'docker run --help'.
```
成功信息如下。
```
➜  ~ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world

03f4658f8b78: Pull complete
a3ed95caeb02: Pull complete
Digest: sha256:8be990ef2aeb16dbcb9271ddfe2610fa6658d13f6dfb8bc72074cc1ca36966a7
Status: Downloaded newer image for hello-world:latest

Hello from Docker.
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker Hub account:
 https://hub.docker.com

For more examples and ideas, visit:
 https://docs.docker.com/userguide/
 ```
