# How to clean the shit of macos`s .DS_Store out to git in terminal
https://gist.github.com/lohenyumnam/2b127b9c3d1435dc12a33613c44e6308

# Git Pull
```shell
mkdir dir
cd dir
git init
git config user.name "username"
git config user.email username@mail.com
git config core.sshCommand "ssh -i ~/.ssh/id_rsa_example -F /dev/null"
git remote add origin git@git.example.com/myproject/repository.git or git remote add origin ssh://git@git.example.com:22/myproject/repository.git
git pull origin main
```

# Git Push
```shell
git add .
git commit -m "update message"
git push -u origin main
```

# All Git Option

## start a working area

### Clone a repository into a new directory
```shell
git clone
```

### Create an empty Git repository or reinitialize an existing one
```shell
git init
```

## work on the current change

### Add file contents to the index
```shell
git add
```

### Move or rename a file, a directory, or a symlink
```shell
git mv
```

### Restore working tree files
```shell
git restore
```

### Remove files from the working tree and from the index
```shell
git rm
```

## examine the history and state

### Use binary search to find the commit that introduced a bug
```shell
git bisect
```

### Show changes between commits, monit and working tree, etc
```shell
git diff
```

### Print lines matching a pattern
```shell
git grep
```

### Show commit logs
```shell
git log
```

### Show various types of objects
```shell
git show
```

### Show the working tree status
```shell
git status
```

## grow, mark and tweak your common history

### List, create, or delete branches
```shell
git branch
```