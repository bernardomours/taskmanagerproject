import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from PyQt5.QtWidgets import QLineEdit
from datetime import datetime
import re


class Ui_TelaPrincipal(object):
    def setupUi(self, TelaPrincipal):
        TelaPrincipal.setObjectName("TelaPrincipal")
        TelaPrincipal.resize(941, 664)
        TelaPrincipal.setMaximumSize(QtCore.QSize(941, 664))
        TelaPrincipal.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/tmp/UPLOADS/foto_logo.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TelaPrincipal.setWindowIcon(icon)
        TelaPrincipal.setStyleSheet("background-color: rgb(43, 255, 177);")
        self.centralwidget = QtWidgets.QWidget(TelaPrincipal)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setStyleSheet("*{\n"
"    border:none;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"    color:black;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_container = QtWidgets.QFrame(self.centralwidget)
        self.left_container.setMaximumSize(QtCore.QSize(200, 16777215))
        self.left_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_container.setObjectName("left_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_container)
        self.verticalLayout_2.setContentsMargins(9, -1, 0, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.left_container)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, 9)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_nome_pytask = QtWidgets.QLabel(self.frame)
        self.label_nome_pytask.setObjectName("label_nome_pytask")
        self.horizontalLayout_4.addWidget(self.label_nome_pytask)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.left_container)
        self.frame_2.setStyleSheet("QFrame{\n"
"    background-color: rgb(43, 255, 177);\n"
"}\n"
"\n"
"QToolBox{\n"
"    text-align:left;\n"
"    background-color: rgb(43, 255, 177);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"    border-radius:5px;\n"
"    background-color: rgb(43, 255, 177);\n"
"    text-align:left;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toolBox = QtWidgets.QToolBox(self.frame_2)
        self.toolBox.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(255,255,255);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:rgb(0,0,0);\n"
"    border-radius:15px;\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 182, 537))
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_home = QtWidgets.QPushButton(self.page)
        self.pushButton_home.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/tmp/UPLOADS/casa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_home.setIcon(icon1)
        self.pushButton_home.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_home.setObjectName("pushButton_home")
        self.verticalLayout_4.addWidget(self.pushButton_home)
        self.pushButton_adicionar_tarefa = QtWidgets.QPushButton(self.page)
        self.pushButton_adicionar_tarefa.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_adicionar_tarefa.setFont(font)
        self.pushButton_adicionar_tarefa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_adicionar_tarefa.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/tmp/UPLOADS/mais.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_adicionar_tarefa.setIcon(icon2)
        self.pushButton_adicionar_tarefa.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_adicionar_tarefa.setObjectName("pushButton_adicionar_tarefa")
        self.verticalLayout_4.addWidget(self.pushButton_adicionar_tarefa)
        self.pushButton_editar_tarefa = QtWidgets.QPushButton(self.page)
        self.pushButton_editar_tarefa.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_editar_tarefa.setFont(font)
        self.pushButton_editar_tarefa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/tmp/UPLOADS/lapis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_editar_tarefa.setIcon(icon3)
        self.pushButton_editar_tarefa.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_editar_tarefa.setObjectName("pushButton_editar_tarefa")
        self.verticalLayout_4.addWidget(self.pushButton_editar_tarefa)
        self.pushButton_excluir_tarefa = QtWidgets.QPushButton(self.page)
        self.pushButton_excluir_tarefa.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_excluir_tarefa.setFont(font)
        self.pushButton_excluir_tarefa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/tmp/UPLOADS/lixo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_excluir_tarefa.setIcon(icon4)
        self.pushButton_excluir_tarefa.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_excluir_tarefa.setObjectName("pushButton_excluir_tarefa")
        self.verticalLayout_4.addWidget(self.pushButton_excluir_tarefa)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 182, 537))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_11.setContentsMargins(-1, 0, 0, 9)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"margin-left: 0")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_11.addWidget(self.label_3, 0, QtCore.Qt.AlignLeft)
        self.toolBox.addItem(self.page_2, "")
        self.verticalLayout_3.addWidget(self.toolBox)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.left_container)
        self.main_container = QtWidgets.QFrame(self.centralwidget)
        self.main_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_container.setObjectName("main_container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_container)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(self.main_container)
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.top_frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.top_frame)
        self.main_frame = QtWidgets.QFrame(self.main_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setContentsMargins(9, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Pages = QtWidgets.QStackedWidget(self.main_frame)
        self.Pages.setObjectName("Pages")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_home)
        self.verticalLayout_6.setContentsMargins(0, 6, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.page_home)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.tableWidget_menu_principal = QtWidgets.QTableWidget(self.page_home)
        self.tableWidget_menu_principal.setStyleSheet("QHeaderView::section{\n"
"    background-color: rgb(240,240,240);\n"
"    color: rgd(0,0,0);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"    background-color: rgb(240,240,240);\n"
"}")
        self.tableWidget_menu_principal.setObjectName("tableWidget_menu_principal")
        self.tableWidget_menu_principal.setColumnCount(7)
        self.tableWidget_menu_principal.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_menu_principal.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_menu_principal.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_menu_principal.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_menu_principal.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_menu_principal.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_menu_principal.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_menu_principal.setHorizontalHeaderItem(6, item)
        self.verticalLayout_6.addWidget(self.tableWidget_menu_principal)
        self.Pages.addWidget(self.page_home)
        self.page_adicionar = QtWidgets.QWidget()
        self.page_adicionar.setObjectName("page_adicionar")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_adicionar)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.page_adicionar)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("background-color: rgb(240,240,240);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background-color: rgb(240,240,240);")
        self.tab.setObjectName("tab")
        self.formLayout = QtWidgets.QFormLayout(self.tab)
        self.formLayout.setObjectName("formLayout")
        self.label_nome_evento = QtWidgets.QLabel(self.tab)
        self.label_nome_evento.setObjectName("label_nome_evento")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_nome_evento)
        self.lineEdit_nome_evento = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_nome_evento.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_nome_evento.setObjectName("lineEdit_nome_evento")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nome_evento)
        # self.label_prazo = QtWidgets.QLabel(self.tab)
        # self.label_prazo.setObjectName("label_prazo")
        # self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_prazo)
        # self.dateEdit_prazo_nova_tarefa = QtWidgets.QDateEdit(self.tab)
        # self.dateEdit_prazo_nova_tarefa.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.dateEdit_prazo_nova_tarefa.setObjectName("dateEdit_prazo_nova_tarefa")
        # self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateEdit_prazo_nova_tarefa)
        self.label_prioridade = QtWidgets.QLabel(self.tab)
        self.label_prioridade.setObjectName("label_prioridade")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_prioridade)
        self.comboBox_prioridade_nova_tarefa = QtWidgets.QComboBox(self.tab)
        self.comboBox_prioridade_nova_tarefa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_prioridade_nova_tarefa.setObjectName("comboBox_prioridade_nova_tarefa")
        self.comboBox_prioridade_nova_tarefa.addItem("")
        self.comboBox_prioridade_nova_tarefa.addItem("")
        self.comboBox_prioridade_nova_tarefa.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_prioridade_nova_tarefa)
        self.label_obs = QtWidgets.QLabel(self.tab)
        self.label_obs.setObjectName("label_obs")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_obs)
        self.label_palavra_chave = QtWidgets.QLabel(self.tab)
        self.label_palavra_chave.setObjectName("label_palavra_chave")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_palavra_chave)
        self.lineEdit_palavra_chave = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_palavra_chave.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_palavra_chave.setObjectName("lineEdit_palavra_chave")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_palavra_chave)
        self.pushButton_salvar_add = QtWidgets.QPushButton(self.tab)
        self.pushButton_salvar_add.setMinimumSize(QtCore.QSize(0, 22))
        self.pushButton_salvar_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_salvar_add.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_salvar_add.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(85, 170, 127);\n"
