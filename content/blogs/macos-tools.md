+++
title = "MacOS Tools"
date = 2023-03-17T13:00:51+08:00
tags = ["MacOS", "Productivity", "Tools"]
categories = ["Tech"]
summary = "分享一些提升效率的 MacOS 常用软件和工具。"
image = "/images/covers/macos-tools.png"
+++

这些是我常使用的 MacOS App，希望能帮助到你。
如果你也有好的工具推荐，欢迎推荐。

## 常用工具清单

| 软件 | 类别 | 作用 |
| :--- | :--- | :--- |
| **搜狗五笔** | 输入法 | 经典的五笔输入法，词库同步方便。 |
| **Homebrew** | 系统管理 | macOS 必备的包管理器，安装软件只需一行命令。 |
| **Chrome** | 浏览器 | 强大的扩展生态，开发者首选。 |
| **Raycast** | 效率工具 | Spotlight 的超强替代品，集成了脚本、剪贴板管理等。 |
| **iTerm2** | 终端 | 功能丰富的终端模拟器，支持分屏、搜索、主题定制。 |
| **WezTerm** | 终端 | 跨平台 GPU 加速终端，使用 Lua 配置，性能极佳。 |
| **Karabiner** | 键盘工具 | 键盘改键神器，实现 Hyper Key 等高级映射。 |
| **Neovim** | 编辑器 | 现代化的 Vim，插件生态丰富，编辑效率极高。 |
| **VS Code** | 编辑器 | 宇宙第一编辑器，不仅写代码，还能写文档、画图。 |
| **Shottr** | 截图工具 | 轻量级截图工具，支持滚动截图、像素化打码。 |

## 推荐理由

### Raycast
它不仅仅是一个启动器。我用它来管理剪貼板历史、窗口管理（替代 Magnet）、运行自定义脚本、查询汇率、甚至直接在搜索框里进行快速计算。它的扩展商店非常丰富，几乎能满足所有快捷操作需求。

### WezTerm vs iTerm2
虽然 iTerm2 是老牌强者，但 WezTerm 基于 GPU 渲染，速度极快。而且它的配置文件是 Lua 脚本，可以非常灵活地编程配置。对于跨平台（同时使用 macOS, Linux, Windows）的用户来说，WezTerm 的一致性体验更好。

### Karabiner-Elements
必装神器。我通常将 `Caps Lock` 映射为 `Hyper Key` (Cmd+Opt+Ctrl+Shift)，这样配合其他按键就可以组合出无数个不会冲突的全局快捷键。
|     Notion      | 笔记           |
|  Sublime Text   | 文本编辑器     |
|    Keycastr     | 按键回显       |
|     Postman     | Web API 请求   |
|     LICEcap     | 录制 Gif       |
|   Pearcleaner   | 软件卸载       |
|   Dictionary    | 字典           |
|    Snipaste     | 截图           |
|      Zoom       | 视频会议       |
|       Omi       | 视频录制       |
|      IINA       | 视频播放       |
|  NeteaseMusit   | 音乐播放       |
| KeepingYouAwake | 防锁屏         |
|     ClashX      | 科学上网       |
|       fzf       | 模糊搜索文件   |
|       bat       | cat 替代者     |
|    mitmproxy    | 抓包工具       |
|     BBDown      | B站下载工具    |

### 搜狗五笔

强烈建议删除 MacOS 自带的 ABC 输入法, 用清歌输入法，配置 shift 为中英文切换键，速度更快。

### [Homebrew](https://brew.sh/)

目前使用的是 MacBook M2，绝大部分软件通过 HomeBrew 安装。并可备份与复原

```
# Install Homebrew
$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)

# Install App by Homebrew
brew install ${SOMEAPP}

# Backup all installed apps to a file
brew bundle dump --describe --force --file="~/github/dotfiles/brew/Brewfile"

# Recover all apps from this file
brew bundle --file="~/github/dotfiles/brew/Brewfile"
```

### [Raycast](https://www.raycast.com/)

![raycast](/images/macos-tools/raycast.png)
Alfred 的替代品，它更加强大且免费。如粘贴板历史记录，文本片段，窗口管理，GitHub 搜索，本地 App 搜索，文件搜索等等。以一敌百，不在话下。

### Karabiner

如果你觉得 Esc 太远，可以与 CapsLock 交换。如果你觉得上下左右方向键太远，你也可以把它映射为 Command + hjkl 键，如果你想，那可以试试。

### Neovim

Yes, I like it. more details you can see: [https://github.com/wsgggws/nvim](https://github.com/wsgggws/nvim)

:wq

### Postman

![postman](/images/macos-tools/postman.jpg)
还是得表扬下这个“男人”，Curl => Code，及保存各种请求上下文，方便请求，响应的调试与复现。

### [KeepingYouAwake](https://keepingyouawake.app/)

当文档被展示，而你又在尽情分享时，你的电脑突然进入了睡眠状态，锁屏啦。这个 App 可以不让你们那么尴尬。

### [fzf](https://github.com/junegunn/fzf)

![fzf](/images/macos-tools/fzf.png)
模糊搜索, 并与很多工具进行了集成，详情可以参考[官方文档](https://github.com/junegunn/fzf)。

### [mitmproxy](https://mitmproxy.org/)

Charles, Fiddler 这些的替代品，值得拥有。

### [BBDown](https://github.com/nilaoda/BBDown)

一个命令行式哔哩哔哩下载器. Bilibili Downloader.
