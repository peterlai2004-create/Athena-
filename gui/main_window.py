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

from recent_manager import RecentManager
from favorite_manager import FavoriteManager


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.recent_manager = RecentManager()
        self.favorite_manager = FavoriteManager()
        self.current_image_info = None

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

        self.root_layout.addWidget(
            self.splitter,
            1
        )

    def _setup_connections(self):

        self.image_panel.image_grid.image_selected.connect(
            self.on_image_selected
        )

        self.search_bar.search_requested.connect(
            self.on_search_requested
        )

        self.search_bar.thumbnail_size_changed.connect(
            self.image_panel.image_grid.set_thumbnail_size
        )

        self.navigation_panel.recent_btn.clicked.connect(
            self.on_recent_clicked
        )

        self.info_panel.favorite_clicked.connect(
            self.on_favorite_clicked
        )

        self.navigation_panel.home_btn.clicked.connect(
            self.on_home_clicked
        )

        self.navigation_panel.favorite_btn.clicked.connect(
            self.on_favorite_page_clicked
        )

    def on_image_selected(self, info):

        self.current_image_info = info

        self.recent_manager.add(info)

        recent_count = len(
            self.recent_manager.get_recent_images()
        )

        self.navigation_panel.set_recent_count(
            recent_count
        )

        self.info_panel.set_image_info(
            image_id=info["id"],
            filename=info["filename"],
            path=info["path"],
            size=info["size"],
            image_hash=info["hash"],
        )

        self.statusBar().showMessage(
            f"Recent Images: {recent_count}"
        )

    def on_search_requested(self, text):

        self.image_panel.image_grid.load_images(
            text
        )

        if text:

            self.statusBar().showMessage(
                f'Search: "{text}"'
            )

        else:

            self.statusBar().showMessage(
                "Athena Ready"
            )

    def on_recent_clicked(self):

        images = (
            self.recent_manager
            .get_recent_images()
        )

        self.image_panel.image_grid.load_recent_images(
            images
        )

        self.statusBar().showMessage(
            f"Showing {len(images)} recent images"
        )

    def on_home_clicked(self):

        self.image_panel.image_grid.load_images()

        self.statusBar().showMessage(
            "Home"
        )

    def on_favorite_page_clicked(self):

        images = (
            self.favorite_manager
            .get_favorites()
        )

        self.image_panel.image_grid.load_favorite_images(
            images
        )

        self.statusBar().showMessage(
            f"Showing {len(images)} favorite images"
        )

    def on_favorite_clicked(self):

        if self.current_image_info is None:
            return

        is_favorite = self.favorite_manager.toggle(
            self.current_image_info
        )

        self.info_panel.set_favorite_state(
            is_favorite
        )

        count = len(
            self.favorite_manager.get_favorites()
        )

        self.navigation_panel.set_favorite_count(
            count
        )

        self.statusBar().showMessage(
            f"Favorites: {count}"
        )

    def _setup_statusbar(self):

        self.statusBar().showMessage(
            "Athena Ready"
        )