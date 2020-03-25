# Java 常用用法

Murmur 哈希算法使用

```java
import com.google.common.hash.HashFunction;
import com.google.common.hash.Hashing;

public class Flow {

    private static final String CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    private static final int SCALE = 62;

    public static String genFlowID(final String[] args) {
        final String str = String.join("_", args);

        HashFunction hf = Hashing.murmur3_128(333);
        return hf.newHasher().putBytes(str.getBytes()).hash().toString();
    }

    public static String genFlowID62(final String[] args) {
        final String str = String.join("_", args);

        HashFunction hf = Hashing.murmur3_128(333);
        StringBuilder sb = new StringBuilder();
        int remainder = 0;
        boolean negative = false;
        long v = hf.newHasher().putBytes(str.getBytes()).hash().asLong();
        if (v < 0) {
            v = Math.abs(v);
            negative = true;
        }
        while (v > SCALE - 1) {
            remainder = Long.valueOf(v % SCALE).intValue();
            sb.append(CHARS.charAt(remainder));
            v = v / SCALE;
        }
        sb.append(CHARS.charAt(Long.valueOf(v).intValue()));
        if (negative) {
            sb.append("-");
        }
        return sb.reverse().toString();
    }
}
```

Maven 配置

```xml
<dependency>
    <groupId>com.google.guava</groupId>
    <artifactId>guava</artifactId>
    <version>21.0</version>
</dependency>
```

参考

[guava 代码](https://github.com/google/guava)
