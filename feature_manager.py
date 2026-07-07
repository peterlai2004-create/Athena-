"""
Project Athena

feature_manager.py

管理哪些圖片需要建立 AI Feature。
"""

import time
from pathlib import Path

from config import AI_MODEL
from feature_engine import generate_feature


def get_pending_images(cursor):

    cursor.execute(
        """
        SELECT
            images.id,
            images.path

        FROM images

        LEFT JOIN image_features

        ON images.id = image_features.image_id
           AND image_features.model = ?

        WHERE image_features.id IS NULL
        """,
        (AI_MODEL,),
    )

    return cursor.fetchall()


def process_features(cursor):

    pending = get_pending_images(cursor)

    total = len(pending)
    success = 0

    start_all = time.time()

    print("=" * 60)
    print(f"AI Model：{AI_MODEL}")
    print(f"等待 AI 分析：{total} 張")
    print("=" * 60)

    for image_id, path in pending:

        filename = Path(path).name

        start = time.time()

        try:

            embedding = generate_feature(path)

            cursor.execute(
                """
                INSERT INTO image_features
                (
                    image_id,
                    model,
                    embedding,
                    created_time
                )

                VALUES (?, ?, ?, ?)
                """,
                (
                    image_id,
                    AI_MODEL,
                    embedding,
                    time.time(),
                ),
            )

            success += 1

            elapsed = time.time() - start
            total_elapsed = time.time() - start_all

            avg = total_elapsed / success

            remain = total - success

            eta = remain * avg

            print(
                f"[{success}/{total}] "
                f"{filename} "
                f"({elapsed:.2f}s)"
            )

            print(
                f"平均 {avg:.2f}s/張 | "
                f"ETA {eta / 60:.1f} 分"
            )

            print()

        except Exception as e:

            print(f"失敗：{filename}")
            print(e)
            print()

        if success > 0 and success % 100 == 0:

            cursor.connection.commit()

            print(">>> Auto Commit <<<")
            print()

    cursor.connection.commit()

    print("=" * 60)
    print(f"成功分析：{success} 張")
    print("=" * 60)