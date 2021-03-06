## How to contribute:

1. Fork this repository on your own GitHub Account

2. Clone this repository to your local machine

```
$ git clone "https://www.github.com/{Your Git Username}/Observability-As-Code"
```

3. Go to the root folder of this repository
```
cd Evolvve-Student-Chapter-Application
```

4. Make your changes on new branch
```
$ git checkout -b {branch name}
```

5. Stage your changes
```
$ git add {filename}
```

6. Commit your changes
```
$ git commit -m "Commit message"
```

7. Push your branch
```
$ git push -u origin {branch name}
```

8. Go to GitHub and open a pull request to the upstream repository

## How to update forked repository with our main repository

```
$ git remote add upstream "https://www.github.com/StatusNeo/Observability-As-Code"
$ git checkout master
$ git fetch upstream
$ git merge upstream/master
$ git push -f origin master
```
