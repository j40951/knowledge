# Gitlab-ci

## Run GitLab Runner in a container

### Docker image installation

1. Install Docker first:

```shell
curl -sSL https://get.docker.com/ | sh
```

2. You need to mount a config volume into the gitlab-runner container to be used for configs and other resources:

```shell
docker run -d --name gitlab-runner --restart always \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:latest
```

Tip: On macOS, use /Users/Shared instead of /srv.

Or, you can use a config container to mount your custom data volume:

```shell
docker run -d --name gitlab-runner-config \
    -v /etc/gitlab-runner \
    busybox:latest \
    /bin/true
```

And then, run the Runner:

```shell
docker run -d --name gitlab-runner --restart always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    --volumes-from gitlab-runner-config \
    gitlab/gitlab-runner:latest
```

3. Register the runner you just launched by following the instructions in the (Docker section of Registering Runners)[https://docs.gitlab.com/runner/register/index.html#docker]. The runner won’t pick up any jobs until it’s registered.

Make sure that you read the (FAQ)[https://docs.gitlab.com/runner/faq/README.html] section which describes some of the most common problems with GitLab Runner.

### Update configuration

If you change the configuration in config.toml, you might need to restart the runner to apply the change. Make sure to restart the whole container instead of using gitlab-runner restart:

```shell
docker restart gitlab-runner
```

### Upgrade version

Pull the latest version (or a specific tag):

```shell
docker pull gitlab/gitlab-runner:latest
```

Stop and remove the existing container:

```shell
docker stop gitlab-runner && docker rm gitlab-runner
```

Start the container as you did originally:

```shell
docker run -d --name gitlab-runner --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  gitlab/gitlab-runner:latest
```

Note: You need to use the same method for mounting you data volume as you did originally (-v /srv/gitlab-runner/config:/etc/gitlab-runner or --volumes-from gitlab-runner-config).

### Reading GitLab Runner logs

When GitLab Runner is started as a foreground task (whether it’s a locally installed binary or inside of a Docker Container), the logs are printed to the standard output. When GitLab Runner is started as a system service (e.g. with Systemd), the logs are in most cases logged through Syslog or other system logging mechanism.

With GitLab Runner started as a Docker based service, since the gitlab-runner ... command is the main process of the container, the logs can be read using the docker logs command.

For example, if GitLab Runner was started with the following command:

```shell
docker run -d --name gitlab-runner --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  gitlab/gitlab-runner:latest
```

you may get the logs with:

```shell
docker logs gitlab-runner
```

where gitlab-runner is the name of the container, set with --name gitlab-runner by the first command.

You may find more information about handling container logs at the (Docker documentation pages)[https://docs.docker.com/engine/reference/commandline/logs/]

## Refrence

(Run GitLab Runner in a container)[https://docs.gitlab.com/runner/install/docker.html]

