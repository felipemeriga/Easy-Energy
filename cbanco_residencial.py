# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cbanco1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time




from Residencial import *
from XLS_Residencia import *

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(692, 551)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo\logo_inv.bmp")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 30, 631, 471))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(130, 0, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(270, 240, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(210, 160, 201, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(210, 180, 201, 20))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(540, 0, 91, 91))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo/pequeno.jpg")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.listWidget = QtGui.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(70, 100, 481, 301))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pCarregar = QtGui.QPushButton(self.tab_2)
        self.pCarregar.setGeometry(QtCore.QRect(180, 410, 75, 23))
        self.pCarregar.setObjectName(_fromUtf8("pCarregar"))
        self.pDeletar = QtGui.QPushButton(self.tab_2)
        self.pDeletar.setGeometry(QtCore.QRect(350, 410, 75, 23))
        self.pDeletar.setObjectName(_fromUtf8("pDeletar"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(50, 70, 481, 20))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(130, 20, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(540, 0, 91, 91))
        self.label_5.setT   ext(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo/pequeno.jpg")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(-30, 0, 721, 561))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo\Energia01.png")))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_7.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Easy Energy-Residencial/Comercial", None))
        self.label_2.setText(_translate("Dialog", "Criar novo banco de dados", None))
        self.pushButton.setText(_translate("Dialog", "Criar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Criar Nova Tabela no Banco de Dados", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pCarregar.setText(_translate("Dialog", "Carregar", None))
        self.pDeletar.setText(_translate("Dialog", "Deletar", None))
        self.label_4.setText(_translate("Dialog", "Selecionar banco de dados", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Carregar Banco de Dados", None))


class Form2(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pDeletar,QtCore.SIGNAL("clicked()"),self.deletar_banco)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.criar_banco)
        QtCore.QObject.connect(self.ui.pCarregar,QtCore.SIGNAL("clicked()"),self.carrega_banco)
        connection = MySQLdb.connect(
                host = 'localhost',
                user = 'root',
                passwd = 'iloverpg1')  # create the connection
        cursor = connection.cursor()     # get the cursor


        cursor.execute("USE CARGA_RESIDENCIA") # select the database

        cursor.execute("SHOW TABLES")    # execute 'SHOW TABLES' (but data is not returned)

        tables = cursor.fetchall()
        for (table_name,) in cursor:
            self.ui.listWidget.addItem(table_name)

    def deletar_banco(self):


        conn=MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="carga_residencia")
        cursor=conn.cursor()
        a=self.ui.listWidget.currentItem().text()
        cursor.execute('drop table %s' %a)
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())



    def criar_banco(self):

        conn=MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="carga_residencia")
        cursor=conn.cursor()
        nome_banco = str(self.ui.lineEdit.text())
        if(nome_banco==""):
            self.ui.label_3.setText("Não Foi inserido nenhum nome")
        else:
            try:
                cursor.execute('create table %s (Local char(50),Nome char(50),Potência_Watts varchar(50),Quantidade smallint,Horas varchar(50),Energia_kWh varchar(50))'%nome_banco)
                conn.commit()
                self.ui.label_3.clear()
                self.ui.listWidget.addItem(nome_banco)
                self.ui.label_3.setText("Criado com sucesso!")

            except:
                self.ui.label_3.setText("Este nome já esta em uso")

    def carrega_banco(self):


        createConnection()
        conn=MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="carga_residencia")
        tabela=self.ui.listWidget.currentItem().text()
        tabela=str(tabela)
        self.janela=MyForm(tabela)
        self.janela.show()
        QtCore.QObject.connect(self.janela, QtCore.SIGNAL('finished(int)'),conn.close)
        self.close()






