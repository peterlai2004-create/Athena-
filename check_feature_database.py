"""
Project Athena

檢查 image_features 是否建立成功。
"""

import sqlite3

from config import DATABASE

conn = sqlite3.connect(DATABASE)

cursor = conn.cursor()

cursor.execute("""

SELECT name

FROM sqlite_master

WHERE type='table'

""")

tables = cursor.fetchall()

print("=" * 50)

for table in tables:

    print(table[0])

print("=" * 50)

conn.close()