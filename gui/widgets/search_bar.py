from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
)


class SearchBar(QWidget):

    search_requested = Signal(str)

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)

        self.search_edit = QLineEdit()

        self.search_edit.setPlaceholderText("🔍 搜尋圖片...")

        self.search_button = QPushButton("Search")

        layout.addWidget(self.search_edit)

        layout.addWidget(self.search_button)

        self.search_button.clicked.connect(self.emit_search)

        self.search_edit.returnPressed.connect(self.emit_search)

    def emit_search(self):

        text = self.search_edit.text().strip()

        self.search_requested.emit(text)