# single install

    参考文档: https://gitlab.cn/install/

```shell
#!/bin/sh

# 依赖环境
sudo apt-get update
sudo apt-get install -y curl openssh-server ca-certificates tzdata perl
sudo apt-get install -y postfix

# 下载
curl -fsSL https://packages.gitlab.cn/repository/raw/scripts/setup.sh | /bin/bash

# 安装
export EXTERNAL_URL="gitlab.pangfaheng.com"
export GITLAB_ROOT_PASSWORD="Wnt#qWA4^tdW7Gk!"
sudo apt-get install gitlab-ce

# 更新存储位置
cat >> /etc/gitlab/gitlab.rb <<EOF
git_data_dirs({
  "default" => {
    "path" => "/data/gitlab-data"
   }
})
EOF
sudo gitlab-ctl reconfigure
```