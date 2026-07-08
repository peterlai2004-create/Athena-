from PySide6.QtCore import Qt, Signal
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

    clicked = Signal(dict)

    def __init__(
        self,
        image_id,
        image_path,
        filename,
        size,
        image_hash,
    ):
        super().__init__()

        self.image_info = {
            "id": image_id,
            "path": image_path,
            "filename": filename,
            "size": size,
            "hash": image_hash,
        }

        self.setFixedSize(180, 220)

        self.selected = False

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
                Qt.SmoothTransformation,
            )
            self.image_label.setPixmap(pixmap)
        else:
            self.image_label.setText("No Preview")

        self.text_label = QLabel(filename)
        self.text_label.setWordWrap(True)
        self.text_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.image_label)
        layout.addWidget(self.text_label)

        self.update_style()

    def update_style(self):

        if self.selected:
            border = "#3B82F6"
        else:
            border = "#555"

        self.setStyleSheet(f"""
        QWidget {{
            background:#2f2f2f;
            border:2px solid {border};
            border-radius:8px;
        }}

        QLabel {{
            color:white;
            border:none;
            background:transparent;
        }}
        """)

    def set_selected(self, value):

        self.selected = value
        self.update_style()

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.image_info)

        super().mousePressEvent(event)


class ImageGrid(QScrollArea):

    image_selected = Signal(dict)

    def __init__(self):
        super().__init__()

        self.current_card = None

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
            SELECT
                id,
                path,
                filename,
                size,
                hash
            FROM images
            LIMIT 120
        """)

        rows = cursor.fetchall()

        conn.close()

        columns = 6

        for i, row in enumerate(rows):

            image_id = row[0]
            image_path = row[1]
            filename = row[2]
            size = row[3]
            image_hash = row[4]

            card = ImageCard(
                image_id,
                image_path,
                filename,
                size,
                image_hash,
            )

            card.clicked.connect(
                lambda info, c=card:
                self.select_card(c, info)
            )

            r = i // columns
            c = i % columns

            self.grid.addWidget(card, r, c)

    def select_card(self, card, info):

        if self.current_card:
            self.current_card.set_selected(False)

        self.current_card = card

        self.current_card.set_selected(True)

        self.image_selected.emit(info)