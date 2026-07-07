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

        central = QWidget()

        self.setCentralWidget(central)

        root = QVBoxLayout(central)

        # Search Bar

        self.search_bar = SearchBar()

        root.addWidget(self.search_bar)
        
        # Main Splitter

        splitter = QSplitter(Qt.Horizontal)

        self.navigation_panel = NavigationPanel()

        self.image_panel = ImagePanel()

        self.info_panel = InfoPanel()

        splitter.addWidget(self.navigation_panel)

        splitter.addWidget(self.image_panel)

        splitter.addWidget(self.info_panel)

        splitter.setStretchFactor(0, 1)

        splitter.setStretchFactor(1, 5)

        splitter.setStretchFactor(2, 2)

        root.addWidget(splitter)

        self.statusBar().showMessage("Athena Ready")