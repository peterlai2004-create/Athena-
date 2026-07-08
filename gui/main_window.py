from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QSplitter,
)

from PySide6.QtCore import Qt

from gui.panels.navigation_panel import NavigationPanel
from gui.panels.image_panel import ImagePanel
from gui.panels.info_panel import InfoPanel
from gui.widgets.search_bar import SearchBar


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Athena")
        self.resize(1600, 900)

        self._setup_ui()
        self._setup_connections()
        self._setup_statusbar()

    def _setup_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        self.root_layout = QVBoxLayout(central)
        self.root_layout.setContentsMargins(8, 8, 8, 8)
        self.root_layout.setSpacing(8)

        self.search_bar = SearchBar()
        self.root_layout.addWidget(self.search_bar)

        self.splitter = QSplitter(Qt.Horizontal)

        self.navigation_panel = NavigationPanel()
        self.image_panel = ImagePanel()
        self.info_panel = InfoPanel()

        self.splitter.addWidget(self.navigation_panel)
        self.splitter.addWidget(self.image_panel)
        self.splitter.addWidget(self.info_panel)

        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 5)
        self.splitter.setStretchFactor(2, 2)

        self.splitter.setSizes([
            250,
            1000,
            350,
        ])

        self.root_layout.addWidget(self.splitter, 1)

    def _setup_connections(self):

        # 點擊圖片
        self.image_panel.image_grid.image_selected.connect(
            self.on_image_selected
        )

        # 搜尋
        self.search_bar.search_requested.connect(
            self.on_search_requested
        )

    def on_image_selected(self, info):

        self.info_panel.set_image_info(
            filename=info["filename"],
            path=info["path"],
            size=info["size"],
            image_hash=info["hash"],
        )

    def on_search_requested(self, text):

        self.image_panel.image_grid.load_images(text)

        if text:
            self.statusBar().showMessage(
                f'Search: "{text}"'
            )
        else:
            self.statusBar().showMessage(
                "Athena Ready"
            )

    def _setup_statusbar(self):

        self.statusBar().showMessage("Athena Ready")