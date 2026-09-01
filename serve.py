#!/usr/bin/env python3
"""Local static server for the agent demos site."""

from __future__ import annotations

import http.server
import os
import socket
import socketserver
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
DEFAULT_PORT = 8080
MAX_TRIES = 20


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args) -> None:
        sys.stderr.write("%s - - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), format % args))


def pick_port(start: int = DEFAULT_PORT) -> int:
    for port in range(start, start + MAX_TRIES):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((HOST, port))
            except OSError:
                continue
            return port
    raise SystemExit(f"No free port found between {start} and {start + MAX_TRIES - 1}.")


def main() -> None:
    os.chdir(ROOT)
    preferred = int(os.environ.get("PORT", DEFAULT_PORT))
    port = pick_port(preferred)

    if port != preferred:
        print(f"Port {preferred} is in use — using {port} instead.", file=sys.stderr)

    with socketserver.TCPServer((HOST, port), QuietHandler) as httpd:
        print(f"Serving {ROOT}")
        print(f"  → http://{HOST}:{port}/")
        print(f"  → http://localhost:{port}/")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
