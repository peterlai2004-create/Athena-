from PySide6.QtWidgets import QWidget, QVBoxLayout

from gui.image_grid import ImageGrid


class ImagePanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.image_grid = ImageGrid()

        layout.addWidget(self.image_grid)