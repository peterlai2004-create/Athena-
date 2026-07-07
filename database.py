"""
Project Athena
database.py

負責建立與管理 SQLite Database。
"""

import sqlite3

from config import DATABASE


def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    # ==========================================
    # Images
    # ==========================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS images (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        path TEXT,

        filename TEXT,

        extension TEXT,

        size INTEGER,

        modified_time REAL,

        hash TEXT

    )
    """)

    cursor.execute("PRAGMA table_info(images)")

    columns = [column[1] for column in cursor.fetchall()]

    if "hash" not in columns:

        cursor.execute("""
        ALTER TABLE images
        ADD COLUMN hash TEXT
        """)

    # ==========================================
    # AI Features
    # ==========================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS image_features (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        image_id INTEGER,

        model TEXT,

        embedding BLOB,

        created_time REAL,

        FOREIGN KEY(image_id)
        REFERENCES images(id)

    )
    """)

    conn.commit()

    return conn, cursor