"""
Project Athena

scanner.py

負責同步圖片與 Database。
"""

from config import IMAGE_FOLDER
from config import IMAGE_EXTENSIONS
from hash_engine import calculate_hash


def scan_images(cursor):

    cursor.execute("""
    SELECT
        path,
        modified_time
    FROM images
    """)

    database = {
        row[0]: row[1]
        for row in cursor.fetchall()
    }

    disk_paths = set()

    count = 0
    new_count = 0
    update_count = 0

    for file in IMAGE_FOLDER.rglob("*"):

        if not file.is_file():
            continue

        if file.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        count += 1

        path = str(file)

        disk_paths.add(path)

        modified_time = file.stat().st_mtime

        # 新圖片
        if path not in database:

            new_count += 1

            print(f"[新增] {file.name}")

            image_hash = calculate_hash(file)

            cursor.execute(
                """
                INSERT INTO images
                (path, filename, extension, size, modified_time, hash)

                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    path,
                    file.name,
                    file.suffix.lower(),
                    file.stat().st_size,
                    modified_time,
                    image_hash,
                ),
            )

            continue

        # 已修改
        if modified_time != database[path]:

            update_count += 1

            print(f"[更新] {file.name}")

            image_hash = calculate_hash(file)

            cursor.execute(
                """
                UPDATE images

                SET

                    size = ?,

                    modified_time = ?,

                    hash = ?

                WHERE path = ?
                """,
                (
                    file.stat().st_size,
                    modified_time,
                    image_hash,
                    path,
                ),
            )

    removed = set(database.keys()) - disk_paths

    remove_count = 0

    for path in removed:

        cursor.execute(
            """
            DELETE FROM images
            WHERE path = ?
            """,
            (path,),
        )

        remove_count += 1

        print(f"[刪除] {path}")

    print()
    print(f"掃描圖片：{count}")
    print(f"新增圖片：{new_count}")
    print(f"更新圖片：{update_count}")
    print(f"刪除圖片：{remove_count}")

    return count