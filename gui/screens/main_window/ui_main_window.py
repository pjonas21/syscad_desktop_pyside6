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


        # CRIANDO O LAYOUT PRINCIPAL DA APLICAÇÃO =========================================
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)


        # LEFT MENU =======================================================================
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #1E830E; color: #F3F2F2")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # LAYOUT LEFT MENU
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)

        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)

        # LAYOUT MENU TOP FRAME
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)

        # TOP BUTTONS MENU
        self.toggle_button = QPushButton("Toggle")
        self.btn_home = QPushButton("Início")
        self.btn_colab = QPushButton("Colaboradores")

        # ADD BUTTONS TO MENU TOP LAYOUT
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_home)
        self.left_menu_top_layout.addWidget(self.btn_colab)

        # MENU SPACER
        self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)

        # LAYOUT MENU BOTTOM FRAME
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout.setSpacing(0)

        # BOTTOM BUTTONS MENU
        self.btn_settings = QPushButton("Config")

        # ADD BUTTONS TO MENU BOTTOM LAYOUT
        self.left_menu_bottom_layout.addWidget(self.btn_settings)

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


        # CONTENT =============================================================================
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #F3F2F2")

        # CONTENT TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setStyleSheet("background-color: #A2FD94; color: #56AB49")
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)

        # TOP BAR - LEFT LABEL
        self.text_label_left = QLabel("Registro e acompanhamento PM")

        # TOP BAR - SPACER
        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # TOP BAR - RIGHT LABEL
        self.text_label_right = QLabel("| PÁGINA INICIAL")
        self.text_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # TOP BAR LAYOUT
        self.top_bar_layout.addWidget(self.text_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.text_label_right)

        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)


        # FOOTER =============================================================================
        self.footer = QFrame()
        self.footer.setStyleSheet("background-color: #A2FD94; color: #56AB49")
        self.footer.setMinimumHeight(30)
        self.footer.setMaximumHeight(30)
        self.footer_layout = QHBoxLayout(self.footer)
        self.footer_layout.setContentsMargins(10,0,10,0)

        # FOOTER - LEFT LABEL
        self.footer_label_left = QLabel("Criado por: Paulo Jonas Alves da Silva - 3ºSgt PM")

        # FOORTER - SPACER
        self.footer_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # FOOTER - RIGHT LABEL
        self.footer_label_right = QLabel("¢ 2023")

        # FOOTER LAYOUT
        self.footer_layout.addWidget(self.footer_label_left)
        self.footer_layout.addItem(self.footer_spacer)
        self.footer_layout.addWidget(self.footer_label_right)


        # APPLICATION PAGES ================================================================
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #083600")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)


        # ADD WIDGETS CONTENT LAYOUT =======================================================
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.footer)


        # ADD WIDGETS CENTRAL FRAME ========================================================
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)


        # SET CENTRAL FRAME ================================================================
        parent.setCentralWidget(self.central_frame)
