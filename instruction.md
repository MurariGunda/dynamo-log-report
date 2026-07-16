An Apache-style access log is at /app/access.log. Each line has the common log format: client IP first, then identity, user, timestamp in brackets, the quoted request line ("METHOD path HTTP/version"), status code, and response size.

Analyze the log and write a summary report to /app/report.json. The file must contain a single JSON object with exactly these three keys:

- "total_requests": integer — the total number of request lines in the log
- "unique_ips": integer — the number of distinct client IP addresses
- "top_path": string — the request path that appears most often in the log

Success criteria:

1. /app/report.json exists and contains a single valid JSON object.
2. Its "total_requests" value is an integer equal to the total number of request lines in /app/access.log.
3. Its "unique_ips" value is an integer equal to the number of distinct client IP addresses in the log.
4. Its "top_path" value is a string equal to the request path that occurs most frequently in the log.
