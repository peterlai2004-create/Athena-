"""
Project Athena

image_repository.py

Image Repository
"""

from dataclasses import dataclass


@dataclass
class ImageInfo:

    id: int

    path: str

    filename: str

    extension: str

    size: int

    modified_time: float

    hash: str


class ImageRepository:

    def __init__(self, cursor):

        self.cursor = cursor

    def get(self, image_id):

        self.cursor.execute(
            """
            SELECT
                id,
                path,
                filename,
                extension,
                size,
                modified_time,
                hash
            FROM images
            WHERE id = ?
            """,
            (image_id,),
        )

        row = self.cursor.fetchone()

        if row is None:
            return None

        return ImageInfo(
            id=row[0],
            path=row[1],
            filename=row[2],
            extension=row[3],
            size=row[4],
            modified_time=row[5],
            hash=row[6],
        )