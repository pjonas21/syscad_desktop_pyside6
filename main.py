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

        self.ui.toggle_button.clicked.connect(self.toggle_btn)

        self.show()

    def toggle_btn(self):
        menu_width = self.ui.left_menu.width()
        width = 50
        if menu_width == width:
            width = 240

        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
