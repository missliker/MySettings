# 运行cpp文件

```bash
g++ main.cpp -std=c++23 -o main
./main
```



# 创建文件夹

```bash
mkdir xx
```



# 创建文件

```bash
touch a.txt
```



# 查看

```bash
ls
ls -l
ls -a
ls -la
```



# 跳转

```bash
cd 
cd ..
cd ../..
cd -
```



# 打印当前路径

```bash
pwd
```



# 查看文件

```bash
cat a.txt
head --line=2 a.txt
head -n 2 a.txt
tail --line=2 a.txt
tail -n 2 a.txt
less a.txt ('专注模式',按q退出)
```



# 查看并修改文件

```bash
vim a.txt
nano a.txt
```



# 查看文件属性

```bash
file a.txt
```



# 查看文件位置

```bash
where gcc
where g++
where clear
```



# 删除文件

```bash
rm a.txt
rm  -f      （--force）   	(强制删除文件或目录：忽略不存在的文件，不提示确认)
rm  -i      （--interactive）	(删除既有文件或目录之前先询问用户)
rm  -r/-R  （--recursive）   (递归删除，防止目录里面有文件不能删除)
rm  -rf                      (递归强制删除非空文件夹)
```



# 删除文件夹

```bash
rm -d new
```



# 复制文件

```bash
cp a.cpp b.cpp
```



# 打印

```bash
echo "Hello, world!"

bg="Hello, world!"
echo ${bg} (变量要用$符号)

echo "${bg} -> 你好,世界!" (用{}来避免歧义)
```



# 重命名(剪切)

```bash
mv old.txt new.txt
```



# 循环

```bash
for i in week*
    do
    echo $i
    done
(打印以week开头的文件)

for i in week??
    do
    echo $i
    done
(打印以week开头并且后面只有两个字符的文件)

for i in week??; do echo ${i#week}; done (掐掉前面的week)

for i in week??; do echo now${i#week}; done (不仅掐掉,还加个now)

for i in week??
	do
	echo "mv $i old${i#week}"
	done
(打印出 mv week{i} old{i})

#掐头,%去尾
```



# 自制简化命令

```bash
alias (打印出已经制作的命令)

常用:
alias ll='ls -l'
alias la='ls -la'
alias cdd='cd /d'
```



# 读入(>>)

```bash
echo 'it is from bash!' >> a.txt
```

