from qt_core import *

from gui.pages.ui_pages import Ui_application_pages


class UiMainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # configurando tamanho inicial e mínimo da aplicação
        parent.resize(900, 600)
        parent.setMinimumSize(700, 450)

        # configurando frame central da aplicação
        self.central_frame = QFrame()

        # CRIANDO O LAYOUT PRINCIPAL DA APLICAÇÃO
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # menu lateral
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #1E830E")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # LAYOUT LEFT MENU
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)

        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setStyleSheet("background-color: black")

        # MENU SPACER
        self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setStyleSheet("background-color: black")

        # LABEL VERSION APP
        self.label_version = QLabel("v1.0.0")
        self.label_version.setStyleSheet("color: #F3F2F2")
        self.label_version.setAlignment(Qt.AlignCenter)
        self.label_version.setMinimumHeight(30)
        self.label_version.setMaximumHeight(30)

        # ADD LAYOUT FRAME MENU
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.label_version)

        # conteudo da aplicação
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #F3F2F2")

        # criando top bar
        self.top_bar = QFrame()
        self.top_bar.setStyleSheet("background-color: #A2FD94; color: #56AB49")
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)

        # left label
        self.text_label_left = QLabel("Registro e acompanhamento PM")

        # top spacer
        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # right label
        self.text_label_right = QLabel("| PÁGINA INICIAL")
        self.text_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # add to layout top bar
        self.top_bar_layout.addWidget(self.text_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.text_label_right)

        # layout do conteudo
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # criando footer
        self.footer = QFrame()
        self.footer.setStyleSheet("background-color: #A2FD94; color: #56AB49")
        self.footer.setMinimumHeight(30)
        self.footer.setMaximumHeight(30)
        self.footer_layout = QHBoxLayout(self.footer)
        self.footer_layout.setContentsMargins(10,0,10,0)

        # left label
        self.footer_label_left = QLabel("Criado por: Paulo Jonas Alves da Silva - 3ºSgt PM")

        # top spacer
        self.footer_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # right label
        self.footer_label_right = QLabel("¢ 2023")

        # add to layout top bar
        self.footer_layout.addWidget(self.footer_label_left)
        self.footer_layout.addItem(self.footer_spacer)
        self.footer_layout.addWidget(self.footer_label_right)

        # paginas da aplicação
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #083600")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)

        # adicionando top bar ao layout de conteudo
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.footer)


        # adicionando widgets ao frame central
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # definindo frame principal da aplicação
        parent.setCentralWidget(self.central_frame)