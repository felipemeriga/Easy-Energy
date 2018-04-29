# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cbanco1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


from Industrial import *

import sys
import MySQLdb
from PyQt4 import QtSql, QtGui

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

class Ui_Dialog_industrial(object):
    def setupUi(self, Dialog_industrial):
        Dialog_industrial.setObjectName(_fromUtf8("Dialog_industrial"))
        Dialog_industrial.resize(692, 551)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo\logo_inv.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_industrial.setWindowIcon(icon)
        self.tabWidget_industria = QtGui.QTabWidget(Dialog_industrial)
        self.tabWidget_industria.setGeometry(QtCore.QRect(30, 30, 631, 471))
        self.tabWidget_industria.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget_industria.setTabsClosable(False)
        self.tabWidget_industria.setMovable(False)
        self.tabWidget_industria.setObjectName(_fromUtf8("tabWidget_industria"))
        self.tab_industrial = QtGui.QWidget()
        self.tab_industrial.setObjectName(_fromUtf8("tab_industrial"))
        self.label_22 = QtGui.QLabel(self.tab_industrial)
        self.label_22.setGeometry(QtCore.QRect(130, 0, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setUnderline(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.pushButton_industria = QtGui.QPushButton(self.tab_industrial)
        self.pushButton_industria.setGeometry(QtCore.QRect(270, 240, 75, 23))
        self.pushButton_industria.setObjectName(_fromUtf8("pushButton_industria"))
        self.lineEdit_industria = QtGui.QLineEdit(self.tab_industrial)
        self.lineEdit_industria.setGeometry(QtCore.QRect(210, 160, 201, 20))
        self.lineEdit_industria.setObjectName(_fromUtf8("lineEdit_industria"))
        self.label_33 = QtGui.QLabel(self.tab_industrial)
        self.label_33.setGeometry(QtCore.QRect(210, 180, 201, 20))
        self.label_33.setText(_fromUtf8(""))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_66 = QtGui.QLabel(self.tab_industrial)
        self.label_66.setGeometry(QtCore.QRect(540, 0, 91, 91))
        self.label_66.setText(_fromUtf8(""))
        self.label_66.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo/pequeno.jpg")))
        self.label_66.setObjectName(_fromUtf8("label_66"))
        self.tabWidget_industria.addTab(self.tab_industrial, _fromUtf8(""))
        self.tab_2_industria = QtGui.QWidget()
        self.tab_2_industria.setObjectName(_fromUtf8("tab_2_industria"))
        self.listWidget_industria = QtGui.QListWidget(self.tab_2_industria)
        self.listWidget_industria.setGeometry(QtCore.QRect(70, 100, 481, 301))
        self.listWidget_industria.setObjectName(_fromUtf8("listWidget_industria"))
        self.pCarregar_industria = QtGui.QPushButton(self.tab_2_industria)
        self.pCarregar_industria.setGeometry(QtCore.QRect(180, 410, 75, 23))
        self.pCarregar_industria.setObjectName(_fromUtf8("pCarregar_industria"))
        self.pDeletar_industria = QtGui.QPushButton(self.tab_2_industria)
        self.pDeletar_industria.setGeometry(QtCore.QRect(350, 410, 75, 23))
        self.pDeletar_industria.setObjectName(_fromUtf8("pDeletar_industria"))
        self.label11 = QtGui.QLabel(self.tab_2_industria)
        self.label11.setGeometry(QtCore.QRect(50, 70, 481, 20))
        self.label11.setText(_fromUtf8(""))
        self.label11.setObjectName(_fromUtf8("label11"))
        self.label_44 = QtGui.QLabel(self.tab_2_industria)
        self.label_44.setGeometry(QtCore.QRect(130, 20, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setUnderline(True)
        self.label_44.setFont(font)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.label_55 = QtGui.QLabel(self.tab_2_industria)
        self.label_55.setGeometry(QtCore.QRect(540, 0, 91, 91))
        self.label_55.setText(_fromUtf8(""))
        self.label_55.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo/pequeno.jpg")))
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.tabWidget_industria.addTab(self.tab_2_industria, _fromUtf8(""))
        self.label_77 = QtGui.QLabel(Dialog_industrial)
        self.label_77.setGeometry(QtCore.QRect(-30, 0, 721, 561))
        self.label_77.setText(_fromUtf8(""))
        self.label_77.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo\engrepequeno.jpg")))
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.label_77.raise_()
        self.label_77.raise_()
        self.tabWidget_industria.raise_()

        self.retranslateUi(Dialog_industrial)
        self.tabWidget_industria.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_industrial)

    def retranslateUi(self, Dialog_industrial):
        Dialog_industrial.setWindowTitle(_translate("Dialog_industrial", "Easy Energy-Industrial", None))
        self.label_22.setText(_translate("Dialog_industrial", "Criar novo banco de dados", None))
        self.pushButton_industria.setText(_translate("Dialog_industrial", "Criar", None))
        self.tabWidget_industria.setTabText(self.tabWidget_industria.indexOf(self.tab_industrial), _translate("Dialog_industrial", "Criar Nova Tabela no Banco de Dados", None))
        __sortingEnabled = self.listWidget_industria.isSortingEnabled()
        self.listWidget_industria.setSortingEnabled(False)
        self.listWidget_industria.setSortingEnabled(__sortingEnabled)
        self.pCarregar_industria.setText(_translate("Dialog_industrial", "Carregar", None))
        self.pDeletar_industria.setText(_translate("Dialog_industrial", "Deletar", None))
        self.label_44.setText(_translate("Dialog_industrial", "Selecionar banco de dados", None))
        self.tabWidget_industria.setTabText(self.tabWidget_industria.indexOf(self.tab_2_industria), _translate("Dialog_industrial", "Carregar Banco de Dados", None))



class Form2_industrial(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui=Ui_Dialog_industrial()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pDeletar_industria,QtCore.SIGNAL("clicked()"),self.deletar_banco_industrial)
        QtCore.QObject.connect(self.ui.pushButton_industria,QtCore.SIGNAL("clicked()"),self.criar_banco_industrial)
        QtCore.QObject.connect(self.ui.pCarregar_industria,QtCore.SIGNAL("clicked()"),self.carrega_banco_industrial)
        connection = MySQLdb.connect(
                host = 'localhost',
                user = 'root',
                passwd = 'iloverpg1')  # create the connection
        cursor = connection.cursor()     # get the cursor


        cursor.execute("USE CARGAS_INDUSTRIAL") # select the database

        cursor.execute("SHOW TABLES")    # execute 'SHOW TABLES' (but data is not returned)

        tables = cursor.fetchall()
        for (table_name,) in cursor:
            self.ui.listWidget_industria.addItem(table_name)


    def deletar_banco_industrial(self):


        conn=MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="cargas_industrial")
        cursor=conn.cursor()
        a=self.ui.listWidget_industria.currentItem().text()
        cursor.execute('drop table %s' %a)
        self.ui.listWidget_industria.takeItem(self.ui.listWidget_industria.currentRow())



    def criar_banco_industrial(self):

        conn=MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="cargas_industrial")
        cursor=conn.cursor()
        nome_banco_industrial = str(self.ui.lineEdit_industria.text())
        if(nome_banco_industrial==""):
            self.ui.label_33.setText("Não Foi inserido nenhum nome")
        else:
            try:
                cursor.execute('create table %s (Setor char(50),Tipo char(50),Nome char(50),Potência_W varchar(50),Quantidade smallint,rendimento varchar(50),FP varchar(50),Corrente_A varchar(50),Tensão_V varchar(50),HorasfPonta varchar(50),HorasPonta varchar(50),Energia_kWh varchar(50))'%nome_banco_industrial)
                conn.commit()
                self.ui.label_33.clear()
                self.ui.listWidget_industria.addItem(nome_banco_industrial)
                self.ui.label_33.setText("Criado com sucesso!")
            except:
                self.ui.label_33.setText("Este nome já esta em uso")


    def carrega_banco_industrial(self):


        createConnection()
        conn=MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="cargas_industrial")
        tabela=self.ui.listWidget_industria.currentItem().text()
        tabela=str(tabela)
        self.janela_industrial=MyForm_Industrial(tabela)
        self.janela_industrial.show()
        QtCore.QObject.connect(self.janela_industrial, QtCore.SIGNAL('finished(int)'),conn.close)
        self.close()