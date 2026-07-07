"""
Project Athena
duplicate_finder.py

找出重複圖片。
"""

import sqlite3

from config import DATABASE


def find_duplicates():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        hash,
        COUNT(*)

    FROM images

    GROUP BY hash

    HAVING COUNT(*) > 1
    """)

    duplicates = cursor.fetchall()

    if len(duplicates) == 0:

        print("沒有找到重複圖片。")

        conn.close()

        return

    print("=" * 60)

    print("找到重複圖片")

    print("=" * 60)

    for image_hash, count in duplicates:

        print()

        print(f"Hash：{image_hash}")

        print(f"共有 {count} 張")

        cursor.execute("""
        SELECT path

        FROM images

        WHERE hash = ?
        """, (image_hash,))

        rows = cursor.fetchall()

        for row in rows:

            print(row[0])

        print("-" * 60)

    conn.close()