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

命令行参数支持
```c++
int main(int argc, char *argv[])
{
	testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}

```

参数列表  
|命令行参数|说明|
|:--|:--|
|--gtest_list_tests|使用这个参数时，将不会执行里面的测试案例，而是输出一个案例的列表。|
|--gtest_filter|对执行的测试案例进行过滤，支持通配符 <br> ?    单个字符<br> *    任意字符<br> -    排除，如，-a 表示除了a <br> :    取或，如，a:b 表示a或b <br> 比如下面的例子：<br> ./foo_test 没有指定过滤条件，运行所有案例 <br> ./foo_test --gtest_filter=* 使用通配符*，表示运行所有案例 <br> ./foo_test --gtest_filter=FooTest.* 运行所有“测试案例名称(testcase_name)”为FooTest的案例 <br> ./foo_test --gtest_filter=*Null*:*Constructor* 运行所有“测试案例名称(testcase_name)”或“测试名称(test_name)”包含Null或Constructor的案例。<br> ./foo_test --gtest_filter=-*DeathTest.* 运行所有非死亡测试案例。<br> ./foo_test --gtest_filter=FooTest.*-FooTest.Bar 运行所有“测试案例名称(testcase_name)”为FooTest的案例，但是除了FooTest.Bar这个案例| <br>
|--gtest_also_run_disabled_tests|执行案例时，同时也执行被置为无效的测试案例。关于设置测试案例无效的方法为: <br> 在测试案例名称或测试名称中添加 `DISABLED` 前缀|
|--gtest_repeat=[COUNT]|设置案例重复运行次数，非常棒的功能！比如：<br> <br> --gtest_repeat=1000      重复执行1000次，即使中途出现错误。<br> --gtest_repeat=-1          无限次数执行。。。。<br> --gtest_repeat=1000 --gtest_break_on_failure     重复执行1000次，并且在第一个错误发生时立即停止。这个功能对调试非常有用。<br> --gtest_repeat=1000 --gtest_filter=FooBar     重复执行1000次测试案例名称为FooBar的案例。<br>
|--gtest_color=(yes\|no\|auto)|输出命令行时是否使用一些五颜六色的颜色。默认是auto。|
|--gtest_print_time|输出命令行时是否打印每个测试案例的执行时间。默认是不打印的。|
|--gtest_output=xml[:DIRECTORY_PATH\|:FILE_PATH]|将测试结果输出到一个xml中。<br> <br> 1.--gtest_output=xml:    不指定输出路径时，默认为案例当前路径。<br> 2.--gtest_output=xml:d:\ 指定输出到某个目录 <br> 3.--gtest_output=xml:d:\foo.xml 指定输出到d:\foo.xml <br> 如果不是指定了特定的文件路径，gtest每次输出的报告不会覆盖，而会以数字后缀的方式创建。xml的输出内容后面介绍吧。 <br>|
|--gtest_break_on_failure|调试模式下，当案例失败时停止，方便调试|
|--gtest_throw_on_failure|当案例失败时以C++异常的方式抛出|
|--gtest_catch_exceptions|是否捕捉异常。gtest默认是不捕捉异常的，因此假如你的测试案例抛了一个异常，很可能会弹出一个对话框，这非常的不友好，同时也阻碍了测试案例的运行。如果想不弹这个框，可以通过设置这个参数来实现。如将--gtest_catch_exceptions设置为一个非零的数。<br> <br> 注意：这个参数只在Windows下有效。|
