# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pageskNxNpN.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(612, 363)
        application_pages.setMinimumSize(QSize(600, 350))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 70))
        self.frame.setMaximumSize(QSize(500, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(30, 131, 14);")

        self.verticalLayout_4.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_user = QLineEdit(self.frame)
        self.lbl_user.setObjectName(u"lbl_user")
        self.lbl_user.setMinimumSize(QSize(0, 36))
        self.lbl_user.setMaximumSize(QSize(16777215, 36))
        self.lbl_user.setStyleSheet(u"QLineEdit {\n"
"	padding: 6px;\n"
"	border: 2px solid #56AB49;\n"
"	border-radius: 8px;\n"
"}")

        self.gridLayout.addWidget(self.lbl_user, 0, 0, 1, 1)

        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(120, 36))
        self.btn_login.setMaximumSize(QSize(120, 36))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"	width: 80px;\n"
"	font: 700 italic 10pt \"Segoe UI\";\n"
"	background-color: #1E830E;\n"
"	color: #F3F2F2;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"	padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #56AB49;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #A2FD94;\n"
"}")

        self.gridLayout.addWidget(self.btn_login, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        application_pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(600, 350))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.field_search = QLineEdit(self.frame_2)
        self.field_search.setObjectName(u"field_search")
        self.field_search.setStyleSheet(u"QLineEdit {\n"
"	padding: 6px;\n"
"	border: 2px solid #56AB49;\n"
"	border-radius: 8px;\n"
"}")

        self.gridLayout_2.addWidget(self.field_search, 0, 0, 1, 1)

        self.btn_search = QPushButton(self.frame_2)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setStyleSheet(u"QPushButton {\n"
"	width: 80px;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	background-color: #1E830E;\n"
"	color: #F3F2F2;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"	padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #56AB49;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #A2FD94;\n"
"}")

        self.gridLayout_2.addWidget(self.btn_search, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.list_colab = QListView(self.frame_2)
        self.list_colab.setObjectName(u"list_colab")
        self.list_colab.setStyleSheet(u"QListView {\n"
"	border-radius: 8px;\n"
"	border: 2px solid #A2FD94;\n"
"}")

        self.gridLayout_4.addWidget(self.list_colab, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_ficha = QPushButton(self.frame_2)
        self.btn_ficha.setObjectName(u"btn_ficha")
        self.btn_ficha.setStyleSheet(u"QPushButton {\n"
"	width: 80px;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	background-color: #1E830E;\n"
"	color: #F3F2F2;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"	padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #56AB49;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #A2FD94;\n"
"}")

        self.gridLayout_3.addWidget(self.btn_ficha, 2, 0, 1, 1)

        self.btn_detail = QPushButton(self.frame_2)
        self.btn_detail.setObjectName(u"btn_detail")
        self.btn_detail.setStyleSheet(u"QPushButton {\n"
"	width: 80px;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	background-color: #1E830E;\n"
"	color: #F3F2F2;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"	padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #56AB49;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #A2FD94;\n"
"}")

        self.gridLayout_3.addWidget(self.btn_detail, 1, 0, 1, 1)

        self.btn_add = QPushButton(self.frame_2)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setStyleSheet(u"QPushButton {\n"
"	width: 80px;\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	background-color: #1E830E;\n"
"	color: #F3F2F2;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"	padding: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #56AB49;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #A2FD94;\n"
"}")

        self.gridLayout_3.addWidget(self.btn_add, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)


        self.verticalLayout_2.addWidget(self.frame_2)

        application_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        application_pages.addWidget(self.page_3)

        self.retranslateUi(application_pages)

        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"Usu\u00e1rio", None))
        self.lbl_user.setText("")
        self.lbl_user.setPlaceholderText(QCoreApplication.translate("application_pages", u"Informe o usu\u00e1rio...", None))
        self.btn_login.setText(QCoreApplication.translate("application_pages", u"Entrar", None))
        self.btn_search.setText(QCoreApplication.translate("application_pages", u"Buscar", None))
        self.btn_ficha.setText(QCoreApplication.translate("application_pages", u"Ficha Ind.", None))
        self.btn_detail.setText(QCoreApplication.translate("application_pages", u"Detalhe", None))
        self.btn_add.setText(QCoreApplication.translate("application_pages", u"Adicionar", None))
        self.label.setText(QCoreApplication.translate("application_pages", u"P\u00c1GINA 03", None))
    # retranslateUi

