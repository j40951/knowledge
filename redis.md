# Redis

## Overview

- `String`: 主要用于存储字符串，显然不支持分页和排序。
- `Hash`: 主要用于存储 key-value 型数据，评论模型中全是 key-value 型数据，所以在这里 Hash 无疑会用到。
- `List`: 主要用于存储一个列表，列表中的每一个元素按元素的插入时的顺序进行保存，如果我们将评论模型按 createDate 排好序后再插入 List 中，似乎就能做到排序了，而且再利用 List 中的 LRANGE key start stop 指令还能做到分页。嗯，到这里 List 似乎满足了我们分页和排序的要求，但是评论还会被删除，就需要更新 Redis 中的数据，如果每次删除评论后都将 Redis 中的数据全部重新写入一次，显然不够优雅，效率也会大打折扣，如果能删除指定的数据无疑会更好，而 List 中涉及到删除数据的就只有 LPOP 和 RPOP 这两条指令，但 LPOP 和 RPOP 只能删除列表头和列表尾的数据，不能删除指定位置的数据，所以 List 也不太适合。
- `Set`: 主要存储无序集合，无序！排除。
- `SortedSet`: 主要存储有序集合， SortedSet 的添加元素指令 ZADD key score member [[score,member]…] 会给每个添加的元素 member 绑定一个用于排序的值 score，SortedSet 就会根据 score 值的大小对元素进行排序，在这里就可以将 createDate 当作 score 用于排序， SortedSet 中的指令 ZREVRANGE key start stop 又可以返回指定区间内的成员，可以用来做分页， SortedSet 的指令 ZREM key member 可以根据 key 移除指定的成员，能满足删评论的要求，所以， SortedSet 在这里是最适合的。

## 为 Redis 设置密码

Redis 默认配置是不需要密码认证的，也就是说只要连接的 Redis 服务器的 host 和 port 正确，就可以连接使用。这在安全性上会有一定的问题，所以需要启用 Redis 的认证密码，增加 Redis 服务器的安全性。

### 修改配置文件

Redis的配置文件默认在/etc/redis.conf，找到如下行：

```ini
#requirepass foobared
```

去掉前面的注释，并修改为所需要的密码：

requirepass myPassword （其中myPassword就是要设置的密码）

### 重启Redis

如果Redis已经配置为service服务，可以通过以下方式重启：

```shell
service redis restart
```

如果Redis没有配置为service服务，可以通过以下方式重启：

```shell
/usr/local/bin/redis-cli shutdown
/usr/local/bin/redis-server /etc/redis.conf
```

### 登录验证

设置Redis认证密码后，客户端登录时需要使用-a参数输入认证密码，不添加该参数虽然也可以登录成功，但是没有任何操作权限。如下：

```shell
$ ./redis-cli -h 127.0.0.1 -p 6379
127.0.0.1:6379> keys *
(error) NOAUTH Authentication required.
```

使用密码认证登录，并验证操作权限：

```shell
$ ./redis-cli -h 127.0.0.1 -p 6379 -a myPassword
127.0.0.1:6379> config get requirepass
1) "requirepass"
2) "myPassword"
```

看到类似上面的输出，说明Reids密码认证配置成功。

除了按上面的方式在登录时，使用-a参数输入登录密码外。也可以不指定，在连接后进行验证：

```shell
$ ./redis-cli -h 127.0.0.1 -p 6379
127.0.0.1:6379> auth myPassword
OK
127.0.0.1:6379> config get requirepass
1) "requirepass"
2) "myPassword"
127.0.0.1:6379>
```

### 在命令行客户端配置密码（redis重启前有效）

前面介绍了通过redis.conf配置密码，这种配置方式需要重新启动Redis。也可以通命令行客户端配置密码，这种配置方式不用重新启动Redis。配置方式如下：

```shell
127.0.0.1:6379> config set requirepass newPassword
OK
127.0.0.1:6379> config get requirepass
1) "requirepass"
2) "newPassword"
```

**注意**：使用命令行客户端配置密码，重启Redis后仍然会使用redis.conf配置文件中的密码。

### 在Redis集群中使用认证密码

如果Redis服务器，使用了集群。除了在master中配置密码外，也需要在slave中进行相应配置。在slave的配置文件中找到如下行，去掉注释并修改与master相同的密码即可：

```shell
# masterauth master-password
```
