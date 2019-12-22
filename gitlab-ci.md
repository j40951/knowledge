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

3. Register the runner you just launched by following the instructions in the [Docker section of Registering Runners](https://docs.gitlab.com/runner/register/index.html#docker). The runner won’t pick up any jobs until it’s registered.

Make sure that you read the [FAQ](https://docs.gitlab.com/runner/faq/README.html) section which describes some of the most common problems with GitLab Runner.

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

You may find more information about handling container logs at the [Docker documentation pages](https://docs.docker.com/engine/reference/commandline/logs/)

## Registering Runners

### One-line registration command

If you want to use the non-interactive mode to register a Runner, you can either use the register subcommands or use their equivalent environment variables

To see a list of all the register subcommands, use:

```shell
gitlab-runner register -h
```

To register a Runner using the most common options, you would do:

```shell
sudo gitlab-runner register \
  --non-interactive \
  --url "https://gitlab.com/" \
  --registration-token "PROJECT_REGISTRATION_TOKEN" \
  --executor "docker" \
  --docker-image alpine:latest \
  --description "docker-runner" \
  --tag-list "docker,aws" \
  --run-untagged="true" \
  --locked="false" \
  --access-level="not_protected"
```

If you’re running the Runner in a Docker container, the register command would look like:

```shell
docker run --rm -v /srv/gitlab-runner/config:/etc/gitlab-runner gitlab/gitlab-runner register \
  --non-interactive \
  --executor "docker" \
  --docker-image alpine:latest \
  --url "https://gitlab.com/" \
  --registration-token "PROJECT_REGISTRATION_TOKEN" \
  --description "docker-runner" \
  --tag-list "docker,aws" \
  --run-untagged="true" \
  --locked="false" \
  --access-level="not_protected"
```

## Setting up GitLab CI

We want to be able to configure our project so that our app is built, and it has the complete suite of tests run upon check-in. To do so, we have to create our GitLab CI config file, called .gitlab-ci.yml, and place it in the root of our project.

So, first things first: If you're just here for a snippet to copy-paste, here is a .gitlab-ci.yml that will build and test the Materialistic app:

```yaml
image: openjdk:8-jdk

variables:
  ANDROID_COMPILE_SDK: "28"
  ANDROID_BUILD_TOOLS: "28.0.2"
  ANDROID_SDK_TOOLS:   "4333796"

before_script:
  - apt-get --quiet update --yes
  - apt-get --quiet install --yes wget tar unzip lib32stdc++6 lib32z1
  - wget --quiet --output-document=android-sdk.zip https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_TOOLS}.zip
  - unzip -d android-sdk-linux android-sdk.zip
  - echo y | android-sdk-linux/tools/bin/sdkmanager "platforms;android-${ANDROID_COMPILE_SDK}" >/dev/null
  - echo y | android-sdk-linux/tools/bin/sdkmanager "platform-tools" >/dev/null
  - echo y | android-sdk-linux/tools/bin/sdkmanager "build-tools;${ANDROID_BUILD_TOOLS}" >/dev/null
  - export ANDROID_HOME=$PWD/android-sdk-linux
  - export PATH=$PATH:$PWD/android-sdk-linux/platform-tools/
  - chmod +x ./gradlew
  # temporarily disable checking for EPIPE error and use yes to accept all licenses
  - set +o pipefail
  - yes | android-sdk-linux/tools/bin/sdkmanager --licenses
  - set -o pipefail

stages:
  - build
  - test

lintDebug:
  stage: build
  script:
    - ./gradlew -Pci --console=plain :app:lintDebug -PbuildDir=lint

assembleDebug:
  stage: build
  script:
    - ./gradlew assembleDebug
  artifacts:
    paths:
    - app/build/outputs/

debugTests:
  stage: test
  script:
    - ./gradlew -Pci --console=plain :app:testDebug
```

Well, that's a lot of code! Let's break it down.

## Refrence

- [Run GitLab Runner in a container](https://docs.gitlab.com/runner/install/docker.html)
- [Registering Runners](https://docs.gitlab.com/runner/register/index.html#docker)
- [Advanced configuration](https://docs.gitlab.com/runner/configuration/advanced-configuration.html)
- [Setting up GitLab CI for Android projects](https://about.gitlab.com/blog/2018/10/24/setting-up-gitlab-ci-for-android-projects/)


