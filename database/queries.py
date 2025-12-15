# database/queries.py
from datetime import datetime
from .connection import get_connection

# USERS (AUTH) — login, register, update, delete

def db_register_user(data):
    conn = get_connection()
    now = datetime.now().isoformat()

    cur = conn.execute("""
        INSERT INTO users (name, email, password, created_at)
        VALUES (?, ?, ?, ?)
    """, (data["name"], data["email"], data["password"], now))

    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return db_get_user(new_id)


def db_login_user(email, password):
    conn = get_connection()
    row = conn.execute("""
        SELECT * FROM users WHERE email=? AND password=?
    """, (email, password)).fetchone()
    conn.close()
    return dict(row) if row else None


def db_get_user(user_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def db_update_user(user_id, data):
    conn = get_connection()
    now = datetime.now().isoformat()

    conn.execute("""
        UPDATE users SET name=?, email=?, password=?, updated_at=?
        WHERE id=?
    """, (data["name"], data["email"], data["password"], now, user_id))

    conn.commit()
    conn.close()
    return db_get_user(user_id)


def db_delete_user(user_id):
    user = db_get_user(user_id)
    if not user:
        return None

    conn = get_connection()
    conn.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    return user

# USER INPUT CRUD (age, height, weight, gender)

def db_create_user_input(data):
    conn = get_connection()
    now = datetime.now().isoformat()

    cur = conn.execute("""
        INSERT INTO user_input (user_id, age, height, weight, gender, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (data["user_id"], data["age"], data["height"], data["weight"], data["gender"], now))

    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return db_get_user_input(new_id)


def db_get_user_input(input_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM user_input WHERE id=?", (input_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def db_get_all_user_inputs(user_id):
    conn = get_connection()
    rows = conn.execute("SELECT * FROM user_input WHERE user_id=? ORDER BY id DESC", (user_id,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def db_update_user_input(input_id, data):
    conn = get_connection()
    now = datetime.now().isoformat()

    conn.execute("""
        UPDATE user_input SET age=?, height=?, weight=?, gender=?, updated_at=?
        WHERE id=?
    """, (data["age"], data["height"], data["weight"], data["gender"], now, input_id))

    conn.commit()
    conn.close()
    return db_get_user_input(input_id)


def db_delete_user_input(input_id):
    old = db_get_user_input(input_id)
    if not old:
        return None

    conn = get_connection()
    conn.execute("DELETE FROM user_input WHERE id=?", (input_id,))
    conn.commit()
    conn.close()
    return old

# DAILY ACTIVITY CRUD (water, steps, calories)

def db_create_activity(data):
    conn = get_connection()
    now = datetime.now().isoformat()

    cur = conn.execute("""
        INSERT INTO daily_activity (user_id, water, steps, calories, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (data["user_id"], data["water"], data["steps"], data["calories"], now))

    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return db_get_activity(new_id)


def db_get_activity(activity_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM daily_activity WHERE id=?", (activity_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def db_get_all_activities(user_id):
    conn = get_connection()
    rows = conn.execute("""
        SELECT * FROM daily_activity 
        WHERE user_id=?
        ORDER BY id DESC
    """, (user_id,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def db_update_activity(activity_id, data):
    conn = get_connection()
    now = datetime.now().isoformat()

    conn.execute("""
        UPDATE daily_activity
        SET water=?, steps=?, calories=?, updated_at=?
        WHERE id=?
    """, (data["water"], data["steps"], data["calories"], now, activity_id))

    conn.commit()
    conn.close()
    return db_get_activity(activity_id)


def db_delete_activity(activity_id):
    old = db_get_activity(activity_id)
    if not old:
        return None

    conn = get_connection()
    conn.execute("DELETE FROM daily_activity WHERE id=?", (activity_id,))
    conn.commit()
    conn.close()
    return old

# MEDICAL RECORD CRUD (previous, current, genetic)

def db_create_medical(data):
    conn = get_connection()
    now = datetime.now().isoformat()

    cur = conn.execute("""
        INSERT INTO medical_records (user_id, previous, current, genetic, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (data["user_id"], data["previous"], data["current"], data["genetic"], now))

    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return db_get_medical(new_id)


def db_get_medical(med_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM medical_records WHERE id=?", (med_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def db_get_all_medicals(user_id):
    conn = get_connection()
    rows = conn.execute("""
        SELECT * FROM medical_records WHERE user_id=? ORDER BY id DESC
    """, (user_id,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def db_update_medical(med_id, data):
    conn = get_connection()
    now = datetime.now().isoformat()

    conn.execute("""
        UPDATE medical_records
        SET previous=?, current=?, genetic=?, updated_at=?
        WHERE id=?
    """, (data["previous"], data["current"], data["genetic"], now, med_id))

    conn.commit()
    conn.close()
    return db_get_medical(med_id)


def db_delete_medical(med_id):
    old = db_get_medical(med_id)
    if not old:
        return None

    conn = get_connection()
    conn.execute("DELETE FROM medical_records WHERE id=?", (med_id,))
    conn.commit()
    conn.close()
    return old