"    border-radius: 12px;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius:15px;\n"
"    background-color: rgb(255,255,255);\n"
"\n"
"}")
        self.pushButton_salvar_add.setObjectName("pushButton_salvar_add")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pushButton_salvar_add)
        self.textEdit_obs_nova_tarefa = QtWidgets.QTextEdit(self.tab)
        self.textEdit_obs_nova_tarefa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_obs_nova_tarefa.setPlaceholderText("")
        self.textEdit_obs_nova_tarefa.setObjectName("textEdit_obs_nova_tarefa")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.textEdit_obs_nova_tarefa)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.calendarWidget_nova_tarefa = QtWidgets.QCalendarWidget(self.tab_2)
        self.calendarWidget_nova_tarefa.setStyleSheet("background-color: rgb(240,240,240);")
        self.calendarWidget_nova_tarefa.setObjectName("calendarWidget_nova_tarefa")
        self.verticalLayout_8.addWidget(self.calendarWidget_nova_tarefa)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_7.addWidget(self.tabWidget)
        self.Pages.addWidget(self.page_adicionar)
        self.page_editar = QtWidgets.QWidget()
        self.page_editar.setObjectName("page_editar")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_editar)
        self.verticalLayout_10.setContentsMargins(0, 6, -1, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.page_editar)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_10.addWidget(self.label_2)
        self.tableWidget_editar_tarefa = QtWidgets.QTableWidget(self.page_editar)
        self.tableWidget_editar_tarefa.setStyleSheet("QHeaderView::section{\n"
"    background-color: rgb(240,240,240);\n"
"    color: rgd(0,0,0);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"    background-color: rgb(240,240,240);\n"
"}")
        self.tableWidget_editar_tarefa.setObjectName("tableWidget_editar_tarefa")
        self.tableWidget_editar_tarefa.setColumnCount(6)
        self.tableWidget_editar_tarefa.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_editar_tarefa.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_editar_tarefa.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_editar_tarefa.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_editar_tarefa.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_editar_tarefa.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_editar_tarefa.setHorizontalHeaderItem(5, item)
        self.verticalLayout_10.addWidget(self.tableWidget_editar_tarefa)
        self.pushButton_editar_ta = QtWidgets.QPushButton(self.page_editar)#
        self.pushButton_editar_ta.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_editar_ta.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(255,255,255);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:rgb(0,0,0);\n"
