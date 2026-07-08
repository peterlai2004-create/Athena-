from PySide6.QtCore import Qt, Signal, QUrl
from PySide6.QtGui import QPixmap, QDesktopServices
from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
    QGridLayout,
    QLabel,
    QVBoxLayout,
    QSizePolicy,
)
from numpy import size

from database import create_database


class ImageCard(QWidget):

    clicked = Signal(dict)
    double_clicked = Signal(dict)

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

        self.selected = False
        self.hover = False

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

        self.setMouseTracking(True)

        self.update_style()

    def update_style(self):

        border = "#555"
        background = "#2f2f2f"

        if self.hover:
            background = "#383838"

        if self.selected:
            border = "#3B82F6"

        self.setStyleSheet(f"""
        QWidget {{
            background:{background};
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

    def enterEvent(self, event):
        self.hover = True
        self.update_style()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.hover = False
        self.update_style()
        super().leaveEvent(event)

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.image_info)

        super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.double_clicked.emit(self.image_info)

        super().mouseDoubleClickEvent(event)


class ImageGrid(QScrollArea):

    image_selected = Signal(dict)

    def __init__(self):
        super().__init__()

        self.current_card = None

        self.current_images = []
        self.current_keyword = ""
        self.thumbnail_size = 180

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

    def clear_grid(self):

        while self.grid.count():

            item = self.grid.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

    def query_images(self, keyword=""):

        conn, cursor = create_database()

        if keyword:

            cursor.execute("""
                SELECT
                    id,
                    path,
                    filename,
                    size,
                    hash
                FROM images
                WHERE filename LIKE ?
                ORDER BY filename
                LIMIT 500
            """, (f"%{keyword}%",))

        else:

            cursor.execute("""
                SELECT
                    id,
                    path,
                    filename,
                    size,
                    hash
                FROM images
                LIMIT 500
            """)

        self.current_images = cursor.fetchall()

        conn.close()

        self.current_keyword = keyword
    def render_images(self):

        self.clear_grid()

        rows = self.current_images

        if not rows:

            label = QLabel("No Images Found")
            label.setAlignment(Qt.AlignCenter)

            self.grid.addWidget(label)

            return

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

            card.setFixedSize(
                self.thumbnail_size,
                self.thumbnail_size + 40
            )

            card.image_label.setFixedSize(
                self.thumbnail_size - 10,
                self.thumbnail_size - 10
        )

            card.clicked.connect(
                lambda info, c=card:
                self.select_card(c, info)
            )

            card.double_clicked.connect(
                self.open_image
            )

            r = i // columns
            c = i % columns

            self.grid.addWidget(card, r, c)

    def load_images(self, keyword=""):

        self.query_images(keyword)

        self.render_images()

    def load_recent_images(self, images):

        self.current_images = []

        for info in images:

            row = (
                info["id"],
                info["path"],
                info["filename"],
                info["size"],
                info["hash"],
            )

            self.current_images.append(row)

        self.render_images()

    def refresh_grid(self):

        self.render_images()

    def set_thumbnail_size(
        self,
        size,
    ):

        self.thumbnail_size = size

        self.render_images()

    def select_card(self, card, info):

        if self.current_card:
            self.current_card.set_selected(False)

        self.current_card = card
        self.current_card.set_selected(True)

        self.image_selected.emit(info)

    def open_image(self, info):

        QDesktopServices.openUrl(
            QUrl.fromLocalFile(info["path"])
        )