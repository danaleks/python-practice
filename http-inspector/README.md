# HTTP Request Inspector

A Python tool to inspect HTTP requests and responses in detail.

## What it does

- Inspects HTTP requests (GET, POST, PUT, DELETE)
- Shows request/response headers
- Displays status codes and timing
- Compares different HTTP methods
- Analyzes response body (JSON/text)

## What I learned

- HTTP methods and their differences
- Request/response headers
- Status codes (2xx, 4xx, 5xx)
- HTTP protocol basics
- Request/response cycle

## Usage

python http_inspector.py


### Examples

**Option 1: Inspect GET request**
URL: httpbin.org/get


**Option 3: Compare all methods**
- Automatically tests GET, POST, PUT, DELETE on httpbin.org
- Shows status codes and timing for each method

## Technical details

- Uses `requests` library
- Timeout: 5 seconds
- Supports JSON payloads
- Shows HTTP version, encoding, cookies

## Requirements

pip install requests