"    border-radius:15px;\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.pushButton_editar_ta.setObjectName("pushButton_editar_ta")
        self.verticalLayout_10.addWidget(self.pushButton_editar_ta, 0, QtCore.Qt.AlignHCenter)#
        self.Pages.addWidget(self.page_editar)
        self.page_excluir = QtWidgets.QWidget()
        self.page_excluir.setObjectName("page_excluir")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_excluir)
        self.verticalLayout_9.setContentsMargins(0, 6, 9, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.page_excluir)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.tableWidget_excluir_tarefa = QtWidgets.QTableWidget(self.page_excluir)
        self.tableWidget_excluir_tarefa.setStyleSheet("QHeaderView::section{\n"
"    background-color: rgb(240,240,240);\n"
"    color: rgd(0,0,0);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"    background-color: rgb(240,240,240);\n"
"}")
        self.tableWidget_excluir_tarefa.setObjectName("tableWidget_excluir_tarefa")
        self.tableWidget_excluir_tarefa.setColumnCount(6)
        self.tableWidget_excluir_tarefa.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_excluir_tarefa.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_excluir_tarefa.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_excluir_tarefa.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_excluir_tarefa.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_excluir_tarefa.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_excluir_tarefa.setHorizontalHeaderItem(5, item)
        self.verticalLayout_9.addWidget(self.tableWidget_excluir_tarefa)
        self.pushButton_Excluir_Ta = QtWidgets.QPushButton(self.page_excluir)
        self.pushButton_Excluir_Ta.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_Excluir_Ta.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(255,255,255);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:rgb(0,0,0);\n"
