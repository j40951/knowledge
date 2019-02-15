# HBase

## 通过 hbase shell 来连接正在运行的 HBase
```sh
./bin/hbase shell
```

HBase Shell; enter 'help<RETURN>' for list of supported commands.
Type "exit<RETURN>" to leave the HBase Shell
Version 0.94.0, r, Sun Aug 26 22:12:56 CST 2012
hbase(main):001:0>

## Display HBase Shell Help Text
Type `help` and press Enter, to display some basic usage information for HBase Shell, as well as several example commands. Notice that table names, rows, columns all must be enclosed in quote characters.
```sh
hbase> help get
```

## 创建表
创建表时，可以选择多个参数，但表名和列族名是必须的参数，其它参数还包括版本数、TTL
以及预分 Region 建表的 key 数组等
```sh
hbase> create 't1', {NAME => 'f1', VERSIONS => 5}
hbase> create 't1', {NAME => 'f1'}, {NAME => 'f2'}, {NAME => 'f3'}
hbase> # The above in shorthand would be the following:
hbase> create 't1', 'f1', 'f2', 'f3'
hbase> create 't1', {NAME => 'f1', VERSIONS => 1, TTL => 2592000, BLOCKCACHE => true}
hbase> create 't1', 'f1', {SPLITS => ['10', '20', '30', '40']}
hbase> create 't1', 'f1', {SPLITS_FILE => 'splits.txt'}
hbase> # Optionally pre-split the table into NUMREGIONS, using
hbase> # SPLITALGO ("HexStringSplit", "UniformSplit" or classname)
hbase> create 't1', 'f1', {NUMREGIONS => 15, SPLITALGO => 'HexStringSplit'}
```

## 插入一行数据 -- put
Put 数据时，必选参数是表名、RowKey、列名（包括列族和列名）和值，可选参数包括时间戳
用法：
```sh
hbase> put 't1', 'r1', 'c1', 'value', ts1
```

例如，向表 test 中 put 三条数据，并通过 count 命令计算 test 表中的数据的条数  
```sh
//向表 test 中 put 数据，RowKey 为 rowkey1，列族名为 cf，列名为 qualifier1，值为 value1
hbase(main):002:0> put 'test','rowkey1','cf:qualifier1','value1'
0 row(s) in 0.5940 seconds
hbase(main):003:0> put 'test','rowkey2','cf:qualifier2','value2'
0 row(s) in 0.0080 seconds
```

```sh
//指定时间戳为 3
hbase(main):011:0> put 'test','rowkey3','cf:qualifier3','value3',3
0 row(s) in 0.0510 seconds
hbase(main):013:0> count 'test'
3 row(s) in 0.0160 seconds
```

## 读取一行数据 -- Get
查询一行数据时，必选参数是表名和 RowKey，可选参数包括列名（包括列族和列名）、时间戳、版本数等
```sh
hbase> get 't1', 'r1'
hbase> get 't1', 'r1', {TIMERANGE => [ts1, ts2]}
hbase> get 't1', 'r1', {COLUMN => 'c1'}
hbase> get 't1', 'r1', {COLUMN => ['c1', 'c2', 'c3']}
hbase> get 't1', 'r1', {COLUMN => 'c1', TIMESTAMP => ts1}
hbase> get 't1', 'r1', {COLUMN => 'c1', TIMERANGE => [ts1, ts2], VERSIONS => 4}
hbase> get 't1', 'r1', {COLUMN => 'c1', TIMESTAMP => ts1, VERSIONS => 4}
hbase> get 't1', 'r1', 'c1'
hbase> get 't1', 'r1', 'c1', 'c2'
hbase> get 't1', 'r1', ['c1', 'c2']
```

## 读取多行数据 -- Scan
查询多行数据，必选参数是表名，可选参数包括列名（包括列族和列名）、起止 Key、Filter
```sh
//查询元表
hbase> scan '.META.'
hbase> scan '.META.', {COLUMNS => 'info:regioninfo'}
hbase> scan 't1', {COLUMNS => ['c1', 'c2'], LIMIT => 10, STARTROW => 'xyz'}
hbase> scan 't1', {COLUMNS => 'c1', TIMERANGE => [1303668804, 1303668904]}
hbase> scan 't1', {FILTER => "(PrefixFilter ('row2') AND (QualifierFilter s(>=, 'binary:xyz')))AND (TimestampsFilter ( 123, 456))"}
hbase> scan 't1', {FILTER => org.apache.hadoop.hbase.filter.ColumnPaginationFilter.new(1, 0)}
hbase> scan 't1', {COLUMNS => ['c1', 'c2'], CACHE_BLOCKS => false}
hbase> scan 't1', {RAW => true, VERSIONS => 10}
```

## List Information About your Table
Use the `list` command to confirm your table exists
```sh
hbase(main):002:0> list 'test'
TABLE
test
1 row(s) in 0.0180 seconds

=> ["test"]
```

Now use the `describe` command to see details, including configuration defaults
```sh
hbase(main):003:0> describe 'test'
Table test is ENABLED
test
COLUMN FAMILIES DESCRIPTION
{NAME => 'cf', VERSIONS => '1', EVICT_BLOCKS_ON_CLOSE => 'false', NEW_VERSION_BEHAVIOR => 'false', KEEP_DELETED_CELLS => 'FALSE', CACHE_DATA_ON_WRITE => 'false', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', MIN_VERSIONS => '0', REPLICATION_SCOPE => '0', BLOOMFILTER => 'ROW', CACHE_INDEX_ON_WRITE => 'false', IN_MEMORY => 'false', CACHE_BLOOMS_ON_WRITE => 'false', PREFETCH_BLOCKS_ON_OPEN => 'false', COMPRESSION => 'NONE', BLOCKCACHE => 'true', BLOCKSIZE => '65536'}
1 row(s)
Took 0.9998 seconds
```


## Other Shell commands
HBase 还提供了一些其它的 Shell API，包括 general、ddl、dml、tools、replication 和 security 六组，每组又包括多个 Shell 命令。每组命令和每个命令的用法均可以通过 help 查询其用法

|Group Name|Commands|
|:--------|:--------|
|general|status, table_help, version, whoami|
|ddl|alter, alter_async, alter_status, create, describe, disable, disable_all, drop, drop_all, enable, enable_all, exists, get_table, is_disabled, is_enabled, list, show_filters|
|namespace|alter_namespace, create_namespace, describe_namespace, drop_namespace, list_namespace, list_namespace_tables|
|dml|append, count, delete, deleteall, get, get_counter, incr, put, scan, truncate, truncate_preserve|
|tools|assign, balance_switch, balancer, catalogjanitor_enabled, catalogjanitor_run, catalogjanitor_switch, close_region, compact, flush, hlog_roll, major_compact, merge_region, move, split, trace, unassign, zk_dump|
|replication|add_peer, disable_peer, disable_tablerep, enable_peer, enable_tablerep, list_peers, list_replicated_tables, remove_peer, set_peer_tableCFs, show_peer_tableCFs|
|snapshots|clone_snapshot, delete_snapshot, list_snapshots, rename_snapshot, restore_snapshot, snapshot|
|security|grant, revoke, user_permission|
|visibility labels|add_labels, clear_auths, get_auths, set_auths, set_visibility|
|backup/restore|backup, list_backups, remove_backups, restore, stop_backup, stop_restore|
