# on-my-posh

主题路径:

```shell
C:\Users\wink\AppData\Local\Programs\oh-my-posh\themes
```

# pwsh

添加参数：
```shell
%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe -nologo
```

主要是-nologo



如果是单独的pwsh，在路径

```shell
C:\Users\wink\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
```

但是如果是Windows Terminal的pwsh，在路径

```shell
C:\Users\wink\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```

输入：

```json
oh-my-posh init pwsh --config $env:POSH_THEMES_PATH\montys.omp.json | Invoke-Expression
```

若报错则需要修改pwsh的安全策略，管理员打开pwsh输入：
```shell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```



但是其实推荐较方便的设置方式是：

输入代码打开配置文件：

```shell
notepad $PROFILE
```

如果第一次配置，没有配置文件，则：
```shell
New-Item -Path $PROFILE -Type File -Force
```

查看有哪些主题：
```shell
Get-PoshThemes
```

推荐主题有：

-   montys
-   M365Princess
-   dracula
-   easy-term
-   gmay
-   jandedobbeleer
-   poshmon
-   xtoys

# Git Bash

## 添加Git Bash

![image-20241225214254960](C:\Users\wink\Desktop\Settings\Windows-Terminal-settings.assets\image-20241225214254960.png)

命令行：
```shell
D:\Program Files\Git\bin\bash.exe --login -i
```

图标：

```shell
D:\Program Files\Git\mingw64\share\git\git-for-windows.ico
```

## 配置oh-my-posh

在路径:

```shell
D:\Program Files\Git\etc\bash.bashrc
```

中加入以下代码:

```bash
eval "$(oh-my-posh init bash --config C:/Users/wink/AppData/Local/Programs/oh-my-posh/themes/montys.omp.json)"
```

## 删除到最开始的时候屏幕闪烁解决办法

新建一个~/.inputrc文件，输入代码：

```bash
set bell-style none
```

如果是windows用户，则路径为：

```shell
C:\Users\wink\.inputrc
```

## 中文乱码

可以用

```bash
locale
```

来看当前的语言包

```bash
export LANG=C.UTF-8
```

需要把这些内容写入到路径:

```bash
D:\Program Files\Git\etc\bash.bashrc
```

新开一个bash后再次输入

```bash
locale
```

输出内容发生改变则大概率成功