"    border-radius:15px;\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.pushButton_Excluir_Ta.setObjectName("pushButton_Excluir_Ta")
        self.verticalLayout_9.addWidget(self.pushButton_Excluir_Ta, 0, QtCore.Qt.AlignHCenter)
        self.Pages.addWidget(self.page_excluir)
        #
        self.verticalLayout_5.addWidget(self.Pages)
        self.verticalLayout.addWidget(self.main_frame)
        self.footer = QtWidgets.QFrame(self.main_container)
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_versao_app = QtWidgets.QLabel(self.footer)
        self.label_versao_app.setObjectName("label_versao_app")
        self.horizontalLayout_3.addWidget(self.label_versao_app, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.footer)
        self.horizontalLayout.addWidget(self.main_container)
        TelaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaPrincipal)
        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipal)
        self.carregar_tarefas()



    def retranslateUi(self, TelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipal.setWindowTitle(_translate("TelaPrincipal", "PYTASK 2024"))
        self.label_nome_pytask.setText(_translate("TelaPrincipal", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">PyTasks</span></p></body></html>"))
        self.pushButton_home.setText(_translate("TelaPrincipal", "Home"))
        self.pushButton_adicionar_tarefa.setText(_translate("TelaPrincipal", "Adicionar Tarefa"))
        self.pushButton_editar_tarefa.setText(_translate("TelaPrincipal", "Editar Tarefa"))
        self.pushButton_excluir_tarefa.setText(_translate("TelaPrincipal", "Excluir Tarefa"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("TelaPrincipal", "Página Inicial"))
        self.label_3.setText(_translate("TelaPrincipal", "<html><head/><body><p align=\"center\">DESENVOLVEDORES</p><p align=\"center\">Antônio Lúcio Pereira de Almeida N.</p><p align=\"center\">Bernardo Moura Bandeira Araújo</p><p align=\"center\">João Fernandes</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("TelaPrincipal", "Desenvolvedores"))
        self.label.setText(_translate("TelaPrincipal", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">GERENCIADOR DE TAREFAS</span></p></body></html>"))
        self.label_5.setText(_translate("TelaPrincipal", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">PÁGINA PRINCIPAL</span></p></body></html>"))
        item = self.tableWidget_menu_principal.horizontalHeaderItem(0)
        item.setText(_translate("TelaPrincipal", "ID da Tarefa"))
        item = self.tableWidget_menu_principal.horizontalHeaderItem(1)
        item.setText(_translate("TelaPrincipal", "Nome do evento"))
        item = self.tableWidget_menu_principal.horizontalHeaderItem(2)
        item.setText(_translate("TelaPrincipal", "Data do Evento"))
        item = self.tableWidget_menu_principal.horizontalHeaderItem(3)
        item.setText(_translate("TelaPrincipal", "Prioridade"))
        item = self.tableWidget_menu_principal.horizontalHeaderItem(4)
        item.setText(_translate("TelaPrincipal", "Observações"))
        item = self.tableWidget_menu_principal.horizontalHeaderItem(5)
        item.setText(_translate("TelaPrincipal", "Status"))
        item = self.tableWidget_menu_principal.horizontalHeaderItem(6)
        item.setText(_translate("TelaPrincipal", "Palavra-Chave"))
        self.label_nome_evento.setText(_translate("TelaPrincipal", "Nome do Evento:"))
        # self.label_prazo.setText(_translate("TelaPrincipal", "Prazo:"))
        self.label_prioridade.setText(_translate("TelaPrincipal", "Prioridade:"))
        self.comboBox_prioridade_nova_tarefa.setItemText(0, _translate("TelaPrincipal", "1 - Baixa"))
        self.comboBox_prioridade_nova_tarefa.setItemText(1, _translate("TelaPrincipal", "2 - Média"))
        self.comboBox_prioridade_nova_tarefa.setItemText(2, _translate("TelaPrincipal", "3 - Alta"))
        self.label_obs.setText(_translate("TelaPrincipal", "Observações:"))
        self.label_palavra_chave.setText(_translate("TelaPrincipal", "Palavra-Chave:"))
        self.lineEdit_palavra_chave.setPlaceholderText(_translate("TelaPrincipal", "Ex: Estudo, Trabalho, Colégio, Faculdade"))
        self.pushButton_salvar_add.setText(_translate("TelaPrincipal", "SALVAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("TelaPrincipal", "Adicionar Tarefa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("TelaPrincipal", "Calendário"))
        self.label_2.setText(_translate("TelaPrincipal", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">SELECIONE APENAS A QUE VOCÊ DESEJA EDITAR</span></p></body></html>"))
        item = self.tableWidget_editar_tarefa.horizontalHeaderItem(0)
        item.setText(_translate("TelaPrincipal", "ID da Tarefa"))
        item = self.tableWidget_editar_tarefa.horizontalHeaderItem(1)
        item.setText(_translate("TelaPrincipal", "Nome do evento"))
        item = self.tableWidget_editar_tarefa.horizontalHeaderItem(2)
        item.setText(_translate("TelaPrincipal", "Data do Evento"))
        item = self.tableWidget_editar_tarefa.horizontalHeaderItem(3)
        item.setText(_translate("TelaPrincipal", "Prioridade"))
        item = self.tableWidget_editar_tarefa.horizontalHeaderItem(4)
        item.setText(_translate("TelaPrincipal", "Observações"))
        item = self.tableWidget_editar_tarefa.horizontalHeaderItem(5)
        item.setText(_translate("TelaPrincipal", "Status"))
        self.pushButton_editar_ta.setText(_translate("TelaPrincipal", "Editar Tarefa"))
        self.label_4.setText(_translate("TelaPrincipal", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">SELECIONE APENAS A QUE VOCÊ DESEJA EXCLUIR</span></p></body></html>"))
        item = self.tableWidget_excluir_tarefa.horizontalHeaderItem(0)
        item.setText(_translate("TelaPrincipal", "ID da Tarefa"))
        item = self.tableWidget_excluir_tarefa.horizontalHeaderItem(1)
        item.setText(_translate("TelaPrincipal", "Nome do Evento"))
        item = self.tableWidget_excluir_tarefa.horizontalHeaderItem(2)
        item.setText(_translate("TelaPrincipal", "Data do Evento"))
        item = self.tableWidget_excluir_tarefa.horizontalHeaderItem(3)
        item.setText(_translate("TelaPrincipal", "Prioridade"))
        item = self.tableWidget_excluir_tarefa.horizontalHeaderItem(4)
        item.setText(_translate("TelaPrincipal", "Observações"))
        item = self.tableWidget_excluir_tarefa.horizontalHeaderItem(5)
        item.setText(_translate("TelaPrincipal", "Status"))
        self.pushButton_Excluir_Ta.setText(_translate("TelaPrincipal", "Excluir Tarefa"))
        self.label_versao_app.setText(_translate("TelaPrincipal", "PyTask 2024.2"))


        self.pushButton_salvar_add.clicked.connect(self.adicionar_tarefa)
        self.pushButton_Excluir_Ta.clicked.connect(self.excluir_tarefas)       
        self.pushButton_editar_ta.clicked.connect(self.editar_tarefa)


########################PÁGINAS DO SISTEMA

        self.pushButton_home.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_home))
        self.pushButton_adicionar_tarefa.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_adicionar))
        self.pushButton_editar_tarefa.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_editar))
        self.pushButton_excluir_tarefa.clicked.connect(lambda:self.Pages.setCurrentWidget(self.page_excluir))
        
