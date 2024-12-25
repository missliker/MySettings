# 创建git仓库

```bash
git init
git add .
git commit -m "A all"
git branch -M main
git remote add origin https://github.com/missliker/sublime-snippet.git
git push -u origin main
```



# 已有仓库

```bash
git remote add origin https://github.com/missliker/sublime-snippet.git
git branch -M main
git push -u origin main
```



# push.sh

```bash
git add .
git commit -m "`git status -s`"
git push
```

