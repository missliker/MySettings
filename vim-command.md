# vim官方说明书

```bash
vimtutor
```



vim的对range的修改是非常强大的

# 文本替换

## 全文a换b(不经过询问)

```bash
:$s/a/b/g
```

或者

```bash
:%s/a/b/g
```

## 全文a换b(经过询问)

```bash
:$s/a/b/gc
```

或者

```bash
:%s/a/b/gc
```

## 从第5行到第15行进行替换

```bash
:5,15s/a/b/g
```

## 当前行至结尾进行替换

```bash
:.,$s/a/b/g
```



# vim配置文件路径

第一个路径在git的根目录下,如图

```shell
D:\Program Files\Git\etc\vimrc
```

![image-20241226173327703](C:\Users\wink\Desktop\Settings\vim-command.assets\image-20241226173327703.png)

第二个在用户根目录下

```shell
C:\Users\wink\.vimrc
```

第三个也在用户根目录下

```shell
C:\Users\wink\.vim\vimrc
```



# 自动补全选择

```shell
ctrl + n (down)
ctrl + p (up)
```



# 区间删除

## 不包括区间符号 (逗号,尖括号,花括号,引号)

```
di(  (不进入insert模式)
ci(  (进入insert模式)
```

## 包括区间符号

```
da(  (不进入insert模式)
ca(  (进入insert模式)
```



# 移动跳转

```
gg				到文本第一个字符
shift + g		到文本最后一个字符
ctrl + o		到上一次光标的位置
zz				不动光标让文本居中
```



# normal模式转insert模式

```shell
i				到光标前输入
a				到光标后输入
shift + i		到行首输入
shift + a		到行尾输入
o				到下一行输入
shift + o		到上一行输入
```



# 复制全文

```shell
ggyG
```



# 批量修改

```shell
old
old 
old
old
old

先用*把old选起来,按一次*就能都选到了
然后按ciw,然后修改成new,然后jk为normal模式
然后按n,跳到下一个old
然后按.(.不用带shhift)就能修改这个新的old为new,
继续按n 继续按.即可
```



# 跳出大括号在下一行输入

```shell
jko
```



# 删除所有注释

```shell
%s/\/\/.*//g
```



# 修改当前行行首的单词

```shell
0ciw
```





