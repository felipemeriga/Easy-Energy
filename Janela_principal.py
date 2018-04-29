# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
from cbanco_residencial import *
from cbanco_industrial import *


from PyQt4 import QtCore, QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(671, 507)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo\logo_inv.bmp")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 681, 471))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Kozuka Mincho Pro B"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo/energia_solar.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 40, 381, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_2.setLineWidth(4)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 290, 151, 171))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo/eee.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 180, 201, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 230, 201, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 280, 201, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 380, 201, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 330, 201, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionCriar_Residencial_2 = QtGui.QAction(MainWindow)
        self.actionCriar_Residencial_2.setObjectName(_fromUtf8("actionCriar_Residencial_2"))
        self.actionCriar_Industrial = QtGui.QAction(MainWindow)
        self.actionCriar_Industrial.setObjectName(_fromUtf8("actionCriar_Industrial"))
        self.actionImportar_XLS = QtGui.QAction(MainWindow)
        self.actionImportar_XLS.setObjectName(_fromUtf8("actionImportar_XLS"))
        self.actionSair = QtGui.QAction(MainWindow)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.actionManuais = QtGui.QAction(MainWindow)
        self.actionManuais.setObjectName(_fromUtf8("actionManuais"))
        self.actionSobre = QtGui.QAction(MainWindow)
        self.actionSobre.setObjectName(_fromUtf8("actionSobre"))
        self.actionCarre_Residencial = QtGui.QAction(MainWindow)
        self.actionCarre_Residencial.setObjectName(_fromUtf8("actionCarre_Residencial"))
        self.actionCarregar_Industrial = QtGui.QAction(MainWindow)
        self.actionCarregar_Industrial.setObjectName(_fromUtf8("actionCarregar_Industrial"))
        self.actionSair_2 = QtGui.QAction(MainWindow)
        self.actionSair_2.setObjectName(_fromUtf8("actionSair_2"))
        self.actionImportar_XLS_2 = QtGui.QAction(MainWindow)
        self.actionImportar_XLS_2.setObjectName(_fromUtf8("actionImportar_XLS_2"))
        self.actionImportar_XLS_Industrial = QtGui.QAction(MainWindow)
        self.actionImportar_XLS_Industrial.setObjectName(_fromUtf8("actionImportar_XLS_Industrial"))
        self.menuFile.addAction(self.actionCriar_Residencial_2)
        self.menuFile.addAction(self.actionCriar_Industrial)
        self.menuFile.addAction(self.actionCarre_Residencial)
        self.menuFile.addAction(self.actionCarregar_Industrial)
        self.menuFile.addAction(self.actionImportar_XLS_2)
        self.menuFile.addAction(self.actionImportar_XLS_Industrial)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSair_2)
        self.menuHelp.addAction(self.actionManuais)
        self.menuHelp.addAction(self.actionSobre)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy Energy", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#005500;\">Bem Vindo ao Easy Energy</span></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "Criar/Carregar Consultoria Residencial", None))
        self.pushButton_2.setText(_translate("MainWindow", "Criar/Carregar Consultoria Industrial", None))
        self.pushButton_3.setText(_translate("MainWindow", "Importar XLS Residencial", None))
        self.pushButton_4.setText(_translate("MainWindow", "Sair", None))
        self.pushButton_5.setText(_translate("MainWindow", "Importar XLS Industrial", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionCriar_Residencial_2.setText(_translate("MainWindow", "Criar Residencial", None))
        self.actionCriar_Industrial.setText(_translate("MainWindow", "Criar Industrial", None))
        self.actionImportar_XLS.setText(_translate("MainWindow", "Importar XLS", None))
        self.actionSair.setText(_translate("MainWindow", "Sair", None))
        self.actionManuais.setText(_translate("MainWindow", "Manuais", None))
        self.actionSobre.setText(_translate("MainWindow", "Sobre", None))
        self.actionCarre_Residencial.setText(_translate("MainWindow", "Carregar Residencial", None))
        self.actionCarregar_Industrial.setText(_translate("MainWindow", "Carregar Industrial", None))
        self.actionSair_2.setText(_translate("MainWindow", "Sair", None))
        self.actionImportar_XLS_2.setText(_translate("MainWindow", "Importar XLS Residencial", None))
        self.actionImportar_XLS_Industrial.setText(_translate("MainWindow", "Importar XLS Industrial", None))


class cria_janela_principal(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #AÇÕES TRIGGERS PARA MÉTODOS RESIDENCIAIS
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.criar_residencial)
        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL("clicked()"),self.close)
        QtCore.QObject.connect(self.ui.pushButton_3,QtCore.SIGNAL("clicked()"),self.converter_XLS)
        QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL("clicked()"), self.converter_XLS)


        #AÇÕES TRIGGERS PARA MÉTODOS INDUSTRIAIS

        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL("clicked()"),self.criar_industrial)

        #ATALHOS PARA TRIGGERS
        self.ui.actionSair_2.triggered.connect(self.close)
        self.ui.actionSair_2.setShortcut('Ctrl+S')

        self.ui.actionCriar_Industrial.triggered.connect(self.criar_industrial)
        self.ui.actionCriar_Industrial.setShortcut('Ctrl+I')
        self.ui.actionCarregar_Industrial.triggered.connect(self.criar_industrial)


        self.ui.actionCriar_Residencial_2.triggered.connect(self.criar_residencial)
        self.ui.actionCriar_Residencial_2.setShortcut('Ctrl+C')

        self.ui.actionCarre_Residencial.triggered.connect(self.criar_residencial)

        self.ui.actionImportar_XLS_2.triggered.connect(self.converter_XLS)
        self.ui.actionImportar_XLS.setShortcut('Ctrl+X')

    def criar_residencial(self):

        self.janela_carrega=Form2()
        self.janela_carrega.show()
        QtCore.QObject.connect(self.janela_carrega, QtCore.SIGNAL('finished(int)'),self.ativa)
        self.setDisabled(1)

    def criar_industrial(self):

        self.janela_carrega_industria=Form2_industrial()
        self.janela_carrega_industria.show()
        QtCore.QObject.connect(self.janela_carrega_industria, QtCore.SIGNAL('finished(int)'),self.ativa)
        self.setDisabled(1)


    def converter_XLS(self):

        self.janela_XLS=FormXLS()
        self.janela_XLS.show()
        QtCore.QObject.connect(self.janela_XLS, QtCore.SIGNAL('finished(int)'),self.ativa)
        self.setDisabled(1)

    def ativa(self):

        self.setDisabled(0)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = cria_janela_principal()
    window.show()
    sys.exit(app.exec_())

