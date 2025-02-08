# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets
from menu_inicial_antigo import * #carregar dados de outra janela
from PyQt5.QtWidgets import QMessageBox


class Ui_TelaLogin(object):
    def setupUi(self, TelaLogin):
        TelaLogin.setObjectName("TelaLogin")
        TelaLogin.resize(350, 200)
        TelaLogin.setMinimumSize(QtCore.QSize(350, 200))
        TelaLogin.setMaximumSize(QtCore.QSize(350, 200))
        self.centralwidget = QtWidgets.QWidget(TelaLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 10, 281, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_entrar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_entrar.setObjectName("pushButton_entrar")
        
        self.pushButton_entrar.clicked.connect(self.login)
        
        self.gridLayout.addWidget(self.pushButton_entrar, 2, 1, 1, 1)
        self.lineEdit_senha = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.gridLayout.addWidget(self.lineEdit_senha, 1, 1, 1, 1)
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.gridLayout.addWidget(self.lineEdit_usuario, 0, 1, 1, 1)
        self.label_senha = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_senha.setObjectName("label_senha")
        self.gridLayout.addWidget(self.label_senha, 1, 0, 1, 1)
        self.label_usuario = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_usuario.setObjectName("label_usuario")
        self.gridLayout.addWidget(self.label_usuario, 0, 0, 1, 1)
        TelaLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaLogin)
        QtCore.QMetaObject.connectSlotsByName(TelaLogin)

    def retranslateUi(self, TelaLogin):
        _translate = QtCore.QCoreApplication.translate
        TelaLogin.setWindowTitle(_translate("TelaLogin", "LOGIN"))
        self.pushButton_entrar.setText(_translate("TelaLogin", "ENTRAR"))
        self.label_senha.setText(_translate("TelaLogin", "Senha:"))
        self.label_usuario.setText(_translate("TelaLogin", "Usuário:"))

    def login(self):
        usuario = self.lineEdit_usuario.text()
        senha = self.lineEdit_senha.text()
        
        if usuario == "bernardo" and senha == "bimba":
            self.tela = QtWidgets.QMainWindow()
            
            self.menu = Ui_TelaMenu()
            
            self.menu.setupUi(self.tela)
            
            self.tela.show()
            
            TelaLogin.close()
            
            
            
            
        else:
            msg = QMessageBox()
            msg.setText("USUÁRIO OU SENHA INCORRETOS")
            msg.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaLogin = QtWidgets.QMainWindow()
    ui = Ui_TelaLogin()
    ui.setupUi(TelaLogin)
    TelaLogin.show()
    sys.exit(app.exec_())
