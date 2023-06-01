import sys
import os

from qt_core import *

from gui.screens.main_window.ui_main_window import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BD-CIA")

        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
