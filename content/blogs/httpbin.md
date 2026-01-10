+++
title = "HttpBin"
date = 2024-08-23T17:50:18+08:00
tags = ["HTTP", "API", "Debugging", "Tools"]
categories = ["Tech", "Debugging"]
summary = "How to use HttpBin to debug HTTP requests and inspect parameters."
+++

**HttpBin** is a simple HTTP request & response service. It is incredibly useful when you need to verify if your HTTP client (curl, Python requests, Go http, etc.) is sending the data you expect.

## Common Endpoints

### 1. Inspect Request Data
Verify headers, query params, and body.

*   `GET /get`: Returns GET arguments.
*   `POST /post`: Returns POST data.
*   `PUT /put`: Returns PUT data.

**Example:**
Check if your query parameters are encoded correctly.
```bash
curl "https://httpbin.org/get?name=navy&age=30"
```
Response:
```json
{
  "args": {
    "age": "30",
    "name": "navy"
  },
  ...
}
```

### 2. Inspect Headers
Check if your custom headers are actually being sent.

```bash
curl -H "X-Custom-Header: value" https://httpbin.org/headers
```

### 3. Test Status Codes
Check how your application handles different HTTP errors.

*   `GET /status/:code`: Returns given HTTP Status code.

```bash
# Test 404 handling
curl -I https://httpbin.org/status/404

# Test 500 handling
curl -I https://httpbin.org/status/500
```

### 4. Test Response Formats
*   `GET /json`: Returns a simple JSON object.
*   `GET /xml`: Returns a simple XML document.

## Debugging Scenario

Imagine you have a complex XML payload that fails on the production server. You can't see what the server receives.

1.  **Change the URL**: Point your client to `https://httpbin.org/post`.
2.  **Send Request**: Trigger the action in your app.
3.  **Inspect Response**: HttpBin will echo back *exactly* what it received (headers, body content type, raw string).
4.  **Compare**: You might find that your library added an extra wrapper or the encoding was wrong.

Useful URL: <https://httpbin.org/>
