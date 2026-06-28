import sqlite3
from config import DATABASE_PATH

def connect_db():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn


def create_tables():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id TEXT UNIQUE,
    name TEXT,
    department TEXT,
    embedding TEXT
)
""")

    conn.commit()
    conn.close()


def add_employee(employee_id, name, department):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO employees(employee_id,name,department)
    VALUES(?,?,?)
    """, (employee_id, name, department))

    conn.commit()
    conn.close()


def employee_exists(employee_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM employees
    WHERE employee_id=?
    """, (employee_id,))

    row = cursor.fetchone()

    conn.close()

    return row


def get_all_employees():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_employee(employee_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM employees
    WHERE employee_id=?
    """, (employee_id,))

    conn.commit()

    conn.close()


create_tables()


def get_employee_by_id(employee_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM employees
    WHERE employee_id=?
    """,(employee_id,))

    row = cursor.fetchone()

    conn.close()

    return row


def get_employee_name(employee_id):

    employee = get_employee_by_id(employee_id)

    if employee:
        return employee[2]

    return None