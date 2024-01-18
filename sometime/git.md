# client pull git:xxx

    如何拉取代码到本地

```shell
mkdir mycode
cd mycode
git init
git config user.name "username"
git config user.email username@mail.com
git config core.sshCommand "ssh -i ~/.ssh/id_rsa_example -F /dev/null"
git remote add origin ssh://git@git.example.com:22/myproject/mycode.git
git pull origin main
```
