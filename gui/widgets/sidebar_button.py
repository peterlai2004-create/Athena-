from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton


class SidebarButton(QPushButton):
    def __init__(self, text: str):
        super().__init__(text)

        self.setCursor(Qt.PointingHandCursor)
        self.setCheckable(True)
        self.setMinimumHeight(42)

        self.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 14px;
                text-align: left;
                font-size: 14px;
            }

            QPushButton:hover {
                background: #313244;
            }

            QPushButton:checked {
                background: #3B82F6;
                color: white;
                font-weight: bold;
            }
        """)