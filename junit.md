# JUNIT 使用

测试用例编写

```java
public class FlowTest {

    @Test
    public void genFlowIDTest() {
        String [] args = new String[]{"a", "b", "c"};

        String v = Flow.genFlowID(args);
        assertEquals("70a78022b9be3aec7935234a0cfdbd7a", v);
    }
}
```

Unit Test 编译时依赖

```xml
<properties>
    <junit.jupiter.version>5.6.1</junit.jupiter.version>
</properties>

<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>${junit.jupiter.version}</version>
    <scope>test</scope>
</dependency>
```

Unit Test 运行时依赖

```xml
<dependency>
    <groupId>org.junit.platform</groupId>
    <artifactId>junit-platform-launcher</artifactId>
    <version>1.6.1</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter-engine</artifactId>
    <version>5.6.1</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.junit.vintage</groupId>
    <artifactId>junit-vintage-engine</artifactId>
    <version>5.6.1</version>
    <scope>test</scope>
</dependency>
```

[JUnit5 User Guard](https://junit.org/junit5/docs/current/user-guide/)
