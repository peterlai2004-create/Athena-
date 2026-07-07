"""
Project Athena

檢查 image_features。
"""

import sqlite3

from config import DATABASE

conn = sqlite3.connect(DATABASE)

cursor = conn.cursor()

cursor.execute("""
SELECT
    image_id,
    model

FROM image_features

LIMIT 20
""")

rows = cursor.fetchall()

print("=" * 50)

for row in rows:

    print(row)

print("=" * 50)

conn.close()