#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime, timezone
import os
import socket

PORT = int(os.environ.get("PORT", "8080"))

class SimpleHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.end_headers()

    def do_GET(self):
        if self.path != "/":
            self.send_error(404, "Not Found")
            return
        self._set_headers()
        # client IP from socket (works behind proxies if you forward real IP)
        client_ip = self.client_address[0]
        payload = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "ip": client_ip
        }
        self.wfile.write(json.dumps(payload, ensure_ascii=False).encode("utf-8"))

    # keep log minimal
    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), SimpleHandler)
    print(f"SimpleTimeService listening on 0.0.0.0:{PORT} ... (serve / )")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
