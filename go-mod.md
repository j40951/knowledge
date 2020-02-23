# Go mod

## go mod 命令

golang 提供了 go mod命令来管理包。

go mod 有以下命令：

| 命令     | 说明                                                                 |
|:---------|:-------------------------------------------------------------------|
| download | download modules to local cache（下载依赖包）                          |
| edit     | edit go.mod from tools or scripts（编辑go.mod）                        |
| graph    | print module requirement graph （打印模块依赖图）                      |
| init     | initialize new module in current directory（在当前目录初始化mod）      |
| tidy     | add missing and remove unused modules（拉取缺少的模块，移除不用的模块） |
| vendor   | make vendored copy of dependencies（将依赖复制到vendor下）             |
| verify   | verify dependencies have expected content （验证依赖是否正确）         |
| why      | explain why packages or modules are needed（解释为什么需要依赖）       |

go get 升级

- 运行 go get -u 将会升级到最新的次要版本或者修订版本（x.y.z, z是修订版本号， y是次要版本号）
- 运行 go get -u=patch 将会升级到最新的修订版本
- 运行 go get package@version 将会升级到指定的版本号 version
- 运行 go get 如果有版本的更改，那么 go.mod 文件也会更改

go.mod 提供了module, require、replace 和 exclude 四个命令

- module 语句指定包的名字（路径）
- require 语句指定的依赖项模块
- replace 语句可以替换依赖项模块
- exclude 语句可以忽略依赖项模块

## 如何在项目中使用

### 新建项目

在 GOPATH 目录之外新建一个目录，并使用 `go mod init modulename` 初始化生成 go.mod 文件

```shell
> mkdir hello
> cd hello
hello> go mod init hello
go: creating new go.mod: module hello
hello> ls
go.mod
hello> cat go.mod
module hello

go 1.13
```

> go.mod 文件一旦创建后，它的内容将会被 go toolchain 全面掌控。go toolchain 会在各类命令执行时，比如 go get、go build、go mod 等修改和维护 go.mod 文件。

go module 安装 package 的原則是先拉最新的 release tag，若无tag则拉最新的commit，go 会自动生成一个 go.sum 文件来记录 dependency tree。

### 改造现有项目

server.go 源码为：

```go
package main

import (
    api "./api"
    "github.com/labstack/echo"
)

func main() {
    e := echo.New()
    e.GET("/", api.HelloWorld)
    e.Logger.Fatal(e.Start(":1323"))
}
```

使用 go mod init *** 初始化go.mod

```shell
$ go mod init helloworld
go: creating new go.mod: module helloworld
```

运行 go run server.go

```shell
go: finding github.com/labstack/gommon/color latest
go: finding github.com/labstack/gommon/log latest
go: finding golang.org/x/crypto/acme/autocert latest
go: finding golang.org/x/crypto/acme latest
go: finding golang.org/x/crypto latest
build command-line-arguments: cannot find module for path _/home/gs/helloworld/api
```

首先还是会查找并下载安装依赖，然后运行脚本 server.go，这里会抛出一个错误：

```shell
build command-line-arguments: cannot find module for path _/home/gs/helloworld/api
```

但是go.mod 已经更新：

```shell
$ cat go.mod
module helloworld

go 1.13

require (
        github.com/labstack/echo v3.3.10+incompatible // indirect
        github.com/labstack/gommon v0.2.8 // indirect
        github.com/mattn/go-colorable v0.1.1 // indirect
        github.com/mattn/go-isatty v0.0.7 // indirect
        github.com/valyala/fasttemplate v1.0.0 // indirect
        golang.org/x/crypto v0.0.0-20190313024323-a1f597ede03a // indirect
)
```

这是因为 server.go 中使用 internal package 的方法跟以前已经不同了，由于 go.mod会扫描同工作目录下所有 package 并且变更引入方法，必须将 helloworld当成路径的前缀，也就是需要写成 import helloworld/api，以往 GOPATH/dep 模式允许的 import ./api 已经失效。

server.go 修改如下：

```go
package main

import (
    api "helloworld/api"
    "github.com/labstack/echo"
)

func main() {
    e := echo.New()
    e.GET("/", api.HelloWorld)
    e.Logger.Fatal(e.Start(":1323"))
}
```

## 使用 replace 替换无法直接获取的 package

由于某些已知的原因，并不是所有的package都能成功下载，比如：golang.org下的包。

modules 可以通过在 go.mod 文件中使用 replace 指令替换成github上对应的库，比如：

```shell
replace (
    golang.org/x/crypto v0.0.0-20190313024323-a1f597ede03a => github.com/golang/crypto v0.0.0-20190313024323-a1f597ede03a
)
```

## How do I migrate from dep to Go Modules

Migrating from Dep to Go Modules is very easy.

1. Run `go version` and make sure you're using version 11 or later.
2. Move your code outside of GOPATH or set export GO111MODULE=on.
3. `go mod init [module path]`: This will import dependencies from Gopkg.lock.
4. `go mod tidy`: This will remove unnecessary imports, and add indirect ones.
5. `rm -rf vendor/`: Optional step to delete your vendor folder.
6. `go build`: Do a test build to see if it works.
7. `rm -f Gopkg.lock Gopkg.toml`: Delete the obsolete files used for Dep.

Go has imported my dependencies from Dep by reading the Gopkg.lock file and also created a go.mod file.

If you want to keep your vendor folder:

- Run go mod vendor to copy your dependencies into the vendor folder.
- Run go build -mod=vendor to ensure go build uses your vendor folder.

## 将私有仓库用作 module 依赖

使用 `GOPRIVATE` 环境变量

```shell
go env -w GOPRIVATE="gitlab.com/xxx"
```

它可以声明指定域名为私有仓库，`go get` 在处理该域名下的所有依赖时，会直接跳过 `GOPROXY` 和 `CHECKSUM` 等逻辑。

另外域名 `gitlab.com/xxx` 非常灵活，它默认是前缀匹配的，所有的 `gitlab.com/xxx` 前缀的依赖模块都会被视为 `private-modules`，它对于企业、私有 Group 等有着一劳永逸的益处。

提示：如果你通过 `ssh` 公钥访问私有仓库，记得配置 `git` 拉取私有仓库时使用 `ssh` 而非 `https`

可以通过命令git config ...的方式来配置

```shell
git config --global url."git@gitlab.com:xxx/zz.git".insteadof "https://gitlab.com/xxx/zz.git"
```

也可以直接修改 `~/.gitconfig` 添加如下配置：

```ini
[url "git@github.com:"]
    insteadOf = https://github.com/
[url "git@gitlab.com:"]
    insteadOf = https://gitlab.com/
```

即可强制 `go get` 针对 `github.com` 与 `gitlab.com` 使用 `ssh` 而非 `https`。
