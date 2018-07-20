## dbg常用命令

dbg attach pid

断点： break
继续执行： continue
打开 c++filter: 
set print asm-demangle on

### 符号
编译的时候要带 -g 参数
objcopy
objdump

### 加载符号
跟so 文件放在同一个目录
info share
显示， 不带 * 的表示 符号表加载成功
add-symblic-file *.dbg address
