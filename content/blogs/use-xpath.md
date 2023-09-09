---
title: "Use XPath"
date: 2023-03-16T12:50:18+08:00
weight: 1
aliases: ["/blogs"]
tags: ["XPATH"]
author: "Navy"
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
description: ""
canonicalURL: "https://canonical.url/to/page"
disableHLJS: true # to disable highlightjs
disableShare: false
disableHLJS: false
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
cover:
    image: "<image path/url>" # image path/url
    alt: "<alt text>" # alt text
    caption: "<text>" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: true # only hide on current single page
editPost:
    URL: "https://github.com/wsgggws/wsgggws.github.io/blob/main/content"
    Text: "Edit" # edit text
    appendFilePath: true # to append file path to Edit link
---

## What is XPath?

XPath(XML Path Language) 通过“路径表达式” 在 XML/HTML 文本中选择节点。

### tips!

1. 公式可以表达为: /node1[node2[predicate1]] | /node3[predicate2][predicate3], 即 Unionable, Chainable, Nestable
2. text() 也是一个节点, 即可以对它使用 predicate
3. $x("//strong[contains(text(), 'Order #')]/parent::td/text()[re:match(., 'W\\d{14}')]") 可在 Chrome Console 中使用

### Descendant selectors

- "/"
- "//h1"
- "//ul/li/a"
- "//div/\*"

### Attribute selectors

- "//button/text()[.='Submit']"
- "//\*[@class='class']"
- "//a[@id="abc"][@for="xyz"]"
- "//a[@name or @href]"
- "//a[starts-with(@href, '/')]"
- "//a[ends-with(@href, '.pdf')]"
- "//a[contains(@href, '://')]"
- "//h1[not(@id)]"
- "//button[text()='Submit']"
- "//product[@price > 2.50]"
- "//a[@id != 'xyz']"
- "//div[@id='head' and position()=2]"
- "//ul[count(li) > 2]"

### Order selectors

- "//ul/li[1]"
- "//ul/li[last()]"
- "//ol/li[position()>1]"
- "//li[1][@id='id']"
- "//\*[last()][name()='a']"

### Axes

- "//h1/following-sibling::ul"
- "//h1/following-sibling::ul[1]"
- "//h1/preceding-sibling::[@id='id']"
- "//ul/descendant-or-self::li"
- "//ul/ancestor-or-self::li"
- "./ancestor-or-self::[@class='box']"
- "//section[h1[@id='section-name']]"
- "//section[//h1[@id='section-name']]"
- "ancestor"
- "ancestor-or-self"
- "attribute"
- "child"
- "descendant"
- "descendant-or-self"
- "namespace"
- "self"
- "parent"
- "following"
- "following-sibling"
- "preceding"
- "preceding-sibling"

### Unions Operators

- "//a | //div"

### Chaining order

- "a[1][@href='/']"

### Nesting predicates

- "//section[.//h1[@id='hi']]"

### Node functions

"name()"
"text()"
"lang(str)"
"namespace-uri()"
"count()"
"position()"

### Boolean functions

- "not(expr)"

### String functions

- "contains()"
- "starts-with()"
- "ends-with()"
- "concat(x,y)"
- "substring(str, start, len)"
- "substring-before('01/02', '/')"
- "substring-after('01/02', '/')"
- "translate()"
- "normalize-space()"
- "string-length()"

### Type conversion

- "string()"
- "number()"
- "boolean()"

## Notes!!!

在浏览器中能执行的 xpath 为什么在 expression 提取不到结果， 这个要对比浏览器中的 html 跟显示网页源代码中的 html 有什么不一样，一般有这几种情况

1. **浏览器给 html 加标签了，比如 table 的子节点的会加一层 tbody 标签**
2. 原来的 html 标签开合不匹配或者标签 id 重复，xpath 库解析 html 报错（调试时会有日志），但是浏览器自动修复了或者忽略错误了，这种情况可以通过 regex_replace 对 email.body 进行修复
3. 如果是 follow link 获取到的 html，可能有某些 header 缺失或者 cookie 问题导致获取到的 html 结构不一样，要对比一下获取到的 html 和浏览器的 html 是否一样
4. 在 chrome 浏览器里调试 xpath 可以用 `$x(xpath_pattern)` 的方式，比如 `$x("//strong[contains(text(), 'Order #')]/parent::td/text()[re:match(., 'W\\d{14}')]")`
5. 我们在 expression 里支持了拓展正则表达式，可以用 `re:match(text, pattern)` 的方式来做正则匹配，但是这个运算不能在浏览器里面执行

