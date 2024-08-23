+++
title = "HttpBin"
date =  2024-08-23T17:50:18+08:00
+++

当你有 CURL 命令并且能够请求到数据，但请求参数复杂，例如 GET 请求参数里直接嵌套 xml 或者 json 数据。
你使用 Python 或者 Go 语言进行改写，请求时却又发现请求参数不正确，这时候你可以使用 [httpbin](https://httpbin.org/) 进行调试。

- CULR 请求 <https://httpbin.org/get?xml={xml}>, 它会返回你的请求参数A
- 代码里请求替换 URL 为 <https://httpbin.org/get?xml={xml}>, 它会返回你的请求参数B

对比 A 和 B，你就能发现代码里请求参数的问题了。

更多请求细节可查看 <https://httpbin.org/>
