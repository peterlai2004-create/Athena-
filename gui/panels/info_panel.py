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

        layout.addWidget(QLabel("Information"))

        self.info = QTextEdit()
        self.info.setReadOnly(True)

        self.info.setPlainText(
            "Filename:\n"
            "\n"
            "Resolution:\n"
            "\n"
            "Size:\n"
            "\n"
            "Hash:\n"
            "\n"
            "Tags:\n"
        )

        layout.addWidget(self.info)