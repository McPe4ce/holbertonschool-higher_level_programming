#!/usr/bin/python3
"""Simple HTTP server serving plain text and JSON responses."""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class ApiSimple(BaseHTTPRequestHandler):
    """Request handler that responds to a few hardcoded endpoints."""

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Error 404")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), ApiSimple)
    print("Starting server on port 8000...")
    server.serve_forever()
