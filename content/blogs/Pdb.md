+++
title = "Python Debugger Pdb"
date =  2024-09-06T08:44:25+08:00
+++

## 为什么要调试

- 更少的代码侵入
- 更高效的错误定位
- 更全面的信息查看
- 条件断点 及 运行时反复修改变量值

## 如何开始调试

1. 添加 breakpoint() 行 (修改源文件)

2. python -m pdb script.py (不修改文件)

3. python -m pdb -c continue script.py (以 post-mortem 模式启动, 在异常发生时自动启动)

4. .pdbrc 文件 (自定义 pdb 的配置)

```python
# 打印欢迎信息
!import sys
!print("Python version:", sys.version)

# Print a dictionary, sorted. %1 is the dict, %2 is the prefix for the names.
alias p_ for k in sorted(%1.keys()): print(f"%2{k.ljust(max(len(s) for s in %1.keys()))} = {%1[k]}")

# Print the member variables of a thing.
alias pi p_ %1.__dict__ %1.

# Print the member variables of self.
alias ps pi self

# Print the locals.
alias pl p_ locals() local:

# Next and list, and step and list.
alias nl n;;l
alias sl s;;l

# 设置自动显示的变量
display sys.argv

# 设置断点, 仅 python -m pdb -c continue script.py 时生效
# break my.py:5

# 退出时打函数
# import atexit
# atexit.register(lambda : print("Exiting pdb..."))
```

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
