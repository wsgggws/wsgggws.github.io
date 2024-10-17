+++
title = "How To Build This Website"
date = 2023-03-12T15:44:12+08:00
+++

- Write a Markdown file
- Commit to GitHub
- Automatically deploy to GitHub Pages by GitHub Actions

## prerequisites

- Hugo
- Git
- GitHub repo

```
brew install git
brew install hugo
```

## Create new site by Hugo

```
hugo new site wsgggws.github.io
cd wsgggws.github.io

git config --global init.defaultBranch main
git init
```

## Install theme [paper](https://www.producthunt.com/products/hugo-paper)

```
git submodule add https://github.com/nanxiaobei/hugo-paper themes/paper
```

## Create a new posts

```
hugo new content blogs/title.md
```

## Observing locally website

```
hugo server
```

## [Hosting on GitHub](https://gohugo.io/hosting-and-deployment/hosting-on-github/)

Create a repo named {username}.github.io in GitHub

```
# You should change wsgggws to your username
git remote add origin git@github.com:wsgggws/wsgggws.github.io.git

vim .github/workflows/hugo.yaml

git add .
git commit -m"Add github action for auto deploying"
git push -f -u origin main

# After GitHub action is done
open https://wsgggws.github.io
```

## references

- <https://gohugo.io/hosting-and-deployment/hosting-on-github/>
