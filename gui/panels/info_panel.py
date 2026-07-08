from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
)

from PIL import Image


class InfoPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)

        title = QLabel("Preview")
        layout.addWidget(title)

        self.preview_label = QLabel()
        self.preview_label.setFixedHeight(250)
        self.preview_label.setAlignment(Qt.AlignCenter)

        self.preview_label.setStyleSheet("""
            QLabel{
                background:#2f2f2f;
                border:1px solid #555;
                border-radius:8px;
            }
        """)

        layout.addWidget(self.preview_label)

        self.info = QTextEdit()
        self.info.setReadOnly(True)

        layout.addWidget(self.info)

        self.clear_info()

    def clear_info(self):

        self.preview_label.clear()

        self.info.setPlainText(
            "Filename:\n"
            "\n"
            "Path:\n"
            "\n"
            "Resolution:\n"
            "\n"
            "Size:\n"
            "\n"
            "Hash:\n"
        )

    def set_image_info(
        self,
        filename,
        path,
        width=None,
        height=None,
        size=None,
        image_hash=None,
        tags=""
    ):

        pixmap = QPixmap(path)

        if not pixmap.isNull():

            pixmap = pixmap.scaled(
                300,
                250,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            self.preview_label.setPixmap(pixmap)

        try:
            img = Image.open(path)
            width, height = img.size
            resolution = f"{width} x {height}"
        except:
            resolution = ""

        size_text = ""

        if size is not None:
            size_text = f"{size:,} bytes"

        hash_text = image_hash or ""

        self.info.setPlainText(
            f"Filename:\n{filename}\n\n"
            f"Path:\n{path}\n\n"
            f"Resolution:\n{resolution}\n\n"
            f"Size:\n{size_text}\n\n"
            f"Hash:\n{hash_text}"
        )