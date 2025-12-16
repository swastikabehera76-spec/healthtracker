from core.responses import send_json, send_404
from core.request import parse_json_body
from services.user_service import (
    service_get_all_users,
    # service_get_user,
    # service_create_user,
)

# READ: get all users
def get_all_users(handler):
    return send_json(handler, 200, service_get_all_users())

# READ: get single user by id
# def get_user_details(handler, user_id):
#     user = service_get_user(user_id)
#     return send_json(handler, 200, user) if user else send_404(handler)

# # CREATE: add new user
# def create_user_details(handler):
#     data = parse_json_body(handler)
#     new_user = service_create_user(data)
#     return send_json(handler, 201, new_user)
