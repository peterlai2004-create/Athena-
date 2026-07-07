from PySide6.QtWidgets import QWidget, QVBoxLayout

from gui.image_grid import ImageGrid


class ImagePanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.image_grid = ImageGrid()

        layout.addWidget(self.image_grid)