# Single Install

    参考文档: https://www.jenkins.io/download/

## 下载jenkins
```shell
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
    https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt-get update
sudo apt-get install fontconfig openjdk-17-jre
sudo apt-get install jenkins
```

## 更新配置
```shell
sudo systemctl stop jenkins
sudo sed -i 's|/var/lib/jenkins|/data/jenkins|g' /lib/systemd/system/jenkins.service
sudo mkdir -p /data/jenkins
sudo chown jenkins:jenkins /data/jenkins
sudo systemctl enable jenkins --now
```

## 查看密码及初始化
```shell
sudo cat /data/jenkins/secrets/initialAdminPassword
```