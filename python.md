# python

## 设置python代理

在文件C:\Users\j00234709\pip\pip.ini中配置如下内容

```ini
[global]
trusted-host=rnd-mirrors.huawei.com
index-url=http://rnd-mirrors.huawei.com/pypi/simple/
```

Linux 下配置文件为：~/.pip/pip.conf

## 设置python使用的第三方插件库

在执行前，设置环境变量PYTHONPATH, 如下：

```bat
set PYTHONHOME=D:\tools\Python27
set PYTHONPATH=D:\Python27\Lib\site-packages
```

## 遍历指定目录下的特定文件，支持过滤某些目录

```python
def get_all_cpp_file(_path, _exclude_dir):
    _target_files = []
    for _root, _dirs, _files in os.walk(_path):
        for _dir in _exclude_dir:
            if _dir in _dirs:
                _dirs.remove(_dir)

        for _file in _files:
            if _file.endswith('.cpp'):
                _target_files.append(_root + os.sep + _file)
    return _target_files
```

## 命令行参数处理

```python
import getopt

_opts, _args = getopt.getopt(sys.argv[1:], "hd:", ['help', 'domain='])

for _op, _value in _opts:
    if _op in ('-h', '--help'):
        _is_help = True
    elif _op in ('-d', '--domain'):
        _domain = _value
```

## 日志模块logging的使用

```python
import logging
import logging.config

logging.config.fileConfig("./conf/xgen_logging.conf")
logger = logging.getLogger('root')
```

## 读取json

```python
with open('conf/build_dir.json', 'r') as _fs:
    _build_dirs = json.load(_fs)

if '_build_dirs' in dir():
    return _build_dirs, None
```

## 获取当前时间

```python
import time
cur_time = time.strftime('%Y%m%d-%H%M%S')
```

## 递归创建目录

递归创建目录

```python
import os
out_dir = '/opt/oss/rtsp/xdao'
if not os.path.makedirs(out_dir):
    os.makedirs(out_dir)
```

创建目录

```python
import os
out_dir = '/opt/oss/rtsp/xdao'
if not os.path.makedirs(out_dir):
    os.mkdir(out_dir)
```

## 正则处理

```python
import re
_pattern = re.compile("const[\s]*([a-zA-Z0-9<> :*,_]+)[\s]*[*&]?")
_code = 'xxxxxx'
_matcher = _pattern.match(_code)
if _matcher:
    print 'match'
```

## 解压 gz

gz：即gzip。通常仅仅能压缩一个文件。

```python
import gzip

def un_gzip(_gz_file):
    _f_name = _gz_file.replace('.gz', '')
    _g_file = gzip.GzipFile(_gz_file)
    with open(_f_name, 'w+') as _fs:
        _fs.write(_g_file.read())
    _g_file.close()
```

## 解压 tar

xxx.tar.gz 解压后得到 xxx.tar，还要进一步解压出来。  
注：tgz 与 tar.gz 是同样的格式，老版本号 DOS 扩展名最多三个字符，故用 tgz 表示。  
因为这里有多个文件，我们先读取全部文件名称。然后解压。例如以下：  
注：tgz 文件与tar文件同样的解压方法。  

```python
import tarfile

def un_tar(file_name):
    # untar zip file"""
    tar = tarfile.open(file_name)
    names = tar.getnames()
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    #因为解压后是很多文件，预先建立同名目录
    for name in names:
        tar.extract(name, file_name + "_files/")
    tar.close()
```

## 解压 zip

与 tar 类似，先读取多个文件名称，然后解压。例如以下  

```python
import zipfile

def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names,file_name + "_files/")
    zip_file.close()
```

## 迭代器的使用

```python
class MKProject:
    def __init__(self):
        self.files = ['1.cpp', '2.cpp', '3.cpp']
        self.pos = 0

    def __iter__(self):
        return self

    def next(self):
        if self.pos >= len(self.files):
            raise StopIteration
        self.pos += 1
        return 'compile->', self.files[self.pos - 1]

if __name__ == '__main__':
    mk_proj = MKProject()
    for proj in mk_proj:
        print proj[0], proj[1]
```

在 python 3.* 里用 `__next__` 方法

## yield 的使用

```python
def test_yield():
    _pics = ['1.png', '2.png', '3.png', '4.png', '5.png']
    for _pic in _pics:
        yield _pic

if __name__ == '__main__':
    for pic in test_yield():
        print pic
```

## virtualenv

### 安装

```shell
pip3 install virtualenv
```

### 创建 virualenv

第一步，创建目录

```shell
mkdir myproject
cd myproject/
```

第二步，创建一个独立的Python运行环境，命名为 `venv`

```shell
virtualenv --no-site-packages venv
```

命令 `virtualenv` 就可以创建一个独立的 Python 运行环境，我们还加上了参数 --no-site-packages，这样，已经安装到系统 Python 环境中的所有第三方包都不会复制过来，这样，我们就得到了一个不带任何第三方包的“干净”的 Python 运行环境。

参数 --no-site-packages 现在已经 DEPRECATED，不适用全局的 site-package 现在是默认行为了。

```shell
virtualenv venv
```

创建指定解释器的 virtualenv：

```shell
virtualenv --python=python2.7 venv
```

新建的 Python 环境被放到当前目录下的 venv 目录。有了 venv 这个 Python 环境，可以用 source 进入该环境：

```shell
Mac:myproject michael$ source venv/bin/activate
(venv)Mac:myproject michael$
```

注意到命令提示符变了，有个(venv)前缀，表示当前环境是一个名为 venv 的 Python环境。

退出当前的 venv 环境，使用 deactivate 命令：

```shell
(venv)Mac:myproject michael$ deactivate
Mac:myproject michael$
```

此时就回到了正常的环境，现在 pip 或 python 均是在系统 Python 环境下执行。

### 导出 vietualenv 中的依赖包

```shell
pip freeze > requirements.txt
```

```shell
pip install -r requirements.txt
```

### 删除一个虚拟环境

要删除一个虚拟环境，只需删除它的文件夹。（执行 rm -rf venv ）。

## virtualenvwrapper

鉴于virtualenv不便于对虚拟环境集中管理，所以推荐直接使用virtualenvwrapper。 virtualenvwrapper提供了一系列命令使得和虚拟环境工作变得便利。它把你所有的虚拟环境都放在一个地方。

### 安装virtualenvwrapper(确保virtualenv已安装)

```shell
pip install virtualenvwrapper
pip install virtualenvwrapper-win　　#Windows使用该命令
```

### 安装完成后，在~/.bashrc写入以下内容

```shell
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh
```

第一行：virtualenvwrapper存放虚拟环境目录  
第二行：virtrualenvwrapper会安装到python的bin目录下，所以该路径是python安装目录下bin/virtualenvwrapper.sh

```shell
source ~/.bashrc　　　　#读入配置文件，立即生效
```

#### virtualenvwrapper基本使用

创建虚拟环境　mkvirtualenv

```shell
mkvirtualenv venv
```

这样会在 WORKON_HOME 变量指定的目录下新建名为 venv 的虚拟环境。

若想指定 python 版本，可通过 "--python" 指定 python 解释器

```shell
mkvirtualenv --python=/usr/local/python3.5.3/bin/python venv
```

基本命令

查看当前的虚拟环境目录

```shell
[root@localhost ~]# workon
```

切换到虚拟环境

```shll
[root@localhost ~]# workon py3
```

退出虚拟环境

```shell
(py3) [root@localhost ~]# deactivate
[root@localhost ~]#
```

删除虚拟环境

```shll
rmvirtualenv venv
```
