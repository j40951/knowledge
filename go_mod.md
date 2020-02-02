# Go Mod

## Usage

### 1. 安装Go 1.13

### 2. 配置环境变量

```ini
#打开 Go modules
go env -w GO111MODULE=on
#设置 GOPROXY
go env -w GOPROXY=https://goproxy.cn,direct
```

go env -w： Go1.13 新增了 go env -w 用于写入环境变量，而写入的地方是 os.UserConfigDir 所返回的路径，需要注意的是 go env -w 不会覆写。需要指出，它不会覆盖系统环境变量。

GO111MODULE：

这个环境变量主要是 Go modules 的开关，主要有以下参数：

- auto：只在项目包含了 go.mod 文件时启用 Go modules，在 Go 1.13 中仍然是默认值，详见 ：golang.org/issue/31857。
- on：无脑启用 Go modules，推荐设置，未来版本中的默认值，让 GOPATH 从此成为历史。
- off：禁用 Go modules。

GOPROXY：

这个环境变量主要是用于设置 Go 模块代理，它的值是一个以英文逗号 “,” 分割的 Go module proxy 列表，默认是proxy.golang.org，国内访问不了。这里要感谢盛傲飞和七牛云为中国乃至全世界的 Go 语言开发者提供免费、可靠的、持续在线的且经过CDN加速Go module proxy（goproxy.cn）。

其实值列表中的 “direct” 为特殊指示符，用于指示 Go 回源到模块版本的源地址去抓取(比如 GitHub 等)，当值列表中上一个 Go module proxy 返回 404 或 410 错误时，Go 自动尝试列表中的下一个，遇见 “direct” 时回源，遇见 EOF 时终止并抛出类似 “invalid version: unknown revision...” 的错误。

### 3. 创建你的项目

这里我们在 $GOPATH/src 外，创建 /var/www/demo实例

```shell
mkdir /var/www/demo
cd  /var/www/demo
```

新建main.go

```go
package main

import (
    "github.com/gin-gonic/gin"
    "fmt"
)

func main() {
    r := gin.Default()
    r.GET("/ping", func(c *gin.Context) {
        fmt.Println("hello world!")
        c.JSON(200, gin.H{
            "message": "pong",
        })
    })
    r.Run() // listen and serve on 0.0.0.0:8080
}
```

### 4. 在/var/www/demo根目录下

```shell
#生成go.mod文件
go mod init  demo
```

打开go.mod文件，内容

```shell
module demo

go 1.13
```

go.mod 是启用了 Go moduels 的项目所必须的最重要的文件，它描述了当前项目（也就是当前模块）的元信息，每一行都以一个动词开头，目前有以下 5 个动词:

- module：用于定义当前项目的模块路径。
- go：用于设置预期的 Go 版本。
- require：用于设置一个特定的模块版本。
- exclude：用于从使用中排除一个特定的模块版本。
- replace：用于将一个模块版本替换为另外一个模块版本。

这里的填写格式基本为包引用路径+版本号，另外比较特殊的是 go $version，目前从 Go1.13 的代码里来看，还只是个标识作用，暂时未知未来是否有更大的作用。

### 5. 在/var/www/demo根目录下，执行 go build

```shell
go build
```

## 更换依赖版本

查看gin所有历史版本

```shell
go list -m -versions github.com/gin-gonic/gin
```

如果想更换依赖版本，比如v1.3.0，怎么办？

只需执行如下命令

```shell
go mod edit -require="github.com/gin-gonic/gin@v1.3.0"
go tidy #更新现有依赖
```

@后跟版本号，这个时候go.mod已经修改好了

```shell
require github.com/gin-gonic/gin v1.3.0
```

查看所有项目依赖的包

```shll
go list -m all
```

```shell
github.com/davecgh/go-spew v1.1.0
github.com/gin-contrib/sse v0.0.0-20190301062529-5545eab6dad3
github.com/gin-gonic/gin v1.4.0
github.com/golang/protobuf v1.3.1
github.com/json-iterator/go v1.1.6
github.com/mattn/go-isatty v0.0.7
github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd
github.com/modern-go/reflect2 v1.0.1
github.com/pmezard/go-difflib v1.0.0
github.com/stretchr/objx v0.1.0
github.com/stretchr/testify v1.3.0
github.com/ugorji/go v1.1.4
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2
golang.org/x/net v0.0.0-20190503192946-f4e77d36d62c
golang.org/x/sys v0.0.0-20190222072716-a9d3bda3a223
golang.org/x/text v0.3.0
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405
gopkg.in/go-playground/assert.v1 v1.2.1
gopkg.in/go-playground/validator.v8 v8.18.2
gopkg.in/yaml.v2 v2.2.2
```

## 参考
[Go 依赖管理工具 Go Modules](https://segmentfault.com/a/1190000020543746)