## XPath examples

```html
<div>
  <!-- author introduction -->
  <div>
    <img src="https://avatars.githubusercontent.com/u/20469245?s=40&v=4" />
    <span>码码要洗手</span>
    <span><a id="github" href="https://github.com/wsgggws">Github</a></span>
    <span
      ><a id="bili" href="https://space.bilibili.com/472722204">Bili</a></span
    >
  </div>
  <br />

  <div>
    <span
      >XPath(XML Path Language) 通过“路径表达式” 在 XML/HTML
      文本中选择节点。</span
    >
    <br />
    <span id="summary"
      >公式表示为: <b>/nodes[predicates]</b>, 即
      /node1[predicate1][predicate2]//node2/node3[predicate3] |
      /node4[predicate4]
    </span>
  </div>
  <br />
  <div id="node">
    <h3>Nodes(节点)</h3>
    <!-- node -->
    <table>
      <tr>
        <th>Element</th>
        <td>/, //, table, span, ...</td>
      </tr>
      <tr>
        <th>Attribute</th>
        <td>@class, @id, @href, @src, ...</td>
      </tr>
      <tr>
        <th>Text</th>
        <td>text()</td>
      </tr>
      <tr>
        <th>Comment</th>
        <td>comment()</td>
      </tr>
      <tr>
        <th>Axes</th>
        <td>preceding-sibling::, following-sibling::, ancestor, ...</td>
      </tr>
    </table>
  </div>

  <div class="predicate">
    <h3>Predicates(谓语条件)</h3>
    <!-- predicate -->
    <table>
      <tr>
        <th>索引</th>
        <td>1, last(), position(), count(), ...</td>
      </tr>
      <tr>
        <th>算术运算</th>
        <td>=, !=, >, <, ...</td>
      </tr>
      <tr>
        <th>逻辑运算</th>
        <td>and, or, not, ...</td>
      </tr>
      <tr>
        <th>字符串判断</th>
        <td>starts-with(), ends-with(), contains(), normalize-space(), ...</td>
      </tr>
      <!-- special tr start -->
      <tr>
        <th>字符串处理</th>
        <td>substring-before(), substring-after(), concat(), ...</td>
      </tr>
      <!-- special tr end -->
      <tr>
        <th>没有td ;)</th>
      </tr>
      <tr>
        <th>连接多个 Xpath</th>
        <td>|</td>
      </tr>
    </table>
  </div>
  <div class="description">
    <h3>Notes!!!</h3>
    <h4>
      在浏览器中能执行的 xpath 为什么在 expression 提取不到结果，
      这个要对比浏览器中的 html 跟显示网页源代码中的 html
      有什么不一样，一般有这几种情况
    </h4>
    <ul>
      <li>
        1. **浏览器给 html 加标签了，比如 table 的子节点的会加一层 tbody 标签**
      </li>
      <li>
        2. 原来的 html 标签开合不匹配或者标签 id 重复，xpath 库解析 html
        报错（调试时会有日志），但是浏览器自动修复了或者忽略错误了，这种情况可以通过
        regex_replace 对 email.body 进行修复
      </li>
      <li>
        3. 如果是 follow link 获取到的 html，可能有某些 header 缺失或者 cookie
        问题导致获取到的 html 结构不一样，要对比一下获取到的 html 和浏览器的
        html 是否一样
      </li>
      <li>
        4. 在 chrome 浏览器里调试 xpath 可以用 `$x(xpath_pattern)` 的方式，比如
        `$x("//strong[contains(text(), 'Order #')]/parent::td/text()[re:match(.,
        'W\\d{14}')]")`
      </li>
      <li>
        5. 我们在 expression 里支持了拓展正则表达式，可以用 `re:match(text,
        pattern)` 的方式来做正则匹配，但是这个运算不能在浏览器里面执行
      </li>
    </ul>
  </div>
</div>
```

```bash
# 获取 element
//table/t
```
