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

## 调试交互命令

[命令参考点这里](https://docs.python.org/3/library/pdb.html#pdbcommand-help)

1. 与断点相关

   - b 5, if num == 4
   - b line (break line, 在 line 处设置断点)
   - tbreak line (break line, 在 line 处设置临时断点, 只会生效一次)
   - break (显示所有断点)
   - clear (删除所有断点)
   - clear num (删除指定断点)

2. 与继续执行相关

   - n (next line, 函数与算一行，不进行)
   - s (step into, 进入函数内部)
   - c (continue, 直到下一个断点)
   - r (return, 直到当前函数返回)
   - unt (until, 直到指定行)
   - j (jump, 跳转到指定行, 中间的代码会被跳过)

3. 与变量与代码相关

   - p (print, 打印变量)
   - pp (pretty print, 打印变量, 格式化)
   - l (list, 显示当前行附近的代码)
   - ll (long list, 显示当前函数的代码)
   - w (where, 显示当前代码调用栈)
   - u (up, 上移一层调用栈)
   - d (down, 下移一层调用栈)
   - a (args, 显示当前函数的参数)
   - q (quit, 退出调试)

## 调试本地 Python API 服务

- TODO

## 调试 Docker 容器进程

- TODO
