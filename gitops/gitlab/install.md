# Single Install

    参考文档: https://docs.gitlab.com/omnibus/settings/configuration.html

## 下载
```shell
#!/bin/sh

# 依赖环境
sudo apt-get update
sudo apt-get install -y curl openssh-server ca-certificates tzdata perl
sudo apt-get install -y postfix

# 下载
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash

# 安装
sudo EXTERNAL_URL="gitlab.pangfaheng.com" apt-get install gitlab-ce

```

## 修改存储配置
```shell
# 更新存储位置
echo 'git_data_dirs({
  "default" => {
    "path" => "/data/gitlab-data"
   }
})'| sudo tee -a /etc/gitlab/gitlab.rb

sudo gitlab-ctl reconfigure
```

## 修改密码
```shell
# 修改密码
# 默认账户是root
sudo gitlab-rake "gitlab:password:reset"
```