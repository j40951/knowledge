## 本地库关联远程库

```
git remote add origin url
git pull origin master --allow-unrelated-histories
git push -u origin master
```
## 修改远程仓
```
git remote set-url origin new_url
--add 参数是增加一个远程仓
```
or
```
git config -e
```
## 回退本地的一个commit
git  reset  [--hard|soft|mixed|merge|keep]  [commit|HEAD]
–hard：重设index和working directory，从`<commit>`以来在working directory中的任何改变都被丢弃，并把HEAD指向`<commit>`
**说明**：第二次提交的test2已被丢弃！HEAD指针重新指向了第一次提交的commitID。**彻底回退到某个版本，本地的源码也会变为上一个版本的内容。**
–soft：index和working directory中的内容不作任何改变，仅仅把HEAD指向`<commit>`。自从`<commit>`以来的所有改变都会显示在git status的_“Changes to be committed”_中。
**说明**：第二次提交的test2被重置到了”Changes to be committed”中！HEAD指针重新指向了第一次提交的commitID。**回退到某个版本，只回退了commit的信息。如果还要提交，直接commit即可。**

–mixed：仅重设index，但是不重设working directory。这个模式是默认模式，即当不显示告知`git reset`模式时，会使用mixed模式。这个模式的效果是，working directory中文件的修改都会被保留，不会丢弃，但是也不会被标记成_“Changes to be committed”_，但是会打出什么还未被更新的报告。

git push --force

## 从顶层库同步新分支的操作

```
# 1\. 新建本地分支
git checkout -b v2r2c00_pi5_feature

# 2\. push到个人远程并设置为默认上游
git push --set-upstream origin v2r2c00_pi5_feature

# 3\. 将远程公共拉去到本地，并强制一致（有冲突不用管）
git pull upstream v2r2c00_pi5_feature
git reset --hard upstream/v2r2c00_pi5_feature

# 4\. 将本地代码强制推送到个人远程
git push -f
```
