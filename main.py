"""
Project Athena
main.py

Athena 主程式
"""

from database import create_database
from scanner import scan_images


def main():

    print("=" * 50)
    print("Project Athena")
    print("=" * 50)

    print("Version 0.4.0")

    conn, cursor = create_database()

    count = scan_images(cursor)

    conn.commit()
    conn.close()

    print("=" * 50)
    print(f"成功寫入 {count} 張圖片")
    print("=" * 50)


if __name__ == "__main__":
    main()