# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaMenu(object):
    def setupUi(self, TelaMenu):
        TelaMenu.setObjectName("TelaMenu")
        TelaMenu.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TelaMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 50, 241, 201))
        self.label.setObjectName("label")
        TelaMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaMenu)
        QtCore.QMetaObject.connectSlotsByName(TelaMenu)

    def retranslateUi(self, TelaMenu):
        _translate = QtCore.QCoreApplication.translate
        TelaMenu.setWindowTitle(_translate("TelaMenu", "MENU"))
        self.label.setText(_translate("TelaMenu", "CORINTHIANS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaMenu = QtWidgets.QMainWindow()
    ui = Ui_TelaMenu()
    ui.setupUi(TelaMenu)
    TelaMenu.show()
    sys.exit(app.exec_())
