+++
title = "Python Debugger Pdb"
date = 2024-09-06T08:44:25+08:00
tags = ["Python", "Debugging", "Pdb"]
categories = ["Tech"]
summary = "A comprehensive guide to using Python's built-in debugger (pdb) for efficient error finding."
image = "/images/covers/Pdb.png"
+++

`ipdb` or `pdb` is the Python Interactive Debugger. It allows you to pause your program, inspect variables, and step through code line by line.

## 为什么要调试 (Why Debug?)

*   **Print is not enough**: `print` 语句虽然简单，但对于复杂逻辑或循环，会产生大量干扰信息。
*   **Interactive**: 可以在断点处动态修改变量值，测试不同的逻辑分支，而无需修改代码重启。
*   **Context**: 查看函数调用栈 (Stack Trace)，知道“我是从哪里来的”。

## 如何启动 (How to Start)

1.  **修改代码式**: 在代码中插入断点。
    ```python
    import pdb; pdb.set_trace()
    # Python 3.7+ can simply use:
    breakpoint()
    ```

2.  **命令行式**: 不修改代码，直接调试脚本。
    ```bash
    python -m pdb myscript.py
    ```

3.  **事后验尸 (Post-mortem)**: 程序崩溃后自动进入调试模式。
    ```bash
    python -m pdb -c continue myscript.py
    ```

## 常用命令清单 (Cheat Sheet)

### Navigation (导航)
*   **`n` (next)**: 执行下一行。遇到函数**不进入**。
*   **`s` (step)**: 执行下一行。遇到函数**进入**内部。
*   **`c` (continue)**: 继续执行，直到下一个断点。
*   **`r` (return)**: 继续执行，直到当前函数返回。
*   **`j` (jump)**: 跳转到指定行号 (如 `j 45`)。

### Inspection (查看)
*   **`l` (list)**: 显示当前执行行附近的代码。
*   **`ll` (long list)**: 显示当前函数的全部代码。
*   **`p variable` (print)**: 打印变量的值。
*   **`pp variable` (pretty print)**: 美化打印（对字典/列表很有用）。
*   **`w` (where)**: 打印堆栈跟踪 (Stack Trace)。

### Control (控制)
*   **`b` (break)**: 设置断点 (如 `b 20` 或 `b main.py:20`)。
*   **`cl` (clear)**: 清除断点。
*   **`disable/enable`**: 禁用/启用断点。
*   **`q` (quit)**: 退出调试器。

## Pro Tip
推荐安装 **`ipdb`** (`pip install ipdb`)。它是 `pdb` 的增强版，支持语法高亮、Tab 自动补全，体验和 IPython 一样好。用法完全兼容。

## 调试交互命令

[命令参考点这里](https://docs.python.org/3/library/pdb.html#pdbcommand-help)

1. 与断点相关

   - b line (break line, 在 line 处设置断点)
   - b 5, if num == 4 (加条件语句)
   - disable bnum (禁用指定断点)
   - enable bnum (启用指定断点)
   - tbreak line (break line, 在 line 处设置临时断点, 只会生效一次)
   - b (break 显示所有断点)
   - cl (clear 删除所有断点)
   - cl bnum (删除指定断点)

2. 与继续执行相关

   - n (next line, 函数与算一行，不进行)
   - s (step into, 进入函数内部)
   - c (continue, 直到下一个断点)
   - unt (until, 直到指定行)
   - Enter (重复执行上一条命令)
   - r (return, 直到当前函数返回)
   - j (jump, 跳转到指定行, 中间的代码会被跳过)

3. 与变量与代码相关

   - p (print, 打印变量)
   - pp (pretty print, 打印变量, 格式化)
   - a (args, 打印函数参数)
   - display \[expression\] (在当前函数，当变量值被改变时，每次打印表达式的值, 不加参数显示所有 display 过的)
   - undisplay \[expression\] (取消显示该表达式的值，不加参数取消所有)
   - l (list, 显示当前行附近的代码)
   - ll (long list, 显示当前函数的代码)
   - w (where, 显示当前代码调用栈)
   - u (up, 上移一层调用栈)
   - d (down, 下移一层调用栈)

4. 帮助与退出

   - h \<topic\> (help, 显示某个命令的帮助)
   - h pdb (help, 显示 pdb 的帮助)
   - q (quit, 退出调试)

5. 自定义 pdb 的配置

   - .pdbrc 可以参考[这里](https://kylekizirian.github.io/ned-batchelders-updated-pdbrc.html)
