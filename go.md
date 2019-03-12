go
=

## 命令行编译
```sh
go build -v $(go list ./... | grep -v '/vendor/')
```

## 开启 go 编译时的逃逸分析日志

开启逃逸分析日志很简单，只要在编译的时候加上`-gcflags '-m'`，但是我们为了不让编译时自动内连函数，一般会加`-l`参数，最终为`-gcflags '-m -l'`

Example:
```go
package main

import (
    "fmt"
)

func main() {
    s := "hello"
    fmt.Println(s)
}
```

```sh
go build -gcflags '-m' escape.go
go run -gcflags '-m -l' escape.go
```

Output:
```sh
# command-line-arguments
escape_analysis/main.go:9: s escapes to heap
escape_analysis/main.go:9: main ... argument does not escape
```

## Websocket
[百万级 WebSockets 和 Go 语言](https://colobu.com/2017/12/13/A-Million-WebSockets-and-Go/)

## Go Generate
go generate命令使用格式如下：
```sh
go generate [-run regexp] [-n] [-v] [-x] [build flags] [file.go... | packages]
```
其中：
- -run 正则表达式匹配命令行，仅执行匹配的命令
- -v 输出被处理的包名和源文件名
- -n 显示不执行命令
- -x 显示并执行命令

执行go generate时，有一些环境变量可以使用:
```sh
$GOARCH
    体系架构 (arm、amd64等待)
$GOOS
    OS环境(linux、windows等)
$GOFILE
    当前处理中的文件名
$GOLINE
    当前命令在文件中的行号
$GOPACKAGE
    当前处理文件的包名
$DOLAR
    固定的"$",不清楚用途
``` 
假设我们有个main.go文件，内容如下：
```go
package main

import "fmt"

//go:generate echo hello
//go:generate go run main.go
//go:generate  echo file=$GOFILE pkg=$GOPACKAGE
func main() {
    fmt.Println("main func")
}
```

执行“go generate”后，输出如下：
```sh
$ go generate
hello
main func
file=main.go pkg=main
```

## net/http 使用
[golang http client 连接池](http://oohcode.com/2018/06/01/golang-http-client-connection-pool/)

### 参考
[go generate介绍](https://www.jianshu.com/p/a866147021da)