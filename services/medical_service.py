# services/medical_service.py

from database.queries import (
    db_medical_get_all,
    db_medical_get_one,
    db_medical_create,
    db_medical_update,
    db_medical_delete
)

def service_get_all_medical():
    return db_medical_get_all()

def service_get_medical(medical_id):
    return db_medical_get_one(medical_id)

def service_create_medical(data):
    return db_medical_create(data)

def service_update_medical(medical_id, data):
    return db_medical_update(medical_id, data)

def service_delete_medical(medical_id):
    return db_medical_delete(medical_id)
