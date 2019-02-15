# Go Channel

channel用于主进程、协程之间的通信。

## channel 关闭原则
- 不要在消费端关闭 channel
- 不要在有多个并行的生产者时对 channel 执行关闭操作

## 同步模式
channel 默认为同步模式，即不创建缓冲区，发送和接收需要一一配对，不然发送方会被一直阻塞，直到数据被接收。需要注意的是，同步的 channel 不能在一个协程中发送&接收，因为会被阻塞而永远跑不到接收的语句。一个最简单的例子：
```go
package main

import "fmt"

func main() {
    data := make(chan int)

    go func() {
        for d := range data {//通过 range 不断地处理 data
            fmt.Println(d)
        }
    }()
    
    data <- 1//发送要放在接收协程跑起来后面，因为发送后会阻塞等待接收
    data <- 2
    data <- 3
    close(data)
}
```

或者用下面这种方法接收 channel，如果 !ok 说明 data 被 close：
```go
go func() {
    for {
        if d, ok := <-data; ok {
            fmt.Println(d)
        }
    }

}()
```

## 异步模式
异步模式 channel 有缓冲区，如果缓冲区已满，发送的主进程或者协程会被阻塞，如果未满不会被阻塞，如果为空，接收的协程会被阻塞。基于这种性质往往需要有个同步 channel 去控制主进程是否退出，否则有可能协程还未处理完所有的信息，主进程已经退出。另外需要注意的是，异步的 channel 用完要 close，不然处理这个的 channel 会被阻塞，形成死锁。
```go
package main

import "fmt"

func main() {
    data := make(chan int, 3)
    canQuit := make(chan bool) //阻塞主进程，防止未处理完就退出

    go func() {
        for d := range data {//如果 data 的缓冲区为空，这个协程会一直阻塞，除非被 channel 被 close
            fmt.Println(d)
        }
        canQuit <- true
    }()

    data <- 1
    data <- 2
    data <- 3
    data <- 4
    data <- 5
    close(data) //用完需要关闭，否则 goroutine会被死锁
    <-canQuit //解除阻塞
}
```

## select 的使用
其实，实际项目中通常这样用 channel。
```go
package main

import "fmt"
import "time"
import "os"

const (
    MAX_REQUEST_NUM = 10
    CMD_USER_POS    = 1
)

var (
    save chan bool
    quit chan bool
    req  chan *Request
)

type Request struct {
    CmdID int16
    Data  interface{}
}

type UserPos struct {
    X int16
    Y int16
}

func main() {
    newReq := Request{
        CmdID: CMD_USER_POS,
        Data: UserPos{
            X: 10,
            Y: 20,
        },
    }
    go handler()

    req <- &newReq

    time.Sleep(2000 * time.Millisecond)

    save <- true
    close(req)

    <-quit
}

func handler() {
    for {
        select {
        case <-save:
            saveGame()
        case r, ok := <-req:
            if ok {
                onReq(r)
            } else {
                fmt.Println("req chan closed.")
                os.Exit(0)
            }
        }
    }
}

func init() {
    req = make(chan *Request, MAX_REQUEST_NUM)
    save = make(chan bool)
    quit = make(chan bool)
}

func saveGame() {
    fmt.Printf("Do Something With Save Game.\n")
    quit <- true
}

func onReq(r *Request) {
    pos := r.Data.(UserPos)
    fmt.Println(r.CmdID, pos)
}
```
