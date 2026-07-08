from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
)


class InfoPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)

        title = QLabel("Information")
        layout.addWidget(title)

        self.info = QTextEdit()
        self.info.setReadOnly(True)

        self.clear_info()

        layout.addWidget(self.info)

    def clear_info(self):

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
            "\n"
            "Tags:\n"
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

        resolution = ""

        if width and height:
            resolution = f"{width} x {height}"

        size_text = ""

        if size is not None:
            size_text = f"{size:,} bytes"

        hash_text = image_hash or ""

        self.info.setPlainText(
            f"Filename:\n{filename}\n\n"
            f"Path:\n{path}\n\n"
            f"Resolution:\n{resolution}\n\n"
            f"Size:\n{size_text}\n\n"
            f"Hash:\n{hash_text}\n\n"
            f"Tags:\n{tags}"
        )