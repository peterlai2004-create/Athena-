"""
Project Athena
check_hash.py

檢查 Hash 是否成功寫入 Database。
"""

import sqlite3

from config import DATABASE

conn = sqlite3.connect(DATABASE)

cursor = conn.cursor()

cursor.execute("""
SELECT
    filename,
    hash
FROM images
LIMIT 10
""")

rows = cursor.fetchall()

print("=" * 60)

for filename, image_hash in rows:

    print(filename)

    print(image_hash)

    print("-" * 60)

conn.close()