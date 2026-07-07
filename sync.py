"""
Project Athena

sync.py

比較資料夾與 Database。
"""

from config import IMAGE_FOLDER
from config import IMAGE_EXTENSIONS


def get_disk_files():

    files = set()

    for file in IMAGE_FOLDER.rglob("*"):

        if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS:

            files.add(str(file))

    return files


def get_database_files(cursor):

    cursor.execute("""
    SELECT path
    FROM images
    """)

    return {row[0] for row in cursor.fetchall()}


def compare(cursor):

    disk = get_disk_files()

    database = get_database_files(cursor)

    added = disk - database

    removed = database - disk

    print("=" * 60)

    print(f"新增圖片：{len(added)}")

    for path in sorted(added):

        print(path)

    print()

    print(f"刪除圖片：{len(removed)}")

    for path in sorted(removed):

        print(path)

    print("=" * 60)