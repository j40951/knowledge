# Docker

## 配置 Docker 仓库镜像

DOCKER_OPTS="--insecure-registry rnd-dockerhub.hotmall.com"
export NO_PROXY="rnd-dockerhub.hotmall.com"

## ubuntu 重启 Docker

```shell
service docker restart
```

## 搜索镜像

```shell
docker search  rnd-dockerhub.hotmall.com/official/
docker search  rnd-dockerhub.hotmall.com/library/
```

rnd-dockerhub.hotmall.com/official/：用于和docker hub官网的镜像进行定期同步  
rnd-dockerhub.hotmall.com/library/ : 为公司内源镜像库，普通用户也无权限上传个人镜像.  

## 创建最小的Go docker 镜像

### 一个简单 Go 程序的镜像

#### 一、首先让我们创建一个很简单的Go程序:

```go
package main
import "fmt"
func main() {
    fmt.Println("hello world")
}
```

运行下面的命令编译:

```shell
GOOS=linux CGO_ENABLED=0 go build -ldflags="-s -w" -o app app.go && tar c app
```

`-s` 忽略符号表和调试信息，`-w`忽略DWARF符号表，通过这两个参数，可以进一步减少编译的程序的尺寸，更多的参数可以参考 go link, 或者 go tool link -help(另一个有用的命令是 go tool compile -help)。

你也可以使用strip工具对编译的Go程序进行裁剪。

本身 `Go` 是静态编译的， 对于 `CGO`, 如果设置 `CGO_ENABLED=0`，则完全静态编译，不会再依赖动态库。

如果设置CGO_ENABLED=0,并且你的代码中使用了标准库的net包的话，有可能编译好的镜像无法运行，报sh: /app: not found的错误，尽管/app这个文件实际存在，并且如果讲基础镜像换为centos或者ubuntu的话就能执行。这是一个奇怪的错误，原因在于：

> 默认情况下 `net` 包会使用静态链接库， 比如 libc

知道了原因，解决办法也很简单，就是完全静态链接或者在基础镜像中加入libc库。

下面是几种解决办法：

- 设置 `CGO_ENABLED=0`
- 编译是使用纯go的net: `go build -tags netgo -a -v`
- 使用基础镜像加 glibc(或等价库 musl、uclibc)， 比如 busybox:glibc、alpine + RUN apk add --no-cache libc6-compat、frolvlad/alpine-glibc

#### 二、新建 Dockerfile

```dockfile
FROM scratch
ADD app /
CMD ["/app"]
```

运行下面的命令创建一个镜像:

```shell
docker build -t app2 .
```

### 其他基础镜像

- scratch: 空的基础镜像，最小的基础镜像
- busybox: 带一些常用的工具，方便调试， 以及它的一些扩展busybox:glibc
- alpine: 另一个常用的基础镜像，带包管理功能，方便下载其它依赖的包

显然。 你应该只在编译阶段使用 [Go](https://hub.docker.com/_/golang/) 的镜像，这样才能将你的镜像减小到最小。
