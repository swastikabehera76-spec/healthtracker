from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
from datetime import datetime

from controllers.user import (
    # create_user_details,
    get_all_users,
)

from core.responses import send_404
from core.middleware import add_cors_headers


class HealthRouter(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        add_cors_headers(self)
        self.end_headers()

    # ------------------------
    # READ USER (GET)
    # ------------------------
    def do_GET(self):
        path = urlparse(self.path).path
        print("PATH:", path)

        if path == "/api/users":
            return get_all_users(self)

        return send_404(self)

    # # ------------------------
    # # CREATE USER (POST)
    # # ------------------------
    # def do_POST(self):
    #     if self.path == "/api/user/details":
    #         return create_user_details(self)

    #     return send_404(self)

    # ------------------------
    # LOGGER
    # ------------------------
    def log_message(self, format, *args):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [Server] {format % args}")

