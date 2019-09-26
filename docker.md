# Docker

## 配置 Docker 仓库镜像
DOCKER_OPTS="--insecure-registry rnd-dockerhub.hotmall.com"
export NO_PROXY="rnd-dockerhub.hotmall.com"

## ubuntu 重启 Docker

```shell
service docker restart
```

## 搜索镜像

```shell
docker search  rnd-dockerhub.hotmall.com/official/
docker search  rnd-dockerhub.hotmall.com/library/
```

rnd-dockerhub.hotmall.com/official/：用于和docker hub官网的镜像进行定期同步  
rnd-dockerhub.hotmall.com/library/ : 为公司内源镜像库，普通用户也无权限上传个人镜像.  
