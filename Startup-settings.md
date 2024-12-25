# 方案一

直接在设置 -> 应用 -> 启动,直接勾上就行

但是有的软件或者很小的脚本,在这里没有显示,

**我们使用下面的方案二和方案三都能解决的问题**

# 方案二

## 第一步

直接在资源管理器中一路找到以下路径:

C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp

一路找可能比如Start Menu后面就找不到,事实上直接把这行路径丢到地址栏即可

或者

直接win+r,然后输入

```json
shell:Common Startup
```

## 第二步

直接把想要开机自启动的软件的快捷方式丢到这个文件夹下即可

# 方案三

与方案二不同的是,

方案二是直接为这台计算机的所有用户都创建了这个开机自启动,这并不好

我们推荐在这个路径下仅为当前账户创建开机自启动

C:\Users\wink\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

接下来和方案二操作一致

或者可以选择win+r,然后输入

```json
shell:startup
```



