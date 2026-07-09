from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)

from gui.widgets.sidebar_button import SidebarButton


class NavigationPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(210)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        title = QLabel("ATHENA")

        title.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
            color:white;
            padding:8px;
        """)

        layout.addWidget(title)

        self.home_btn = SidebarButton("🏠 Home")
        self.search_btn = SidebarButton("🔍 Search")
        self.library_btn = SidebarButton("🖼 Library")
        self.recent_btn = SidebarButton("🕒 Recent")
        self.favorite_btn = SidebarButton("⭐ Favorites")
        self.collection_btn = SidebarButton("📁 Collections")
        self.duplicate_btn = SidebarButton("🔄 Duplicate")
        self.ai_btn = SidebarButton("🤖 AI Search")
        self.setting_btn = SidebarButton("⚙ Settings")

        self.home_btn.setChecked(True)

        self.buttons = [
            self.home_btn,
            self.search_btn,
            self.library_btn,
            self.recent_btn,
            self.favorite_btn,
            self.collection_btn,
            self.duplicate_btn,
            self.ai_btn,
            self.setting_btn,
        ]

        for button in self.buttons:

            button.clicked.connect(
                lambda _, b=button:
                self.select_button(b)
            )

            layout.addWidget(button)

        layout.addStretch()

    def select_button(self, button):

        for b in self.buttons:
            b.setChecked(False)

        button.setChecked(True)

    def set_recent_count(self, count):

        self.recent_btn.setText(
            f"🕒 Recent ({count})"
        )

    def set_favorite_count(self, count):

        self.favorite_btn.setText(
            f"⭐ Favorites ({count})"
        )