##############################################
###############################################

#funções para as abas home, excluir e editar tarefas e alguns detalhes...
##############################################
#atualizar a lista e das outras abas
    def carregar_tarefas(self):
        from database import listar_tarefas

        db = listar_tarefas() #pega as imformações armazenadas do banco(tarefas.db)

        self.tableWidget_menu_principal.clearContents()
        self.tableWidget_menu_principal.setRowCount(len(db))


        
        self.tableWidget_excluir_tarefa.clearContents()
        self.tableWidget_excluir_tarefa.setRowCount(len(db))
        
        for row, text in enumerate(db):
                for column, data in enumerate(text):
                     item = QtWidgets.QTableWidgetItem(str(data))
        
                
                     self.tableWidget_menu_principal.setItem(row, column, item)
                     item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

        #tabela de edição 
        self.tableWidget_editar_tarefa.clearContents()
        self.tableWidget_editar_tarefa.setRowCount(len(db))

        for row, text in enumerate(db):
                for column, data in enumerate(text):
                        item = QtWidgets.QTableWidgetItem(str(data))
                        self.tableWidget_editar_tarefa.setItem(row, column, item)  # Permite edição 
                        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

        # Preencher a tabela de exclusão
        self.tableWidget_excluir_tarefa.clearContents()
        self.tableWidget_excluir_tarefa.setRowCount(len(db))

        for row, text in enumerate(db):
                for column, data in enumerate(text):
                        item = QtWidgets.QTableWidgetItem(str(data))
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Impede edição
                        self.tableWidget_excluir_tarefa.setItem(row, column, item)            

# função de adicionar a tarefa
    def adicionar_tarefa(self):
        from database import inserir_tarefa

        # Captura os dados dos campos de entrada
        nome = self.lineEdit_nome_evento.text()
        data = self.calendarWidget_nova_tarefa.selectedDate().toString("yyyy-MM-dd")
        prioridade = self.comboBox_prioridade_nova_tarefa.currentText()
        obs = self.textEdit_obs_nova_tarefa.toPlainText()
        palavra_chave = self.lineEdit_palavra_chave.text()
        status = "Pendente"  # Padrão ao adicionar

        # Verifica se o nome do evento está preenchido
        if not nome:
                QtWidgets.QMessageBox.warning(None, "Erro", "O nome do evento é obrigatório!")
                return

        # Adiciona a tarefa no banco de dados
        inserir_tarefa(nome, data, prioridade, obs, status, palavra_chave)

        # Atualiza a tabela principal
        self.carregar_tarefas()

        # Limpa os campos das linhas para manter sempre atualizada
        self.lineEdit_nome_evento.clear()
        self.textEdit_obs_nova_tarefa.clear()
        self.lineEdit_palavra_chave.clear()

        QtWidgets.QMessageBox.information(None, "Sucesso", "Tarefa adicionada com sucesso!")

