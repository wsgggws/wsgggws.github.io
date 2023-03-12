---
title: "How to build this website"
date: 2023-03-12T15:44:12+08:00
aliases: ["/blogs"]
tags: ["GitHub Page", "Hugo", "PaperMod"]
draft: false
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
description: "Depoly a static website to GitHub by Hugo"
canonicalURL: "https://canonical.url/to/page"
disableHLJS: true # to disable highlightjs
disableShare: false
disableHLJS: false
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
cover:
    image: "<image path/url>" # image path/url
    alt: "<alt text>" # alt text
    caption: "<text>" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: true # only hide on current single page
editPost:
    URL: "https://github.com/wsgggws/wsgggws.github.io/blob/main/content"
    Text: "Edit" # edit text
    appendFilePath: true # to append file path to Edit link
---

## Prequiments

- Hugo
- Git
- GitHub

```bash
brew install git
brew install hugo
```

## Create new site by Hugo

```bash
hugo new site wsgggws.github.io
cd wsgggws.github.io

git config --global init.defaultBranch main
git init
```

## Install theme [PaperMod](https://github.com/adityatelange/hugo-PaperMod/wiki/Installation#method-2)

```bash
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
git submodule update --init --recursive # needed when you reclone your repo (submodules may not get cloned automatically)
```

## Edit [config.yaml](https://github.com/adityatelange/hugo-PaperMod/wiki/Installation#sample-configyml)

Noted I set [profileMode](https://github.com/wsgggws/wsgggws.github.io/blob/main/config.yaml#L60) as `true`

```bash
# you could remove config.toml, or translate yaml to toml online
vim config.yaml
```

Make some dirctions named `blogs`, `projects`, `about` in _content_ direction.

```bash
content
├── about
│   └── index.md
├── blogs
│   ├── go-solo.md
│   └── how-to-build-this-website.md
├── projects
│   ├── learn-english.md
│   └── learn-go.md
└── tags
```

## Create a new posts

```bash
hugo new posts blogs/go-solo.md
```

Edit this file, and notice that set [aliases](https://raw.githubusercontent.com/wsgggws/wsgggws.github.io/main/content/blogs/go-solo.md): ["/blogs"]
In this way, Its content could be showed in `Blogs`.
Template could refer [page.md](https://github.com/adityatelange/hugo-PaperMod/wiki/Installation#sample-pagemd)

## Observing locally website

```bash
hugo server
```

## [Hosting on GitHub](https://gohugo.io/hosting-and-deployment/hosting-on-github/)

Create a repo named {username}.github.io in GitHub

```bash
# You should change wsgggws to your username
git remote add origin git@github.com:wsgggws/wsgggws.github.io.git

vim .github/workflows/hugo.yaml

git add .
git commit -m"Add github action for auto deploying"
git push -f -u origin main

# After GitHub action is done
open https://wsgggws.github.io
```

## Write blogs and auto deploy

```
hugo new posts blogs/xxx.md
vim conten/blogs/xxx.md
git add .
git commit -m"Add a new post xxx"
git push -f origin main

# After GitHub action is done
open https://wsgggws.github.io
```
