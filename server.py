#!/usr/bin/env python3
"""
Simple static file server for local network testing.

Run:
    python server.py
Then open from phone:
    http://<your-pc-lan-ip>:8000
"""

import http.server
import socket
import socketserver


PORT = 8000
HOST = "0.0.0.0"


def get_local_ip() -> str:
    """Best-effort LAN IP detection for display in logs."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # No packets are sent; this helps choose the active interface.
        sock.connect(("8.8.8.8", 80))
        return sock.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        sock.close()


def main() -> None:
    handler = http.server.SimpleHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer((HOST, PORT), handler) as httpd:
        local_ip = get_local_ip()
        print(f"Server pornit pe portul {PORT}")
        print(f"Local:   http://localhost:{PORT}")
        print(f"In retea: http://{local_ip}:{PORT}")
        print("Apasa Ctrl+C pentru oprire.")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
