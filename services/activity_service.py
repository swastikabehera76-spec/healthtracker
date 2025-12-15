# services/activity_service.py

from database.queries import (
    db_activity_get_all,
    db_activity_get_one,
    db_activity_create,
    db_activity_update,
    db_activity_delete
)

def service_get_all_activity():
    return db_activity_get_all()

def service_get_activity(activity_id):
    return db_activity_get_one(activity_id)

def service_create_activity(data):
    return db_activity_create(data)

def service_update_activity(activity_id, data):
    return db_activity_update(activity_id, data)

def service_delete_activity(activity_id):
    return db_activity_delete(activity_id)
