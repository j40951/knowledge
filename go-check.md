# gocheck框架使用

gocheck 作为 golang 的一种测试框架，可以直接继承 go test 使用，他允许之前基于 testing 框架的测试平滑迁移到 gocheck 框架而不会发生冲突，gocheck API 与 testing 也有很多相似的地方

[gocheck 官网](http://labix.org/gocheck)

## 安装运行

```shell
go get -u gopkg.in/check.v1
```

### 例子

```go
package hello_test

import (
    "testing"
    "io"
    "fmt"
    "strconv"
    . "gopkg.in/check.v1"
)

var a int =1

// Hook up gocheck into the "go test" runner.
func Test(t *testing.T) { TestingT(t) }

type MySuite struct{}

var _ = Suite(&MySuite{})


func (s *MySuite) SetUpSuite(c *C) {
    str3:="第1次套件开始执行"
    fmt.Println(str3)

}

func (s *MySuite) TearDownSuite(c *C) {
    str4:="第1次套件执行完成"
    fmt.Println(str4)
}

func (s *MySuite) SetUpTest(c *C) {
    str1:="第"+strconv.Itoa(a)+"条用例开始执行"
    fmt.Println(str1)

}

func (s *MySuite) TearDownTest(c *C) {
    str2:="第"+strconv.Itoa(a)+"条用例执行完成"
    fmt.Println(str2)
    a=a+1
}

func (s *MySuite) TestHelloWorld(c *C) {
    c.Assert(42, Equals, 42)
    c.Assert(io.ErrClosedPipe, ErrorMatches, "io: .*on closed pipe")
    c.Check(42, Equals, 42)
}

func (s *MySuite) TestHelloTerry(c *C) {
    c.Assert("terry", Equals, "terry")
    c.Assert(io.ErrClosedPipe, ErrorMatches, "io: .*on closed pipe")
    c.Check(42, Equals, 42)
}
```

最后输出的结果为

```shell
E:\\go_project>go test
第1次套件开始执行
第1条用例开始执行
第1条用例执行完成
第2条用例开始执行
第2条用例执行完成
第1次套件执行完成
OK: 2 passed
PASS
ok      _/E_/go_project 0.502s
```

### 前置后置操作

除了最基本的结构，当然少不得我们熟悉的测试用例前置后置操作，用于满足用例执行前的准备，以及执行完成后清理环境等方法

```go
func (s *SuiteType) SetUpSuite(c *C)        // 在测试套件启动前执行一次
func (s *SuiteType) SetUpTest(c *C)         // 在每个用例执行前执行一次
func (s *SuiteType) TearDownTest(c *C)      // 在每个用例执行后执行一次
func (s *SuiteType) TearDownSuite(c *C)     // 在测试套件用例都执行完成后执行一次
```

### 选择执行指定用例

- 当然我们在执行用例的时候未必需要全部执行，那就需要通过一些选择性的API来选择部分用例执行，如跳过用例或用例套件使用skip

```go
func (s *MySuite) SetUpSuite(c *C) {
    str3:="第1次套件开始执行"
    fmt.Println(str3)
    c.Skip("Skip TestSutie")  //在测试套件启动前跳过整个测试套件的用例
}
//其余代码参考上文
```

- 如果在跳过套件中的测试用例

```go
func (s *MySuite) TestHelloWorld(c *C) {
    c.Skip("Skip TestCase")  //跳过当前测试用例
    c.Assert(42, Equals, 42)
    c.Assert(io.ErrClosedPipe, ErrorMatches, "io: .*on closed pipe")
    c.Check(42, Equals, 42)
}
```

- 除了跳过还有选择测试用例执行

```shell
go test -check.f MyTestSuite                    //选择测试套件
go test -check.f "Test.*Works"                  //选择测试方法
go test -check.f "MyTestSuite.Test.*Works"      //选择套件中的方法
```

## Checker

```go
// Commentf returns an infomational value to use with Assert or Check calls.
// If the checker test fails, the provided arguments will be passed to
// fmt.Sprintf, and will be presented next to the logged failure.
//
// For example:
//
//     c.Assert(v, Equals, 42, Commentf("Iteration #%d failed.", i))
//
// Note that if the comment is constant, a better option is to
// simply use a normal comment right above or next to the line, as
// it will also get printed with any errors:
//
//     c.Assert(l, Equals, 8192) // Ensure buffer size is correct (bug #123)
//
```

Commentf

```go
// The Not checker inverts the logic of the provided checker.  The
// resulting checker will succeed where the original one failed, and
// vice-versa.
//
// For example:
//
//     c.Assert(a, Not(Equals), b)
//
```

Not

```go
// The IsNil checker tests whether the obtained value is nil.
//
// For example:
//
//    c.Assert(err, IsNil)
//
```

IsNil

```go
// The NotNil checker verifies that the obtained value is not nil.
//
// For example:
//
//     c.Assert(iface, NotNil)
//
// This is an alias for Not(IsNil), made available since it's a
// fairly common check.
//
```

NotNil

```go
// The Equals checker verifies that the obtained value is equal to
// the expected value, according to usual Go semantics for ==.
//
// For example:
//
//     c.Assert(value, Equals, 42)
//
```

Equals

```go
// The DeepEquals checker verifies that the obtained value is deep-equal to
// the expected value.  The check will work correctly even when facing
// slices, interfaces, and values of different types (which always fail
// the test).
//
// For example:
//
//     c.Assert(value, DeepEquals, 42)
//     c.Assert(array, DeepEquals, []string{"hi", "there"})
//
```

DeepEquals

```go
// The HasLen checker verifies that the obtained value has the
// provided length. In many cases this is superior to using Equals
// in conjunction with the len function because in case the check
// fails the value itself will be printed, instead of its length,
// providing more details for figuring the problem.
//
// For example:
//
//     c.Assert(list, HasLen, 5)
//
```

HasLen

```go
// The ErrorMatches checker verifies that the error value
// is non nil and matches the regular expression provided.
//
// For example:
//
//     c.Assert(err, ErrorMatches, "perm.*denied")
//
```

ErrorMatches

```go
// The Matches checker verifies that the string provided as the obtained
// value (or the string resulting from obtained.String()) matches the
// regular expression provided.
//
// For example:
//
//     c.Assert(err, Matches, "perm.*denied")
//
```

Matches

```go
// The Panics checker verifies that calling the provided zero-argument
// function will cause a panic which is deep-equal to the provided value.
//
// For example:
//
//     c.Assert(func() { f(1, 2) }, Panics, &SomeErrorType{"BOOM"}).
//
//
```

Panics

```go
// The PanicMatches checker verifies that calling the provided zero-argument
// function will cause a panic with an error value matching
// the regular expression provided.
//
// For example:
//
//     c.Assert(func() { f(1, 2) }, PanicMatches, `open.*: no such file or directory`).
//
//
```

PanicMatches

```go
// The FitsTypeOf checker verifies that the obtained value is
// assignable to a variable with the same type as the provided
// sample value.
//
// For example:
//
//     c.Assert(value, FitsTypeOf, int64(0))
//     c.Assert(value, FitsTypeOf, os.Error(nil))
//
```

FitsTypeOf

```go
// The Implements checker verifies that the obtained value
// implements the interface specified via a pointer to an interface
// variable.
//
// For example:
//
//     var e os.Error
//     c.Assert(err, Implements, &e)
//
```

Implements
