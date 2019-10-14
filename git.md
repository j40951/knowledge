# Git

## git config

vi ~/.gitconfig

```ini
[user]
        name = j00234709
        email = jack.ju@huawei.com
[credential]
        helper = store
[http "https://github.comn"]
        proxy = http://user:pwd@proxyhk.xx.com:8080
        sslVerify = false
[https "https://github.com"]
        proxy = http://user:pwd@proxyhk.xx.com:8080
        sslVerify = false
```

### 清除掉缓存在git中的用户名和密码

```shell
git credential-manager uninstall
```

### 运行一下命令缓存输入的用户名和密码

```shell
git config --global credential.helper wincred
```

## create a new repository on the command line

```shell
echo "# commandline" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/mallbook/commandline.git
git push -u origin master
```

## push an existing repository from the command line

```shell
git remote add origin https://github.com/mallbook/commandline.git
git push -u origin master

```

## 本地库关联远程库

```shell
git remote add origin url
git pull origin master --allow-unrelated-histories
git push -u origin master
```

## 修改远程仓

```shell
git remote set-url origin new_url
--add 参数是增加一个远程仓
```

or

```sh
git config -e
```

If you wish to set tracking information for this branch you can do so with:

```sh
git branch --set-upstream-to=origin/<branch> <branch>
```

## 提交本地分支到远程分支

```shell
git push origin test:master         // 提交本地test分支作为远程的master分支 //好像只写这一句，远程的github就会自动创建一个test分支
git push origin test:test              // 提交本地test分支作为远程的test分支
```

如果想删除远程的分支呢？类似于上面，如果:左边的分支为空，那么将删除:右边的远程的分支。

```shell
git push origin :test              // 刚提交到远程的test将被删除，但是本地还会保存的，不用担心
```

## 回退本地的一个commit

```shell
git reset [--hard|soft|mixed|merge|keep] [commit|HEAD]
```

- --hard  
重设 index 和 working directory，从 `<commit>` 以来在 working directory 中的任何改变都被丢弃，并把 HEAD 指向 `<commit>`  
**说明**：第二次提交的 test2 已被丢弃！HEAD 指针重新指向了第一次提交的 commitID。**彻底回退到某个版本，本地的源码也会变为上一个版本的内容。**  

- --soft  
index 和 working directory 中的内容不作任何改变，仅仅把 HEAD 指向 `<commit>`。自从 `<commit>` 以来的所有改变都会显示在 git status 的 *Changes to be committed* 中。  
**说明**：第二次提交的 test2 被重置到了 *Changes to be committed* 中！HEAD 指针重新指向了第一次提交的commitID。**回退到某个版本，只回退了 commit 的信息。如果还要提交，直接 commit 即可。**

- --mixed  
仅重设 index，但是不重设 working directory。这个模式是默认模式，即当不显示告知 `git reset` 模式时，会使用 mixed 模式。这个模式的效果是，working directory 中文件的修改都会被保留，不会丢弃，但是也不会被标记成 *Changes to be committed*，但是会打出什么还未被更新的报告。

```shell
git push --force
```

## 从顶层库同步新分支的操作

- 1、新建本地分支

```shell
git checkout -b v2r2c00_pi5_feature
```

- 2、push到个人远程并设置为默认上游

```shell
git push --set-upstream origin v2r2c00_pi5_feature
```

- 3、将远程公共拉去到本地，并强制一致（有冲突不用管）

```shell
git pull upstream v2r2c00_pi5_feature
git reset --hard upstream/v2r2c00_pi5_feature
```

- 4、将本地代码强制推送到个人远程

```shell
git push -f
```

## 放弃本地修改

```shell
git reset --hard HEAD
git pull
```

## 使用Git下载指定分支命令为

```shell
git clone -b 分支名 仓库地址
```

## 查看最近一次提交修改的文件清单

```sh
git diff --name-only HEAD~ HEAD
```

## 获取两次commit修改的文件

```shell
git diff --name-only <commit-1> <commit-2>
```

## 删除分支

```shell
git branch -d dev
```

## Submodule 的使用

### 在项目中使用 Submodule

```shell
git submodule add git@github.com:jjz/pod-library.git pod-library
```

### 修改 Submodule

```shell
cd pod-library/
git status
git commit -a -m'test submodule'
git push
cd ..
git commit -m'update submodule'
git push
```

### 更新 Submodule

```shell
git submodule foreach git pull
```

or

```shell
cd pod-library
git pull
```

### clone Submodule

- 采用递归参数 --recursive

```shell
git clone git@github.com:jjz/pod-project.git --recursive
```

- 先 clone 父项目，再初始化 Submodule

```shell
git clone git@github.com:jjz/pod-project.git
cd pod-project
git submodule init
git submodule update
```

### 删除 Submodule

git 并不支持直接删除 Submodule 需要手动删除对应的文件:

```shell
cd pod-project
git rm --cached pod-library
rm -rf pod-library
rm .gitmodules
vim .git/config
```

可以看到 Submodule 的配置信息：

```ini
[submodule "pod-library"]
  url = git@github.com:jjz/pod-library.git
```

删除 submodule 相关的内容,然后提交到远程服务器:

```shell
git commit -a -m 'remove pod-library submodule'
```

### 参考

[submodule 笔记1](https://segmentfault.com/a/1190000003076028)  
[submodule 笔记2](https://segmentfault.com/a/1190000009928515)  
[submodule 笔记3](https://segmentfault.com/a/1190000000523363)  

```sh
git submodule foreach git checkout newcore_mysql
git submodule foreach git pull
```

## git cherry-pick 用于把另一个本地分支的 commit 修改应用到当前分支

```shell
git cherry-pick commit
```

Git 从 1.7.2 版本开始支持批量 cherry-pick，就是一次可以 cherry-pick 一个区间的 commit  

```shell
git cherry-pick <start-commit-id>..<end-commit-id>
git cherry-pick <start-commit-id>^..<end-commit-id>
```

前者表示把 `<start-commit-id>` 到 `<end-commit-id>` 之间(左开右闭，不包含 start-commit-id)的提交 cherry-pick 到当前分支  
后者有 "^" 标志的表示把 `<start-commit-id>` 到 `<end-commit-id>` 之间(闭区间，包含 start-commit-id)的提交 cherry-pick 到当前分支。  
其中，`<start-commit-id>` 到 `<end-commit-id>` 只需要 commit-id 的前6位即可，并且 `<start-commit-id>` 在时间上必须早于 `<end-commit-id>`

## git tag 使用

```shell
git tag
git tag -l 'v1.4.2.*'
```

### 显示 tag 信息

```shell
git show v1.4.2
```

### 新建标签

```shell
git tag -a v1.4 -m 'my version 1.4'
```

### 后期加注标签

```shell
git log --pretty=oneline
```

### 分享标签

```shell
git push origin v1.5
```

### 推送所有标签

```shell
git push origin --tags
```

### 基于 tag 创建分支

```shell
git checkout -b branch tag
```
