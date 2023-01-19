# git使用
# git add test.php（随便一个你的文件）
# git commit -m "第一次提交" //注释说明
# git remote add origin https://github.com/***/VSCode_Git_Test.git （这里是你的github仓库地址）
# git push -u origin master  //提交到你的仓库

# 关闭origin操作
# 1、先输入git remote rm origin 删除关联的origin的远程库
# 2、关联自己的仓库 git remote add origin https://gitee.com/xxxxxx.git
# 3、最后git push origin master，这样就推送到自己的仓库了。

# 代理解决方案
# //取消http代理
# git config --global --unset http.proxy
# //取消https代理 
# git config --global --unset https.proxy

# 分支处理
# (1)新建分支 git branch '分支名'
# (2)切换分支 git checkout '分支名'
# (3)进行项目上传
# git add .
# git commit -m "提交的信息"
# git remote add origin 远程仓库地址
# git push -u origin '分支名'


print('hlell')