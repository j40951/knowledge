# Spring

## context:component-scan 使用

在xml文件配置了 `<context:component-scan>` 标签后，spring 容器可以自动去扫描 base-pack 所指定的包或其子包下面的 Java 类文件，如果扫描到有 @Component、@Controller、@Service 、@Repository 等注解修饰的 Java类，则将这些类注册为 spring 容器中的 bean。

```xml
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans-2.5.xsd
    http://www.springframework.org/schema/context
    http://www.springframework.org/schema/context/spring-context.xsd">

    <!--<bean id="customerService" class="com.hotmall.chat.services.CustomerService">-->
        <!--<property name="customerDAO" ref="customerDAO"/>-->
    <!--</bean>-->

    <!--<bean id="customerDAO" class="com.hotmall.chat.dao.CustomerDAO"/>-->
    <context:component-scan base-package="com.hotmall.chat">
        <!--<context:include-filter type="annotation" expression="org.springframework.stereotype.Controller"/>-->
    </context:component-scan>
</beans>
```

注意点：

- 如果配置了 `<context:component-scan>` 标签元素，那么 `<context:annotation-config/>` 标签就可以不用在 `xml` 中配置了，因为前者包含了后者。
- `<context:component-scan>` 有一个 use-default-filters 属性，该属性值默认为 true，这就意味着会扫描指定包下的全部的有 @Component、@Controller、@Service 、@Repository 等注解修饰的 Java 类，则将这些类注册为 Spring 容器的 bean。
- `<context:component-scan>` 还提供了两个子标签：`<context:include-filter>` 和 `<context:exclude-filter>`
