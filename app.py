#!/usr/bin/env python3
"""HealthViewer — Minimal web server for the health dashboard."""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os


PORT = 8080
INDEX_PATH = os.path.join(os.path.dirname(__file__), "public", "index.html")


class HealthViewerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self._serve_html()
        elif self.path.startswith("/api/"):
            self._serve_json()
        else:
            self.send_error(404, "Not Found")

    def _serve_html(self):
        with open(INDEX_PATH, "rb", encoding="utf-8") as f:
            body = f.read()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_json(self):
        data = {"message": "HealthViewer API"}
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def log_message(self, format, *args):
        pass  # suppress server logs


if __name__ == "__main__":
    print(f"HealthViewer running at http://localhost:{PORT}")
    with HTTPServer(("", PORT), HealthViewerHandler) as srv:
        srv.serve_forever()
