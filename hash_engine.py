"""
Project Athena
hash_engine.py

負責計算圖片 SHA-256。
"""

import hashlib


def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:

        while True:

            data = f.read(65536)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()