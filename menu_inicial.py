# AVISO: Qualquer mudança feita neste arquivo será perdida quando o pyuic5 for executado novamente.
# Não edite este arquivo a menos que você saiba o que está fazendo.
# Arquivo convertido em ui2py.vercel.app

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_TelaMenu(object):
    def setupUi(self, TelaMenu):
        TelaMenu.setObjectName("TelaMenu")
        TelaMenu.resize(553, 431)
        self.centralwidget = QtWidgets.QWidget(TelaMenu)
        self.centralwidget.setObjectName("centralwidget")
        TelaMenu.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(TelaMenu)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 553, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuTELA_INICIAL = QtWidgets.QMenu(self.menuBar)
        self.menuTELA_INICIAL.setObjectName("menuTELA_INICIAL")
        TelaMenu.setMenuBar(self.menuBar)
        self.actionEditar_tarefa = QtWidgets.QAction(TelaMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("edit_5953096.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditar_tarefa.setIcon(icon)
        self.actionEditar_tarefa.setObjectName("actionEditar_tarefa")
        
        self.actionEditar_tarefa.triggered.connect(self.editar_tarefa)
        
        self.actionSair = QtWidgets.QAction(TelaMenu)
        self.actionSair.setObjectName("actionSair")
        
        self.actionSair.triggered.connect(self.sair) #triggered significa = acinar, ou seja, quando acionado ele executa
        
        self.actionCTRL_N = QtWidgets.QAction(TelaMenu)
        self.actionCTRL_N.setObjectName("actionCTRL_N")
        self.actionNova_tarefa = QtWidgets.QAction(TelaMenu)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("paper_14910408.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNova_tarefa.setIcon(icon1)
        self.actionNova_tarefa.setObjectName("actionNova_tarefa")
        
        self.actionNova_tarefa.triggered.connect(self.nova_tarefa) #abre a janela para nova tarefa
        
        self.menuTELA_INICIAL.addAction(self.actionNova_tarefa)
        self.menuTELA_INICIAL.addAction(self.actionEditar_tarefa)
        self.menuTELA_INICIAL.addSeparator()
        self.menuTELA_INICIAL.addAction(self.actionSair)
        self.menuBar.addAction(self.menuTELA_INICIAL.menuAction())

        self.retranslateUi(TelaMenu)
        QtCore.QMetaObject.connectSlotsByName(TelaMenu)

    def retranslateUi(self, TelaMenu):
        _translate = QtCore.QCoreApplication.translate
        TelaMenu.setWindowTitle(_translate("TelaMenu", "MENU"))
        self.menuTELA_INICIAL.setTitle(_translate("TelaMenu", "&Tarefas"))
        self.actionEditar_tarefa.setText(_translate("TelaMenu", "&Editar tarefa"))
        self.actionEditar_tarefa.setShortcut(_translate("TelaMenu", "Ctrl+E"))
        self.actionSair.setText(_translate("TelaMenu", "Sair"))
        self.actionCTRL_N.setText(_translate("TelaMenu", "CTRL + N"))
        self.actionNova_tarefa.setText(_translate("TelaMenu", "&Nova tarefa"))
        self.actionNova_tarefa.setShortcut(_translate("TelaMenu", "Ctrl+N"))
        
    def sair(self):
        sys.exit(app.exec_())
        
    def nova_tarefa(self):
        from nova_tarefa import Ui_Tela_Nova_Tarefa
        self.tela = QtWidgets.QMainWindow()
        self.cad = Ui_Tela_Nova_Tarefa()
        self.cad.setupUi(self.tela)
        self.tela.show()
        
    def editar_tarefa(self):
        from edicao_tarefa import Ui_Edicao_tarefa
        self.tela_edicao = QtWidgets.QMainWindow()
        self.ed = Ui_Edicao_tarefa()
        self.ed.setupUi(self.tela_edicao)
        self.tela_edicao.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaMenu = QtWidgets.QMainWindow()
    ui = Ui_TelaMenu()
    ui.setupUi(TelaMenu)
    TelaMenu.show()
    sys.exit(app.exec_())
