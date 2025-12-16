from datetime import datetime
from database.connection import get_connection

# READ: get all users
def db_get_all_users():
    conn = get_connection()
    
    rows = conn.execute(
        "SELECT * FROM user_inputs ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]

# # READ: get single user by id
# def db_get_user(id):
#     conn = get_connection()
#     row = conn.execute(
#         "SELECT * FROM user_inputs WHERE id = ?",
#         (id,)
#     ).fetchone()
#     conn.close()
#     return dict(row) if row else None

# # CREATE: insert new user
# def db_create_user(data):
#     conn = get_connection()
#     now = datetime.now().isoformat()

#     cur = conn.execute(
#         """
#         INSERT INTO user_inputs (user_id, age, height, weight, gender, created_at)
#         VALUES (?, ?, ?, ?, ?, ?)
#         """,
#         (
#             data["user_id"],
#             data["age"],
#             data["height"],
#             data["weight"],
#             data["gender"],
#             now
#         )
#     )

#     conn.commit()
#     new_id = cur.lastrowid
#     conn.close()
#     return db_get_user(new_id)
