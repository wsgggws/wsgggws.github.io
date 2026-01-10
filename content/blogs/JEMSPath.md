+++
title = "JEMSPath"
date = 2024-08-01T10:50:18+08:00
tags = ["JSON", "JMESPath", "Query Language", "Python"]
categories = ["Tech", "Data"]
summary = "Overview of JMESPath, a query language for JSON, and its usage in data extraction."
+++

**JMESPath** (pronounced "James path") is a query language for JSON. It allows you to declaratively specify how to extract elements from a JSON document.

Unlike `jq`, which is a standalone CLI tool, JMESPath is often used as a library embedded in other languages (Python, JavaScript, Go, etc.) or tools (AWS CLI).

## Key Features

-   **Declarative**: Describe *what* you want, not *how* to get it.
-   **Portable**: Implementations available in many languages.

## Examples

Given the following JSON:
```json
{
  "locations": [
    {"name": "Seattle", "state": "WA"},
    {"name": "New York", "state": "NY"},
    {"name": "Bellevue", "state": "WA"},
    {"name": "Olympia", "state": "WA"}
  ]
}
```

### Basic Expressions

*   **Select list**: `locations`
*   **Filter list**: `locations[?state == 'WA']`
    *   Result: `[{"name": "Seattle", "state": "WA"}, ...]`
*   **Projection (Map)**: `locations[*].name`
    *   Result: `["Seattle", "New York", "Bellevue", "Olympia"]`
*   **Filter & Project**: `locations[?state == 'WA'].name`
    *   Result: `["Seattle", "Bellevue", "Olympia"]`

## Python Usage

```python
import jmespath

data = {"foo": {"bar": "baz"}}
result = jmespath.search('foo.bar', data)
print(result) # "baz"
```

## RTFM

- [JMESPath Tutorial](https://jmespath.org/tutorial.html) - The best place to start.
- [JMESPath Specification](https://jmespath.org/specification.html)
- [parsel](https://parsel.readthedocs.io/en/latest/) - A library that wraps JMESPath and XPath.
