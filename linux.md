# Linux

## 配置core文件转储路径方法
```sh
cat /proc/sys/kernel/core_pattern

mkdir -p /var/log/oss/cores
chown ossuser:ossgroup /var/log/oss/cores
chmod 777 /var/log/oss/cores
sysctl -w kernel.core_pattern="/var/log/oss/cores/core.%e.%p"
sysctl -w kernel.core_pattern="/var/log/coredumps/core.%e.%p"
mkdir -p /var/log/oss/cores
chown ossuser:ossgroup /var/log/oss/cores
chmod 777 /var/log/oss/cores
sysctl -w kernel.core_pattern="/var/log/oss/cores/core.%e.%p"
```

## 带时间戳拷贝
```sh
cp --preserve=timestamps file file1 # 保留时间戳
cp --preserve=mode file file1       # 保留模式
cp --preserve=ownership file file1  # 保留所有权
cp -p file file1                    # 包括上述三者
```

## Find 查询符号链接
```sh
find . -follow -name "*.so" -print
find . -type f -name "" -exec tar cvf {} ;\
find . -type f -name "" |xargs rm -rf
```

## pgrep
```sh
pgrep {procName}
cat /proc/{procId}/environ | tr '\0' '\n'
```

## 进程启动
```sh
gdb -p `pgrep Nml_ip`
gdb -p `ps -ef | grep update_cipher.pyc | grep -v grep | awk '{print $2}'`
```

## 查看是否有未定义的符号
配置好 LD_LIBRARY_PATH 执行：
```sh
ldd -r libxxx.so
```

## ss 查看 socket 信息
```sh
ss -tip | grep 12788 | grep 32083
```

## zgrep 搜索压缩文件中的内容 
```sh
zgrep "hello world" *.gz
grep "hello world" *.txt
```

## 增加用户
ubuntu
```sh
sudo useradd -g gourpid userName
mkdir /home/userName
sudo passwd userName
```

## 为用户添加sudo权限
ubuntu
```sh
sudo usermod -aG sudo username
```

## 定位进程启动异常的问题，可以用 strace 命令
```sh
strace aaaaa > /tmp/aaa.txt
```
