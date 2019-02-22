## gdb常用命令

## 基本操作
- 附加进程：dbg attach pid  - 查看源码: list src
- 断点： break
- 删除断点: delte break_num|range
	delete 5
	delete 1-10
- 继续执行： continue

## 打开 c++filter 
```sh
set print asm-demangle on
```

## 让 p 输出字符串时不截断
```sh
set print repeats 0
```

`gdb` 用 `p` 看一个字符串的时候默认显示是截断的，可以通过 `set print element 0` 命令显示完整的字符串

## 查看所有线程的堆栈
```sh
> thread apply all bt
```

## 将GDB中的输出定向到文件
方法一：适合临时向文件输出些信息的情况。
比如要用info functions输出所有函数，结果往往有一大坨，所以可以将之输出到文件。
```sh
(gdb) set logging file <file name>
(gdb) set logging on
(gdb) info functions
(gdb) set logging off
```

方法二：适合整个gdb会话期间都重定向输出的情况
```sh
gdb |tee newfile
```

## 符号
编译的时候要带 -g 参数
- objcopy
- objdump

### 加载符号
跟so 文件放在同一个目录
info share
显示， 不带 * 的表示 符号表加载成功
add-symblic-file *.dbg address

### 输出日志
拷贝 Debug 信息
```sh
objcopy --only-keep-debug /usr/lib/release/libxx.so /usr/lib/pdb/xxxx.dbg
```

剥离 Debug 信息
```sh
objcopy --strip-debug /opt/server/lib/release/libxxx.so
```

合并 Debug 信息
```sh
objcopy --add-gnu-debuglink=/opt/build/server/pdb/xxxx.dbg /opt/build/server/lib/release/libxx.so
```

