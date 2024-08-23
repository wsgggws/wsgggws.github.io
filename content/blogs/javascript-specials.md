+++
title = "Javascript 特性"
date =  2024-08-05T21:13:46+08:00
+++

## 类型 _typeof x_

- let, const, var
- 基本类型 number, bigint, string, boolean, null, undefined, symbol
- 引用类型 object(Array Function Date RegExp Error)

## 交互

- alert, prompt, confirm

## 类型转换与运算比较

- null => 0, undefined => NaN, NaN \*\* 0 == 1, NaN + 1 == NaN
- 加法从左到右运算，遇到字符串则转换为字符串
- 减法总是转换为数字
- 一元运算符优先级高于二元运算符
- 不同类型的值比较时，转化为数字（number）再判定大小, 相同类型的值比较时，直接比较且字符串比较时逐个比较字符编码
- null 只与 undefined 互等, 相等性检查 == 和普通比较符 > < >= <= 的代码逻辑是相互独立的, undefined 和 null 在相等性检查 == 中不会进行任何的类型转换

## 函数

- 函数表达式在执行流程到达时创建。
- 箭头函数: (...args) => expression, (...args) => { body }

## reference

- [JavaScript 特性](https://zh.javascript.info/javascript-specials)
