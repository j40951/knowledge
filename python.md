# python

## 设置python代理
在文件C:\Users\j00234709\pip\pip.ini中配置如下内容
```ini
[global]
trusted-host=rnd-mirrors.huawei.com
index-url=http://rnd-mirrors.huawei.com/pypi/simple/
```

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
