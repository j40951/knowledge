# vi

## 查找命令

```shell
/pattern<Enter>  #向下查找pattern匹配字符串
?pattern<Enter>  #向上查找pattern匹配字符串
```

使用了查找命令之后，使用如下两个键快速查找：  
n：按照同一方向继续查找  
N：按照反方向查找  

## 字符串匹配

pattern 是需要匹配的字符串，例如：

```shell
/abc<Enter>      #查找abc
/ abc <Enter>    #查找abc单词（注意前后的空格）
```
  
除此之外，pattern 还可以使用一些特殊字符，包括（/、^、$、*、.），其中前三个是 vi 与 vim 通用的，“/” 为转义字符。  

```shell
/^abc<Enter>      #查找以abc开始的行
/test$<Enter>     #查找以abc结束的行
//^test<Enter>    #查找^tabc字符串
```
  
## 基本替换

```shell
:s/vivian/sky/         #替换当前行第一个 vivian 为 sky
:s/vivian/sky/g        #替换当前行所有 vivian 为 sky
:n,$s/vivian/sky/      #替换第 n 行开始到最后一行中每一行的第一个 vivian 为 sky
:n,$s/vivian/sky/g     #替换第 n 行开始到最后一行中每一行所有 vivian 为 sky
```

n 为数字，若 n 为 .，表示从当前行开始到最后一行

```shell
:%s/vivian/sky/        #（等同于 :g/vivian/s//sky/） 替换每一行的第一个 vivian 为 sky
:%s/vivian/sky/g       #（等同于 :g/vivian/s//sky/g） 替换每一行中所有 vivian 为 sky
```
