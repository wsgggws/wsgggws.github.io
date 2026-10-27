# 个人博客

使用 [Hugo](https://gohugo.io/) 和 Hugo Theme Stack 构建，文章保存在 `content/blogs/`。推送到 `main` 后，GitHub Actions 会构建并部署到 [GitHub Pages](https://wsgggws.github.io/) 和 [navydev.top/blog](https://navydev.top/blog/)。

## 本地环境

在 macOS 上安装 Hugo（主题需要 Extended 版本，Homebrew 的 Hugo 包已包含）：

```bash
brew install hugo sass/sass/sass
hugo version
sass --version
```

如果 Homebrew 提示需要显式添加或信任 Dart 依赖，可按其提示执行 `brew tap dart-lang/dart` 和 `brew trust --formula dart-lang/dart/dart`，再重试安装 Sass。

以下命令均在仓库根目录，也就是 `hugo.toml` 所在目录执行。当前主题使用 Hugo 的 `locale`、`hugo.Data` 等 API，要求 Hugo `0.158.0` 或更新版本，并通过 Dart Sass 编译样式。本地已使用 Hugo Extended `0.168.0` 验证；GitHub Actions 同样固定使用 `0.168.0` 并安装 Dart Sass，版本配置见 `.github/workflows/hugo.yaml`。

## 使用现有模板新建文章

```bash
hugo new content 'blogs/我的新文章.md'
```

Hugo 会读取仓库的 `archetypes/default.md`，自动生成 `content/blogs/我的新文章.md`，并填入标题、当前时间和以下字段：

```toml
+++
title = "我的新文章"
date = 2026-10-27T10:00:00+08:00
tags = []
categories = []
summary = ""
draft = false
+++
```

上面的日期仅作示例，新建时以 Hugo 自动生成的时间为准。两个 `+++` 之间是 TOML 格式的文章元数据，第二个 `+++` 之后用 Markdown 写正文，例如：

```markdown
这篇文章的开场介绍。

## 第一个要点

正文内容，支持 **加粗**、列表、引用和代码块。
```

常用字段：

| 字段 | 用途 |
| --- | --- |
| `title` | 页面显示的文章标题，可与文件名不同 |
| `date` | 文章日期，保留 `+08:00` 可明确使用北京时间 |
| `tags` | 标签，例如 `["English", "Learning"]` |
| `categories` | 分类，例如 `["Learning"]` 或 `["Tech"]` |
| `summary` | 文章摘要，建议填写简短介绍 |
| `draft` | 草稿开关；当前模板默认 `false`，未写完时可改为 `true` |
| `image` | 可选封面路径，例如 `"/images/covers/我的新文章.webp"`，需自行添加此字段 |

例如，本次文章可以通过下面的命令创建（文件已存在时无需重复执行）：

```bash
hugo new content 'blogs/林语堂的英文学习方法.md'
```

文章应放在 `blogs/` 下，因为站点的 `mainSections` 配置为 `["blogs"]`。目前文章链接使用文件名生成，例如 `blogs/我的新文章.md` 对应 `/blog/我的新文章/`。发布后修改文件名会改变链接；只改 `title` 不会改变该链接。

如果想调整以后新文章的默认字段，编辑 `archetypes/default.md` 即可，已有文章不会随之改变。

## 本地预览与草稿发布

```bash
hugo server -D
```

打开 [http://localhost:1313](http://localhost:1313)。修改文章保存后，页面会自动刷新；按 `Ctrl+C` 停止服务。`-D` 表示包含 `draft = true` 的草稿。

准备发布时，将文章的 `draft` 改为 `false`，然后检查正常构建：

```bash
hugo --gc --minify
```

输出目录为 `public/`，已经被 Git 忽略，无需提交。正常构建不会包含草稿或未来日期的文章；如果文章没有出现，先检查 `draft` 和 `date`。

## 图片与封面

将图片放入 `static/images/`，在正文中省略路径中的 `static`：

```markdown
![图片说明](/images/example.webp)
```

封面同理：先将文件放入 `static/images/covers/`，再在文章元数据中添加：

```toml
image = "/images/covers/我的新文章.webp"
```

也可以运行仓库现有的 `make images`：它会创建 Python 虚拟环境、安装 Pillow，并为文章生成文字封面。注意，此命令会遍历 `content/blogs/` 下所有 Markdown 文件，重写其中的 `image` 字段，运行后应检查 `git diff`。脚本默认使用 macOS 的苹方字体。

## 提交与自动部署

确认文章预览和构建无误后，只添加本次需要发布的源文件，例如：

```bash
git add 'content/blogs/我的新文章.md'
git commit -m "docs: 添加我的新文章"
git push
```

如果添加了图片，也要将相应图片加入提交。推送到 `main` 后，`.github/workflows/hugo.yaml` 会自动构建并部署；可以在仓库的 Actions 页面查看结果，也可以手动触发该工作流。`navydev.top` 的部署依赖仓库中配置的 SSH Secrets。

## Giscus 评论

站点使用 [Giscus](https://giscus.app/zh-CN) 提供免费评论，配置位于 `hugo.toml` 的 `[params.comments.giscus]`。评论保存在公开仓库 [wsgggws/wsgggws.github.io 的 Discussions](https://github.com/wsgggws/wsgggws.github.io/discussions) 中，分类为 `Announcements`；访客需要登录 GitHub 才能留言。

仓库需要开启 Discussions，并将 [Giscus GitHub App](https://github.com/apps/giscus) 安装到 `wsgggws.github.io` 仓库。安装时选择 **Only select repositories**，只勾选此博客仓库即可。仓库 ID 与分类 ID 是公开标识，不需要配置 API Key 或其他密钥。

评论使用 `pathname` 与文章关联，开启严格匹配。同一篇文章在两个正式站点的路径都是 `/blog/文章文件名/`，因此可以共享评论。修改标题不会影响关联；修改文件名或文章路径则需要同步调整对应 Discussion 的标题。每篇文章的讨论会在第一次有人留言或回应时自动创建，不必提前逐篇创建。

评论区使用简体中文，跟随站点的浅色、深色模式，并延迟加载。发布后打开任意文章，滚动到文末即可查看评论区；在 Discussions 页面管理、锁定或删除评论。

如需关闭某一篇文章的评论，在其 TOML 元数据中添加：

```toml
comments = false
```

全站关闭则将 `[params.comments]` 的 `enabled` 改为 `false`。如果评论区未正常加载，检查是否能访问 `giscus.app` 和 GitHub、仓库是否仍为公开状态，以及 Giscus App 是否获得了该仓库的授权。

## 常用命令与目录

| 命令 | 用途 |
| --- | --- |
| `hugo new content 'blogs/标题.md'` | 使用现有模板新建文章 |
| `hugo server -D` | 预览文章，包含草稿 |
| `hugo --gc --minify` | 构建正式站点到 `public/` |
| `make images` | 批量生成封面并更新文章的封面字段 |
| `make dev` | 先执行 `make images`，再启动预览（默认不包含草稿） |
| `make build` | 先执行 `make images`，再构建正式站点 |
| `make blog` | 先生成封面，再构建适用于 `navydev.top/blog/` 的站点到 `public-blog/` |

| 目录或文件 | 用途 |
| --- | --- |
| `archetypes/default.md` | 新文章模板 |
| `content/blogs/` | 博客文章 Markdown 源文件 |
| `static/images/` | 图片等静态资源 |
| `hugo.toml` | 站点、主题、菜单和文章链接配置 |
| `permalinks.navy.toml` | `navydev.top/blog/` 的文章链接覆盖配置，避免重复 `/blog/` 前缀 |
| `themes/hugo-theme-stack/` | 已有主题，无需重新添加 |
| `.github/workflows/hugo.yaml` | 自动构建与部署流程 |
