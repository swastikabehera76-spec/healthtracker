from database.queries import (
    db_user_get_all,
    db_user_get_one,
    db_user_create,
    db_user_update,
    db_user_delete
)

def service_get_all_users():
    return db_user_get_all()

def service_get_user(user_id):
    return db_user_get_one(user_id)

def service_create_user(data):
    return db_user_create(data)

def service_update_user(user_id, data):
    return db_user_update(user_id, data)

def service_delete_user(user_id):
    return db_user_delete(user_id)