#  função de excluir tarefa, um por um pela linha
    def excluir_tarefas(self):
        selecionar_row = self.tableWidget_excluir_tarefa.currentRow() #Obtem a linha selecionada
        if selecionar_row == -1: #nenhuma linha selecionada
                QtWidgets.QMessageBox.warning(None, "Erro"," Selecione uma tarefa para excluir.")
                return

        item = self.tableWidget_excluir_tarefa.item(selecionar_row, 0)
        if item is None:
                return

        id_tarefa = item.text()

        resposta = QtWidgets.QMessageBox.question(
                None, "Confirmar Exclusão", 
                f"Tem certeza que deseja excluir a tarefa '{id_tarefa}'?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if resposta == QtWidgets.QMessageBox.No:
                return

        from database import excluir_tarefa   

        excluir_tarefa(id_tarefa)

        self.tableWidget_excluir_tarefa.removeRow(selecionar_row)

        self.carregar_tarefas()     

# isso para poder fazer as edições das tarefas sem problema 
    def __init__(self):
        # Conectar ao banco de dados SQLite3
        self.conexao = sqlite3.connect("tarefas.db")
        self.cursor = self.conexao.cursor()

# função de editar tarefas, piores dias da minha vida: fazer essa função.. que negócio dificil    
    def editar_tarefa(self):
        # Pega a linha e coluna selecionada
        selecionado_item = self.tableWidget_editar_tarefa.selectedItems()
        

        if not selecionado_item:
                QMessageBox.warning(None, 'Aviso', "Selecione uma célula para editar.")
                return

# função da verificação da data ainda está com bugs
# o programa valida a data corretamente mas se estiver com a data no formato errado,
# ele da o erro mas salva a informação mesmo assim. 

        def validar_data(data_str):
                """Verifica se a data está no formato correto DD-MM-YYYY."""
                padrao = r"^\d{4}-\d{2}-\d{2}$"
                if re.match(padrao, data_str):
                        return True
                try:
                        datetime.strptime(data_str, "%Y-%m-%d")
                        return True
                except ValueError:
                        return
                          
                                    
        
        item = selecionado_item[0] # Obtém o primeiro item selecionado
        linha = item.row() # Pega a linha da tabela
        coluna = item.column()# Pega a coluna da tabela
        valor_atual = item.text()        # Obtém o valor atual da célula
        
        novo_valor, ok = QInputDialog.getText(None, "Editar Tarefa", "Novo valor:", text=valor_atual) #

        if ok and novo_valor.strip():
                        
                id_tarefa = self.tableWidget_editar_tarefa.item(linha, 0).text()
                colunas_db = ["id","nome", "data", "prioridade", "observacoes", "status", "palavra_chave"]
                nome_coluna = colunas_db[coluna]

                if coluna == 0: #Garante que o id não vai poder ser editado
                      QMessageBox.warning(None, "Aviso", "O ID da tarefa não pode ser editado.")
                      return
                elif coluna == 2:
                       if not validar_data(novo_valor):
                               
                               QMessageBox.warning(None, "Erro", "Formato de data inválido! Use YYYY/MM/DD.")
                               return
                elif coluna == 3:
                       if novo_valor not in ['1 - Baixa', '2 - Média', '3 - Alta']:
                              QMessageBox.warning(None, "Erro", "Formato inválido!O formato deve seguir o da ordem: 1 - Baixa, 2 - Média, 3 - Alta")
                              return
                if coluna == 5:
                        if novo_valor not in ['Pendente', 'Concluida']:
                              QMessageBox.warning(None, "Erro", "Formato inválido! O formato deve seguir o da ordem: Pendente ou Concluida.")
                              return                                                   
                      
                

                # Atualiza o valor na tabela da interface
                item.setText(novo_valor)        


# to fazendo as alterações conectando o banco de dados dessa forma por não ter uma função específica no arquivo database.py e achei mais facil
                cursor = self.conexao.cursor()
                cursor.execute(f"UPDATE tarefas SET {nome_coluna} = ? WHERE id = ?", (novo_valor, id_tarefa) )
                self.conexao.commit()

                self.carregar_tarefas()        

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_TelaPrincipal()
    ui.setupUi(TelaPrincipal)
    TelaPrincipal.show()
    sys.exit(app.exec_())