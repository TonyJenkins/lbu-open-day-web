#!/usr/bin/env python3
"""
Simple HTTP server to serve the LBU Software Engineering promotional website.
Serves static files on port 8080.
"""

import http.server
import socketserver
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler to serve files from the script's directory."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


def main():
    """Start the HTTP server on port 8080."""
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print(f"Server running at http://localhost:{PORT}/")
            print(f"Serving files from: {DIRECTORY}")
            print("Press Ctrl+C to stop the server")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"Error: Port {PORT} is already in use.")
            print("Please stop the other process or use a different port.")
            sys.exit(1)
        else:
            raise


if __name__ == "__main__":
    main()
