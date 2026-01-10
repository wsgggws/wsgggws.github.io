+++
title = "JavaScript 特性"
date = 2024-08-05T21:13:46+08:00
tags = ["JavaScript", "Frontend", "Cheatsheet"]
categories = ["Tech"]
summary = "A quick reference specifically for JavaScript types, interactions, and operations."
image = "/images/covers/javascript-specials.png"
+++

## 1. 变量声明 (Variable Declaration)

*   `var`: 函数作用域，可被提升 (Hoisting)，尽量少用。
*   `let`: 块级作用域，不可重复声明。
*   `const`: 块级作用域，常量（引用地址不变）。

## 2. 数据类型 (Data Types)

可以使用 `typeof` 操作符查看类型。

### 基本类型 (Primitives)
*   `number`: 整数或浮点数。 `typeof 123` -> `"number"`
*   `bigint`: 大整数。 `typeof 10n` -> `"bigint"`
*   `string`: 字符串。
*   `boolean`: `true` / `false`.
*   `null`: 空值。 **注意**: `typeof null` 是 `"object"` (历史遗留 Bug)。
*   `undefined`: 未定义。
*   `symbol`: 唯一标识符。

### 引用类型 (Reference Types)
*   `object`: 包括 Array, Function, Date, RegExp, Error 等。

## 3. 用户交互 (Interaction)

```javascript
alert("Hello");              // 仅确认
let age = prompt("How old?", 18); // 输入框
let isBoss = confirm("Are you the boss?"); // 确认/取消 (true/false)
```

## 4. 类型转换与运算 (Type Conversion & Coercion)

JavaScript 的隐式转换是著名的坑。

### String Conversion
```javascript
String(123)   // "123"
123 + ""      // "123"
```

### Numeric Conversion
```javascript
Number("123") // 123
+"123"        // 123
Number(true)  // 1
Number(null)  // 0
Number(undefined) // NaN
```

### Boolean Conversion
Falsy values: `0`, `""`, `null`, `undefined`, `NaN`, `false`. All others are `true`.

### 奇怪的特性 (The "Wat" moments)

```javascript
null > 0;  // false
null == 0; // false
null >= 0; // true (Here null is converted to 0)

undefined > 0; // false
undefined < 0; // false
undefined == 0; // false (Undefined only equals null or undefined)

"2" > 1;   // true (String converted to number)
"01" == 1; // true
```

*   **加法 (`+`)**: 如果有一方是字符串，另一方也会转换为字符串。
*   **减法/乘法/除法**: 总是尝试转换为数字。

```javascript
2 + 2 + '1'; // "41"
'1' + 2 + 2; // "122"
'6' / '2';   // 3
```
- 一元运算符优先级高于二元运算符
- 不同类型的值比较时，转化为数字（number）再判定大小, 相同类型的值比较时，直接比较且字符串比较时逐个比较字符编码
- null 只与 undefined 互等, 相等性检查 == 和普通比较符 > < >= <= 的代码逻辑是相互独立的, undefined 和 null 在相等性检查 == 中不会进行任何的类型转换

## 函数

- 函数表达式在执行流程到达时创建。
- 箭头函数: (...args) => expression, (...args) => { body }

## reference

- [JavaScript 特性](https://zh.javascript.info/javascript-specials)
