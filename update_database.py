import sqlite3
from config import DATABASE_PATH

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

try:
    cursor.execute("""
        ALTER TABLE employees
        ADD COLUMN embedding TEXT
    """)
    print("✅ 'embedding' column added successfully.")
except sqlite3.OperationalError as e:
    print("ℹ️", e)

conn.commit()
conn.close()

print("Database update completed.")