from datetime import datetime
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from controllers.auth import ( 
login_user, 
register_user, 
update_user,
delete_user
)

from controllers.responses import (
    save_user_details,
    get_user_details,
    update_user_details,
    delete_user_details
)

from controllers.activity import (
    add_activity_record,
    get_activity_records,
    update_activity_record,
    delete_activity_record
)

from controllers.medical import (
    add_medical_record,
    get_medical_records,
    update_medical_record,
    delete_medical_record
)

from core.static import serve_static
from core.responses import send_404
from core.middleweare import add_cors_headers


class HealthRouter(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        add_cors_headers(self)
        self.end_headers()

# READ
def do_GET(self):
    path = urlparse(self.path).path

    if handle_ui_router(self, path):
        return
    
    # AUTH
    if path == "/api/auth/user":
        return get_user_details(self)
    
    # USER PERSONAL DETAILS 
    if path == "/api/details":
        return get_user_details(self)
    
    # DAILY ACTIVITY 
    if path == "/api/activity":
        return get_activity_records(self)
    
    # MEDICAL 
    if path == "/api/medical":
        return get_medical_records(self)
    
    return send_404(self)

# CREATE 
def do_POST(self):

    if self.path == "/api/auth/login":
        return login_user(self)
    
    if self.path == "/api/auth/register":
        return register_user(self)

        # USER DETAILS
    if self.path == "/api/user/details":
        return save_user_details(self)

     # ACTIVITY
    if self.path == "/api/activity":
        return add_activity_record(self)

    # MEDICAL
    if self.path == "/api/medical":
        return add_medical_record(self)

    return send_404(self)


# UPDATE 
def do_PUT(self):
    path = self.path

    # AUTH UPDATE
    if path == "/api/auth/update":
        return update_user(self)

    # USER DETAILS UPDATE
    if path == "/api/user/details":
        return update_user_details(self)

    # ACTIVITY UPDATE
    if path.startswith("/api/activity/"):
        record_id = int(path.split("/")[-1])
        return update_activity_record(self, record_id)

    # MEDICAL UPDATE
    if path.startswith("/api/medical/"):
        record_id = int(path.split("/")[-1])
        return update_medical_record(self, record_id)

    return send_404(self)


# DELETE 
def do_DELETE(self):
    path = self.path

    # AUTH DELETE
    if path == "/api/auth/delete":
        return delete_user(self)

    # USER DETAILS DELETE
    if path == "/api/user/details":
        return delete_user_details(self)

    # DELETE ACTIVITY
    if path.startswith("/api/activity/"):
        record_id = int(path.split("/")[-1])
        return delete_activity_record(self, record_id)

    # DELETE MEDICAL
    if path.startswith("/api/medical/"):
        record_id = int(path.split("/")[-1])
        return delete_medical_record(self, record_id)

    return send_404(self)

# LOGGER 
def log_messager(self, format, *args):
    timestamp = datetime.new().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [Server] {format % args}")
