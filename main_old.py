from pathlib import Path
import sqlite3


# ===== 設定 =====
IMAGE_FOLDER = Path(r"C:\Users\Peter\OneDrive\圖片")
DATABASE = "Athena.db"

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".gif",
    ".bmp",
}

print("=" * 50)
print("Project Athena")
print("=" * 50)

# 連線資料庫
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# 建立資料表（如果不存在）
cursor.execute("""
CREATE TABLE IF NOT EXISTS images (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    path TEXT,

    filename TEXT,

    extension TEXT,

    size INTEGER,

    modified_time REAL

)
""")

# 先清空舊資料（Sprint 3 暫時這樣做）
cursor.execute("DELETE FROM images")

count = 0

for file in IMAGE_FOLDER.rglob("*"):

    if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS:

count += 1
print(f"[{count}] {file.name}")

        cursor.execute("""

        INSERT INTO images
        (path, filename, extension, size, modified_time)

        VALUES (?, ?, ?, ?, ?)

        """,

        (
            str(file),
            file.name,
            file.suffix.lower(),
            file.stat().st_size,
            file.stat().st_mtime
        )
        )

        count += 1

conn.commit()

conn.close()

print(f"成功寫入 {count} 張圖片")
print("=" * 50)