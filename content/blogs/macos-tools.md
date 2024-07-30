+++
title = "MacOS Tools"
date = 2023-03-17T13:00:51+08:00
+++

以下是我常使用的 MacOS 工具(App)，我并会对部分 App 进行说明，希望能在效率上帮助到你。
如果你有好的工具推荐，欢迎留言。

## 常用工具

|      软件       | 作用              |
| :-------------: | :---------------- |
|    Homebrew     | 软件包管理        |
|     Chrome      | 搜索与网页浏览    |
|     Raycast     | 效率神器          |
|     iTerm2      | 终端              |
|    Karabiner    | 改键              |
|     Neovim      | 文本编辑          |
|     Notion      | 笔记              |
|  Sublime Text   | 文本编辑器        |
|    Keycastr     | 按键回显          |
|     Postman     | Web API 请求      |
|     LICEcap     | 录制 Gif          |
|   AppCleaner    | 软件卸载          |
|   Dictionary    | 字典              |
|    Snipaste     | 截图              |
|      Zoom       | 视频会议          |
|       Omi       | 视频录制          |
|      IINA       | 视频播放          |
|  NeteaseMusit   | 音乐播放          |
| KeepingYouAwake | 防锁屏            |
|     ClashX      | 科学上网          |
|       fzf       | 模糊搜索文件      |
|       bat       | cat 替代者        |
|     AltTab      | 切换窗口          |
|   Hidden Bar    | 隐藏菜单栏        |
|    mitmproxy    | 抓包工具          |
|  Thor Launcher  | 快捷键直接打开App |
| KeyboardHolder  | 设置App初始输入法 |

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

### [AltTab](https://alt-tab-macos.netlify.app/)

它的窗口要的键是 Option + Tab， 相比原生的 Command + Tab，它更加直观更易选择你想打开的 App。

### [Hidden Bar](https://apps.apple.com/us/app/hidden-bar/id1452453066?mt=12)

![hidden-bar](/images/macos-tools/hidden-bar.png)
对常用的显示，不常用的隐藏，这样有更好的屏幕空间体验。

### [mitmproxy](https://mitmproxy.org/)

Charles, Fiddler 这些的替代品，值得拥有。
