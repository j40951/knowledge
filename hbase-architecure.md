# HBase Architecture

## Architecture
![Architecture](hbase-images/architecture.png)

## Region
![Region](hbase-images/region.png)

将一个数据表按Key值范围横向划分为一个个的子表，实现分布式存储。这个子表，在HBase中被称作“Region”。每一个Region都关联一个Key值范围，即一个使用StartKey和EndKey描述的区间。事实上，每一个Region仅仅记录StartKey就可以了，因为它的EndKey就是下一个Region的StartKey。Region是HBase分布式存储的最基本单元。

## Region 与 RegionServer
![RegionServer](hbase-images/regionserver.png)

RegionServer是HBase的数据服务进程。负责处理用户数据的读写请求。Region被交由RegionServer管理。实际上，所有用户数据的读写请求，都是和RegionServer上的Region进行交互。Region可以在RegionServer之间发生转移。  

思考?  
一个Region包含了一个Startkey和EndKey范围；一条用户数据KeyValue必然属于一个唯一的Region；Region由RegionServer来管，那么，这个路由信息保存在哪里呢？Region如何才可以转移？由谁负责转移？  

## Region 分类
![Region](hbase-images/region_classes.png)

Region 分为元数据 Region 以及用户 Region 两类。而对于元数据 Region，又包含 Root Region 和 Meta Region 两类。
- Root Region 记录了 Meta Region 的路由信息。
- Meta Region 记录了每一个 User Region 的路由信息。
读写 Region 数据的路由，包括如下几步：
- 找寻 Root Region 地址。
- 由 Root Region 找寻 Meta Region 地址。
- 再由 Meta Region 找寻 User Region 地址。

思考？  
Root Region 信息保存在哪里？

## Master
![Master](hbase-images/master.png)
- Master 进程负责管理所有的 RegionServer。
  - 新 RegionServer 的注册。
  - RegionServer Failover 处理。
- Master 进程负责建表/修改表/删除表以及一些集群操作。
- Master 进程负责所有 Region 的转移操作。
  - 新表创建时的 Region 分配。
  - 运行期间的负载均衡保障。
  - RegionServer Failover 后的 Region 接管。
- Master 进程有主备角色。集群可以配置多个
  - Master 角色，集群启动时，这些 Master 角色通过竞争获得主 Master 角色。
  - 主 Master 只能有一个，所有的备 Master 进程在集群运行期间处于休眠状态，不干涉任何集群事务。

疑问？  
主备 Master 进程角色是如何进行裁决的？

## ZooKeeper
![Zookeeper](hbase-images/zookeeper.png)

- 提供分布式锁的服务。  
例如，多个 Master 进程竞争主 Master 角色时，怎么样保证仅有一个 Active 角色存在？这就需要一个分布式的锁机制来保证。多个 Master 进程都尝试着去 ZooKeeper 中写入一个对应的节点，该节点只能被一个 Master 进程创建成功，创建成功的 Master 进程就是 Active 角色。
- 提供了事件监听机制。  
例如，主 Master 进程宕掉之后，其它的备 Master 如何能够快速的接管？这个过程中，备 Master 在监听那个对应的 ZooKeeper 节点。主 Master 进程宕掉之后，该节点会被删除，那么，其它的备 Master 就可以收到相应的消息。
- 个别场景，可充当一个微型数据库角色。  
例如，在 ZooKeeper 中存放了 Root Region 的地址（RootRegion 原来是存在 ZooKeeper 中的！），此时，可以将它理解成一个微型数据库。

## HDFS
![HDFS](hbase-images/hdfs.png)
- HDFS 是一个分布式文件系统。它通过将一个大的文件划分成一个个固定大小的 Block 来实现分布式存储。每一个 Block 的默认大小为64MB。
- 每一个 Block 都存在多个备份，并且被部署在不同的数据节点上，来保障数据的安全。
- 目前，HBase 的所有底层数据都以文件的形式交由 HDFS 来存储。HBase 一侧本身不固化保存数据信息。


思考?  
NAS 能否替代 HDFS 来作为 HBase 的底层存储？

## 总结 
![summary](hbase-images/summary.png)
