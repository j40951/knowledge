# HBase

## Standalone HBase

This is the default mode. Standalone mode is what is described in the [quickstart](https://hbase.apache.org/book.html#quickstart) section. In standalone mode, HBase does not use HDFS — it uses the local filesystem instead — and it runs all HBase daemons and a local ZooKeeper all up in the same JVM. ZooKeeper binds to a well known port so clients may talk to HBase.

## Starting/Stopping HBase

- Starting HBase

```shell
./bin/start-hbase.sh
```

- Stopping HBase  

```sh
./bin/stop-hbase.sh
```

**Starting the HBase Thrift and REST Servers in the Foreground**  
Where `port` is the service’s port, and `info port` is the port for the web-ui with information about the service, use the following command to start the HBase Thrift server in the foreground:

```shell
./bin/hbase thrift2 -p <port> --infoport <infoport>
```

Where `port` is the service’s port, and `info port` is the port for the web-ui with information about the service, use the following command to start the HBase REST server in the foreground:

```shell
./bin/hbase rest -p <port> --infoport <infoport>
```

**Starting the HBase Thrift Server in the Background**  
Where `port` is the service’s port, and `info port` is the port for the web-ui with information about the service, use the following command to start the HBase Thrift server in the background:

```shell
./bin/hbase-daemon.sh start thrift2 -p <port> --infoport <infoport>
./bin/hbase-daemon.sh stop thrift2
```

Where `port` is the service’s port, and `info port` is the port for the web-ui with information about the service, use the following command to start the HBase REST server in the background:

```shell
./bin/hbase-daemon.sh start rest -p <port> --infoport <infoport>
./bin/hbase-daemon.sh stop rest
```
