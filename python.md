# python

## 设置python代理
在文件C:\Users\j00234709\pip\pip.ini中配置如下内容
```
[global]
trusted-host=rnd-mirrors.huawei.com
index-url=http://rnd-mirrors.huawei.com/pypi/simple/
```
## 设置python使用的第三方插件库
在执行前，设置环境变量PYTHONPATH, 如下：
```
set PYTHONPATH=D:\Python27\Lib\site-packages
```

## logging 模块使用
```
import logging
import logging.config

logging.config.fileConfig("./conf/my_logging.conf")
logger = logging.getLogger('root')
```

conf/my_logging.conf 内容
```
[loggers]
keys=root

[logger_root]
level=DEBUG
handlers=hand01,hand02

[handlers]
keys=hand01,hand02

[handler_hand01]
class=StreamHandler
level=INFO
formatter=form02
args=(sys.stdout,)

[handler_hand02]
class=handlers.RotatingFileHandler
level=DEBUG
formatter=form01
args=('log/push_cpp.log', 'a', 50*1024*1024, 5)

[formatters]
keys=form01,form02

[formatter_form01]
format=%(asctime)s %(filename)s[%(lineno)d] %(levelname)s %(message)s

[formatter_form02]
format=%(asctime)s %(filename)s[%(lineno)d] %(levelname)s %(message)s
```
