# GTest

## 编译
下载 gtest 代码，编译得到如下两个 lib 库
- gtest.lib
- gtest_main.lib

## Quick Start
待测函数
```c++
int g_count = 0;

int Foo(int a, int b)
{
	g_count ++;
	std::cout << "g_count=" << g_count << std::endl;

    if (a == 0 || b == 0)
    {
        throw "don't do that";
    }
    int c = a % b;
    if (c == 0)
        return b;
    return Foo(b, c);
}
```

测试桩
```c++
#include <gtest/gtest.h>
#include <iostream>

class FooTest : public ::testing::Test
{
public:

	virtual void SetUp()
	{
		std::cout << "Setup" << std::endl;
	}

	void TearDown()
	{
		std::cout << "TearDown" << std::endl;
	}
};

TEST_F(FooTest, HandleNoneZeroInput)
{
    EXPECT_EQ(2, Foo(4, 10));
    EXPECT_EQ(6, Foo(30, 18));
}

TEST_F(FooTest, HandleNoneZeroInput2)
{
    EXPECT_EQ(2, Foo(4, 10));
    EXPECT_EQ(6, Foo(30, 18));
}

TEST(FooTestOther, HandleNoneZeroInput3)
{
    EXPECT_EQ(2, Foo(4, 10));
    EXPECT_EQ(6, Foo(30, 18));
}
```
