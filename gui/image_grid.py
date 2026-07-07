from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
    QGridLayout,
    QLabel,
)

from database import create_database


class ImageCard(QLabel):

    def __init__(self, text):

        super().__init__(text)

        self.setFixedSize(180, 180)

        self.setAlignment(Qt.AlignCenter)

        self.setWordWrap(True)

        self.setStyleSheet("""
        QLabel{
            background:#3a3a3a;
            border:1px solid #666666;
            color:white;
            padding:8px;
        }
        """)


class ImageGrid(QScrollArea):

    def __init__(self):

        super().__init__()

        self.setWidgetResizable(True)

        self.container = QWidget()

        self.grid = QGridLayout(self.container)

        self.grid.setSpacing(10)

        self.setWidget(self.container)

        self.load_images()

    def load_images(self):

        conn, cursor = create_database()

        cursor.execute("""
            SELECT filename
            FROM images
            LIMIT 120
        """)

        rows = cursor.fetchall()

        conn.close()

        columns = 6

        for i, row in enumerate(rows):

            filename = row[0]

            card = ImageCard(filename)

            r = i // columns
            c = i % columns

            self.grid.addWidget(card, r, c)