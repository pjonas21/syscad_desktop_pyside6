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

        self.ui.btn_home.clicked.connect(self.show_page_home)
        self.ui.btn_colab.clicked.connect(self.show_page_colab)
        self.ui.btn_settings.clicked.connect(self.show_page_settings)

        self.ui.ui_pages.btn_login.clicked.connect(self.enter_system)

        self.show()

    def enter_system(self):
        user = self.ui.ui_pages.lbl_user.text()
        log_user = f"Usuário logado: {user}"
        self.ui.text_label_right.setText(log_user)

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def show_page_home(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_home.set_active(True)

    def show_page_colab(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_colab.set_active(True)

    def show_page_settings(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.btn_settings.set_active(True)

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
