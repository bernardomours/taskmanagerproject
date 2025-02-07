# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Edicao_tarefa(object):
    def setupUi(self, Edicao_tarefa):
        Edicao_tarefa.setObjectName("Edicao_tarefa")
        Edicao_tarefa.resize(672, 382)
        self.centralwidget = QtWidgets.QWidget(Edicao_tarefa)
        self.centralwidget.setObjectName("centralwidget")
        Edicao_tarefa.setCentralWidget(self.centralwidget)

        self.retranslateUi(Edicao_tarefa)
        QtCore.QMetaObject.connectSlotsByName(Edicao_tarefa)

    def retranslateUi(self, Edicao_tarefa):
        _translate = QtCore.QCoreApplication.translate
        Edicao_tarefa.setWindowTitle(_translate("Edicao_tarefa", "Edição de Tarefa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Edicao_tarefa = QtWidgets.QMainWindow()
    ui = Ui_Edicao_tarefa()
    ui.setupUi(Edicao_tarefa)
    Edicao_tarefa.show()
    sys.exit(app.exec_())
