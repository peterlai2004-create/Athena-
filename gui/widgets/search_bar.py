from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QSlider,
)


class SearchBar(QWidget):

    search_requested = Signal(str)
    thumbnail_size_changed = Signal(int)

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("🔍 搜尋圖片...")

        self.search_button = QPushButton("Search")

        self.size_label = QLabel("Size")

        self.size_slider = QSlider(Qt.Horizontal)
        self.size_slider.setMinimum(120)
        self.size_slider.setMaximum(300)
        self.size_slider.setValue(180)
        self.size_slider.setFixedWidth(150)

        layout.addWidget(self.search_edit)
        layout.addWidget(self.search_button)
        layout.addWidget(self.size_label)
        layout.addWidget(self.size_slider)

        self.search_button.clicked.connect(
            self.emit_search
        )

        self.search_edit.returnPressed.connect(
            self.emit_search
        )

        self.size_slider.valueChanged.connect(
            self.thumbnail_size_changed.emit
        )

    def emit_search(self):

        text = self.search_edit.text().strip()

        self.search_requested.emit(text)