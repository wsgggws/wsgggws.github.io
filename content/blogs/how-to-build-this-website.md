+++
title = "How To Build This Website"
date = 2023-03-12T15:44:12+08:00
tags = ["Start", "Hugo", "GitHub Actions", "Website"]
categories = ["Tech"]
summary = "A quick guide on how to build this website using Hugo and GitHub Actions."
image = "/images/covers/how-to-build-this-website.webp"
+++

This website is built with **Hugo**, a static site generator, and hosted on **GitHub Pages**. The deployment process is automated using **GitHub Actions**.

## Workflow

1.  **Write**: I write blog posts in Markdown format in the `content` directory.
2.  **Commit**: I commit the changes and push them to the GitHub repository.
3.  **Deploy**: GitHub Actions detects the push, builds the Hugo site, and deploys the generated `public` folder to the `gh-pages` branch.

## Prerequisites

You need the following tools installed on your local machine:

-   **Git**: For version control.
-   **Hugo**: For generating the static site.
-   **GitHub Account**: To host the repository.

### Installation

On macOS, you can use Homebrew:

```bash
brew install git
brew install hugo
```

## Setup Guide

### 1. Create a New Site

```bash
hugo new site my-blog
cd my-blog
git init
```

### 2. Add a Theme

Add a theme (e.g., PaperMod) as a submodule:

```bash
git submodule add https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
echo "theme = 'PaperMod'" >> hugo.toml
```

### 3. Create Content

```bash
hugo new posts/my-first-post.md
```

### 4. Run Locally

Start the local server with draft enabled:

```bash
hugo server -D
```

Visit `http://localhost:1313`.

### 5. GitHub Actions Configuration

Create `.github/workflows/hugo.yaml` to automate deployment.
You can find the standard workflow in the [Hugo Hosting on GitHub Pages](https://gohugo.io/hosting-and-deployment/hosting-on-github/) documentation.

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
