#!/usr/bin/env python3
"""
Simple Python web server for the business website.
This serves the static HTML, CSS, and image files.
"""

import http.server
import socketserver
import os
import webbrowser
from threading import Timer

# Configuration
PORT = 8001
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve files with proper MIME types"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add some security headers
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Custom log format"""
        print(f"[{self.address_string()}] {format % args}")

def open_browser():
    """Open the website in the default browser after a short delay"""
    webbrowser.open(f'http://localhost:{PORT}')

def main():
    """Start the web server"""
    try:
        # Change to the directory containing the website files
        os.chdir(DIRECTORY)
        
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print(f"Business Website Server")
            print(f"Serving at http://localhost:{PORT}")
            print(f"Serving files from: {DIRECTORY}")
            print("\nPress Ctrl+C to stop the server")
            
            # Open browser after 1 second
            Timer(1.0, open_browser).start()
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"Port {PORT} is already in use. Try a different port or stop the existing server.")
        else:
            print(f"Error starting server: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()