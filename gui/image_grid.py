from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
    QGridLayout,
    QLabel,
    QVBoxLayout,
    QSizePolicy,
)

from database import create_database


class ImageCard(QWidget):

    def __init__(self, image_path, filename):
        super().__init__()

        self.setFixedSize(180, 220)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)

        self.image_label = QLabel()
        self.image_label.setFixedSize(170, 170)
        self.image_label.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap(image_path)

        if not pixmap.isNull():
            pixmap = pixmap.scaled(
                170,
                170,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.image_label.setPixmap(pixmap)
        else:
            self.image_label.setText("No Preview")

        self.text_label = QLabel(filename)
        self.text_label.setWordWrap(True)
        self.text_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.image_label)
        layout.addWidget(self.text_label)

        self.setStyleSheet("""
        QWidget{
            background:#2f2f2f;
            border:1px solid #555;
            border-radius:8px;
        }

        QLabel{
            color:white;
            border:none;
            background:transparent;
        }
        """)


class ImageGrid(QScrollArea):

    def __init__(self):
        super().__init__()

        self.setWidgetResizable(True)

        self.container = QWidget()

        self.container.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Maximum
        )

        self.grid = QGridLayout(self.container)
        self.grid.setSpacing(10)
        self.grid.setContentsMargins(10, 10, 10, 10)
        self.grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.setWidget(self.container)

        self.load_images()

    def load_images(self):

        conn, cursor = create_database()

        cursor.execute("""
            SELECT  path, filename
            FROM images
            LIMIT 120
        """)

        rows = cursor.fetchall()

        conn.close()

        columns = 6

        for i, row in enumerate(rows):

            image_path = row[0]
            filename = row[1]

            card = ImageCard(
                image_path,
                filename
            )

            r = i // columns
            c = i % columns

            self.grid.addWidget(card, r, c)