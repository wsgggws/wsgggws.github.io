+++
title = "jq"
date = 2024-07-31T10:50:18+08:00
tags = ["JSON", "CLI", "jq", "Data Processing"]
categories = ["Tech", "Tools"]
summary = "Introduction to jq, a lightweight and flexible command-line JSON processor."
image = "/images/covers/jq.png"
+++

**jq** is a lightweight and flexible command-line JSON processor. It is like `sed` for JSON data - you can use it to slice and filter and map and transform structured data with the same ease that `sed`, `awk`, `grep` and friends let you play with text.

## Installation

```bash
brew install jq
```

## Common Usage Examples

### 1. Prettify JSON
Format JSON output to be readable:

```bash
echo '{"foo": "bar"}' | jq .
```

### 2. Extract a Value
Get the value of a specific key:

```bash
echo '{"foo": "bar"}' | jq '.foo'
# Output: "bar"
```

### 3. Filter Array
Process elements in an array:

```bash
echo '[{"id":1}, {"id":2}]' | jq '.[].id'
# Output:
# 1
# 2
```

### 4. Select Objects
Filter objects based on a condition:

```bash
echo '[{"id":1, "active":true}, {"id":2, "active":false}]' | jq '.[] | select(.active==true)'
```

### 5. Construct New JSON
Create a new JSON structure from input:

```bash
echo '{"user":"navy", "age":30}' | jq '{name: .user, year: .age}'
# Output: { "name": "navy", "year": 30 }
```

## RTFM

- [jq Manual](https://stedolan.github.io/jq/manual/)
- [jq Playground](https://jqplay.org/)
