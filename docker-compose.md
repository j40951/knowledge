# docker-compose

- [Docker Compose入门使用指南](https://www.jianshu.com/p/4c4b8e8f9f55)
- [使用Docker-Compose编排容器](http://www.dockerinfo.net/4257.html)
- [使用 docker-compose 替代 docker run](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)
- [Docker Compose Offical Document](https://docs.docker.com/compose/)

## 常用命令

```shell
docker-compose up
docker-compose images
docker-compose ps
docker-compose stop
docker-compose down
```

登录容器

```shell
docker-compose exec -u postgres postgres /bin/bash
```
