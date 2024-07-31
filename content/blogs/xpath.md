+++
title = "XPath"
date = 2024-07-31T10:50:18+08:00
+++

XPath(XML/HTML Path Language): Query language for XML/HTML.

[本人在线操作 XPath 视频版点这里](https://www.bilibili.com/video/BV1Kd4y1R7Bt/)

## XPath 表达式构成

|  Component  |         Example         |
| :---------: | :---------------------: |
|   分隔符    |          /, //          |
| 节点(标签)  |     div, tr, td ...     |
| 节点(属性)  |     @class，@id ...     |
| 节点(文本)  |  text()，comment() ...  |
| 限定符/谓语 |           []            |
|     轴      | following-sibling:: ... |
|    函数     |    starts-with() ...    |
|   操作符    |   and, or, >=, <= ...   |

## 如何使用 XPath

- Chrome Elements
  ![Elements](/images/xpath/elements.png)
- Chrome Console
  ![Console](/images/xpath/console.png)
- Scrapy shell
  ![Scrapy](/images/xpath/scrapy.png)

## XPath 案例

|                            XPath                            | Comment  |
| :---------------------------------------------------------: | :------: |
|                          //ul/li/a                          |  纯节点  |
|                //button/text()\[.=‘Submit’\]                |  限定符  |
|               //a\[@id=“abc”\]\[@for=“xyz”\]                | 多限定符 |
|                    //a\[@name or @href\]                    |  操作符  |
|               //a\[starts-with(@href, “/”)\]                |   函数   |
| //ul\[count(li) > 2 and li\[ends-with(@class, “active”)\]\] | 复合条件 |
|                      //ul/li\[last()\]                      |   位置   |
|                 //h1/following-sibling::ul                  |    轴    |
|      //div\[count(./div)=2\] \| //tr\[count(./td)=2\]       |   合集   |

## XPath 要注意的 11 个点

1. 返回的是节点集合。
1. text() 也是节点，可以限定。
1. [] 可联结(Chainable: `[][]`), 可嵌套(Nestable: `[[]]`)。
1. 路径表达式可以通过 "|" 获取合集。
1. source code 里 **tbody** 标签可能不存在。
1. 善用函数 `substring-before(XPath, "split_str")`, `concat(XPath, XPath)`。
1. 注意函数的作用域，往往只作用于节点集的第一个节点。
1. 当前节点它是一个引用，依然可以搜索整棵树。
1. 可结合 re 的功能。
1. 强烈推荐 Python package parsel，它还支持 JMESPath。
1. 如果是 XML 类型，需要声明 namespace 及替换没有 namespace 的 soap。

## 参考

- [XPath cheatsheet](https://devhints.io/xpath)
- [XPath tips](https://www.zyte.com/blog/xpath-tips-from-the-web-scraping-trenches/)
- [XPath functions](https://developer.mozilla.org/en-US/docs/Web/XPath/Functions)
