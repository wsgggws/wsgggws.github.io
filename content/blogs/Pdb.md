+++
title = "Python Debugger Pdb"
date =  2024-09-06T08:44:25+08:00
+++

## 调试本地脚本文件

### 1. breakpoint()

- help
- n
- s
- c
- l

### 2. python -m pdb script.py

- b 5, if num == 4
- brack
- clear 1
- l
- ll
- p var
- pp var
- unt 10
- jump 15 (中间的代码不会执行)
- return
- where
- args

### 3. python -m pdb -c continue script.py

- 以 post-mortem 模式启动, 在异常发生时自动启动

## 调试本地 Python API 服务

- TODO

## 调试 Docker 容器进程

- TODO
