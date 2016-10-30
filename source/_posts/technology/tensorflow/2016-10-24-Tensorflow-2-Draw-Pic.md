---
layout: post
title: Tensorflow学习笔记之二：梵高作画
categories: 技术
tags: [tensorflow,mac]
keywords: tensorflow,mac,画图，梵高
date: 2016-10-08
permalink: Tensorflow-Setup-Mac
---
### 准备工作 ###
好久就听说使用Tensorflow可以学着梵高画画，准备尝试下，结果踩了很多坑，在这里总结下，避免大家走重复弯路。
<!--more-->

#### 环境 ####
OS：Mac-10.10.5
Python：2.7.11
Tensorflow：[0.11.0rc0-py2](https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.11.0rc0-py2-none-any.whl)

#### 基本工具 ####
安装 & 下载
* [neural-style](https://github.com/anishathalye/neural-style.git)
* [vgg-19](http://www.vlfeat.org/matconvnet/models/beta16/imagenet-vgg-verydeep-19.mat)
在网络不稳定的条件下不得不说是一种煎熬，文件略大而且网络不稳定。
将imagenet-vgg-verydeep-19.mat文件copy到neural-style文件夹中即可。

### 开始画图 ###
在neural-style文件夹下执行
```
python neural_style.py --content ./test_input.jpg --styles examples/1-style.jpg --output test_output.jpg
```
本来以为静静等待出来一张梵高风格的图，结果上来就报了如下的错误。

### 解决错误 ###
#### 缺少scipy.misc ####
* 执行现象
```
ImportError: No module named scipy.misc
AttributeError: 'module' object has no attribute 'misc'
```
* 解决方案
```
pip install scipy
```
#### 缺少Pillow ####
* 执行现象
```
Traceback (most recent call last):
  File "neural_style.py", line 152, in <module>
    main()
  File "neural_style.py", line 85, in main
    content_image = imread(options.content)
  File "neural_style.py", line 143, in imread
    return scipy.misc.imread(path).astype(np.float)
AttributeError: module 'scipy.misc' has no attribute 'imread'
```
* 解决方案
```
brew install libtiff libjpeg webp little-cms2
pip install Pillow

```
#### 执行现象 ####
```
Traceback (most recent call last):
  File "neural_style.py", line 152, in <module>
    main()
  File "neural_style.py", line 130, in main
    checkpoint_iterations=options.checkpoint_iterations
  File "/home/dyx107107/workspace/github/neural-style/stylize.py", line 41, in stylize
    net, mean_pixel = vgg.net(network, image)
  File "/home/dyx107107/workspace/github/neural-style/vgg.py", line 24, in net
    data = scipy.io.loadmat(data_path)
  File "/usr/lib/python2.7/dist-packages/scipy/io/matlab/mio.py", line 152, in loadmat
    matfile_dict = MR.get_variables(variable_names)
  File "/usr/lib/python2.7/dist-packages/scipy/io/matlab/mio5.py", line 290, in get_variables
    res = self.read_var_array(hdr, process)
  File "/usr/lib/python2.7/dist-packages/scipy/io/matlab/mio5.py", line 253, in read_var_array
    return self._matrix_reader.array_from_header(header, process)
  File "mio5_utils.pyx", line 624, in scipy.io.matlab.mio5_utils.VarReader5.array_from_header (scipy/io/matlab/mio5_utils.c:5280)
  File "mio5_utils.pyx", line 669, in scipy.io.matlab.mio5_utils.VarReader5.array_from_header (scipy/io/matlab/mio5_utils.c:4917)
  File "mio5_utils.pyx", line 822, in scipy.io.matlab.mio5_utils.VarReader5.read_cells (scipy/io/matlab/mio5_utils.c:6633)
  File "mio5_utils.pyx", line 622, in scipy.io.matlab.mio5_utils.VarReader5.read_mi_matrix (scipy/io/matlab/mio5_utils.c:4533)
  File "mio5_utils.pyx", line 671, in scipy.io.matlab.mio5_utils.VarReader5.array_from_header (scipy/io/matlab/mio5_utils.c:4940)
  File "mio5_utils.pyx", line 900, in scipy.io.matlab.mio5_utils.VarReader5.read_struct (scipy/io/matlab/mio5_utils.c:7455)
  File "mio5_utils.pyx", line 622, in scipy.io.matlab.mio5_utils.VarReader5.read_mi_matrix (scipy/io/matlab/mio5_utils.c:4533)
  File "mio5_utils.pyx", line 669, in scipy.io.matlab.mio5_utils.VarReader5.array_from_header (scipy/io/matlab/mio5_utils.c:4917)
  File "mio5_utils.pyx", line 822, in scipy.io.matlab.mio5_utils.VarReader5.read_cells (scipy/io/matlab/mio5_utils.c:6633)
  File "mio5_utils.pyx", line 622, in scipy.io.matlab.mio5_utils.VarReader5.read_mi_matrix (scipy/io/matlab/mio5_utils.c:4533)
  File "mio5_utils.pyx", line 653, in scipy.io.matlab.mio5_utils.VarReader5.array_from_header (scipy/io/matlab/mio5_utils.c:4720)
  File "mio5_utils.pyx", line 706, in scipy.io.matlab.mio5_utils.VarReader5.read_real_complex (scipy/io/matlab/mio5_utils.c:5469)
  File "mio5_utils.pyx", line 424, in scipy.io.matlab.mio5_utils.VarReader5.read_numeric (scipy/io/matlab/mio5_utils.c:3303)
  File "mio5_utils.pyx", line 360, in scipy.io.matlab.mio5_utils.VarReader5.read_element (scipy/io/matlab/mio5_utils.c:3032)
  File "streams.pyx", line 181, in scipy.io.matlab.streams.FileStream.read_string (scipy/io/matlab/streams.c:2458)
IOError: could not read bytes
```
#### 解决方案 ####
```
https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.loadmat.html
brew install numpy --with-python3
http://stackoverflow.com/questions/15031694/installing-python-packages-from-local-file-system-folder-with-pip
```
