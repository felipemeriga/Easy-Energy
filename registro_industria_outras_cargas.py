# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registro_outras_cargas.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


import math


import MySQLdb
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

class Ui_Dialog_cargas(object):
    def setupUi(self, Dialog_cargas):
        Dialog_cargas.setObjectName(_fromUtf8("Dialog_cargas"))
        Dialog_cargas.resize(447, 408)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Fernanda/Google Drive/Engenharia/TCC/Logo/logo_inv.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_cargas.setWindowIcon(icon)
        self.label_cargas = QtGui.QLabel(Dialog_cargas)
        self.label_cargas.setGeometry(QtCore.QRect(30, 20, 341, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Mistral"))
        self.label_cargas.setFont(font)
        self.label_cargas.setObjectName(_fromUtf8("label_cargas"))
        self.label_2 = QtGui.QLabel(Dialog_cargas)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog_cargas)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 111, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog_cargas)
        self.label_4.setGeometry(QtCore.QRect(70, 150, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog_cargas)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 141, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_add = QtGui.QPushButton(Dialog_cargas)
        self.pushButton_add.setGeometry(QtCore.QRect(150, 350, 75, 23))
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.pushButton_cancel = QtGui.QPushButton(Dialog_cargas)
        self.pushButton_cancel.setGeometry(QtCore.QRect(250, 350, 75, 23))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.lineEdit_nome_cargas = QtGui.QLineEdit(Dialog_cargas)
        self.lineEdit_nome_cargas.setGeometry(QtCore.QRect(160, 90, 171, 20))
        self.lineEdit_nome_cargas.setObjectName(_fromUtf8("lineEdit_nome_cargas"))
        self.lineEdit_pot_cargas = QtGui.QLineEdit(Dialog_cargas)
        self.lineEdit_pot_cargas.setGeometry(QtCore.QRect(160, 120, 171, 20))
        self.lineEdit_pot_cargas.setObjectName(_fromUtf8("lineEdit_pot_cargas"))
        self.lineEdit_qnt_cargas = QtGui.QLineEdit(Dialog_cargas)
        self.lineEdit_qnt_cargas.setGeometry(QtCore.QRect(160, 150, 171, 20))
        self.lineEdit_qnt_cargas.setObjectName(_fromUtf8("lineEdit_qnt_cargas"))
        self.lineEdit_rend_cargas = QtGui.QLineEdit(Dialog_cargas)
        self.lineEdit_rend_cargas.setGeometry(QtCore.QRect(160, 180, 171, 20))
        self.lineEdit_rend_cargas.setObjectName(_fromUtf8("lineEdit_rend_cargas"))
        self.lineEdit_setor_cargas = QtGui.QLineEdit(Dialog_cargas)
        self.lineEdit_setor_cargas.setGeometry(QtCore.QRect(160, 60, 171, 20))
        self.lineEdit_setor_cargas.setObjectName(_fromUtf8("lineEdit_setor_cargas"))
        self.label_8 = QtGui.QLabel(Dialog_cargas)
        self.label_8.setGeometry(QtCore.QRect(70, 60, 81, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_6 = QtGui.QLabel(Dialog_cargas)
        self.label_6.setGeometry(QtCore.QRect(40, 210, 141, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_FP = QtGui.QLineEdit(Dialog_cargas)
        self.lineEdit_FP.setGeometry(QtCore.QRect(160, 210, 171, 20))
        self.lineEdit_FP.setObjectName(_fromUtf8("lineEdit_FP"))
        self.lineEdit_tensao = QtGui.QLineEdit(Dialog_cargas)
        self.lineEdit_tensao.setGeometry(QtCore.QRect(160, 240, 171, 20))
        self.lineEdit_tensao.setObjectName(_fromUtf8("lineEdit_tensao"))
        self.label_11 = QtGui.QLabel(Dialog_cargas)
        self.label_11.setGeometry(QtCore.QRect(20, 240, 161, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Dialog_cargas)
        self.label_12.setGeometry(QtCore.QRect(20, 270, 161, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_horas_fora = QtGui.QLineEdit(Dialog_cargas)
        self.lineEdit_horas_fora.setGeometry(QtCore.QRect(160, 270, 171, 20))
        self.lineEdit_horas_fora.setObjectName(_fromUtf8("lineEdit_horas_fora"))
        self.label_13 = QtGui.QLabel(Dialog_cargas)
        self.label_13.setGeometry(QtCore.QRect(20, 300, 161, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_horas_ponta = QtGui.QLineEdit(Dialog_cargas)
        self.lineEdit_horas_ponta.setGeometry(QtCore.QRect(160, 300, 171, 20))
        self.lineEdit_horas_ponta.setObjectName(_fromUtf8("lineEdit_horas_ponta"))
        self.label = QtGui.QLabel(Dialog_cargas)
        self.label.setGeometry(QtCore.QRect(-680, -120, 1141, 681))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Fernanda/Google Drive/Engenharia/TCC/Logo/industriaaaa.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.raise_()
        self.label_cargas.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton_add.raise_()
        self.pushButton_cancel.raise_()
        self.lineEdit_nome_cargas.raise_()
        self.lineEdit_pot_cargas.raise_()
        self.lineEdit_qnt_cargas.raise_()
        self.lineEdit_rend_cargas.raise_()
        self.lineEdit_setor_cargas.raise_()
        self.label_8.raise_()
        self.label_6.raise_()
        self.lineEdit_FP.raise_()
        self.lineEdit_tensao.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.lineEdit_horas_fora.raise_()
        self.label_13.raise_()
        self.lineEdit_horas_ponta.raise_()

        self.retranslateUi(Dialog_cargas)
        QtCore.QMetaObject.connectSlotsByName(Dialog_cargas)
        Dialog_cargas.setTabOrder(self.lineEdit_setor_cargas, self.lineEdit_nome_cargas)
        Dialog_cargas.setTabOrder(self.lineEdit_nome_cargas, self.lineEdit_pot_cargas)
        Dialog_cargas.setTabOrder(self.lineEdit_pot_cargas, self.lineEdit_qnt_cargas)
        Dialog_cargas.setTabOrder(self.lineEdit_qnt_cargas, self.lineEdit_rend_cargas)
        Dialog_cargas.setTabOrder(self.lineEdit_rend_cargas, self.lineEdit_FP)
        Dialog_cargas.setTabOrder(self.lineEdit_FP, self.lineEdit_tensao)
        Dialog_cargas.setTabOrder(self.lineEdit_tensao, self.lineEdit_horas_fora)
        Dialog_cargas.setTabOrder(self.lineEdit_horas_fora, self.lineEdit_horas_ponta)
        Dialog_cargas.setTabOrder(self.lineEdit_horas_ponta, self.pushButton_add)
        Dialog_cargas.setTabOrder(self.pushButton_add, self.pushButton_cancel)

    def retranslateUi(self, Dialog_cargas):
        Dialog_cargas.setWindowTitle(_translate("Dialog_cargas", "Easy Energy", None))
        self.label_cargas.setText(_translate("Dialog_cargas", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Mistral\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:600; font-style:italic; color:#005500;\">Cadastro de Cargas Gerais</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog_cargas", "Nome da Carga:", None))
        self.label_3.setText(_translate("Dialog_cargas", "           Potência(W):", None))
        self.label_4.setText(_translate("Dialog_cargas", "      Quantidade:", None))
        self.label_5.setText(_translate("Dialog_cargas", "               Rendimento:", None))
        self.pushButton_add.setText(_translate("Dialog_cargas", "Adicionar", None))
        self.pushButton_cancel.setText(_translate("Dialog_cargas", "Cancelar", None))
        self.label_8.setText(_translate("Dialog_cargas", "                Setor:", None))
        self.label_6.setText(_translate("Dialog_cargas", "      Fator de Potência:", None))
        self.label_11.setText(_translate("Dialog_cargas", "                Tensão nominal:", None))
        self.label_12.setText(_translate("Dialog_cargas", "      Horário Fora de ponta:", None))
        self.label_13.setText(_translate("Dialog_cargas", "              Horário de ponta:", None))



class Form_Outras_Cargas(QtGui.QDialog):
    def __init__(self,tabela):
        QtGui.QWidget.__init__(self,)
        self.ui=Ui_Dialog_cargas()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_add,QtCore.SIGNAL('clicked()'),self.cadastro)
        QtCore.QObject.connect(self.ui.pushButton_cancel,QtCore.SIGNAL('clicked()'),self.close)
        global tab_outras
        tab_outras=tabela
        QtGui.QWidget.setWindowTitle(self, "Easy Energy - Industrial - %s"%(tab_outras))
        print(tab_outras)

    def cadastro(self):

        if(self.ui.lineEdit_setor_cargas.text()==""or self.ui.lineEdit_nome_cargas.text()=="" or self.ui.lineEdit_pot_cargas.text()==""or self.ui.lineEdit_qnt_cargas.text()=="" or self.ui.lineEdit_rend_cargas.text()=="" or self.ui.lineEdit_FP.text()=="" or self.ui.lineEdit_tensao.text()==""):
            self.close()
        else:
            setor=str(self.ui.lineEdit_setor_cargas.text())
            nome_carga=str(self.ui.lineEdit_nome_cargas.text())
            pot=float(self.ui.lineEdit_pot_cargas.text())
            qnt=int(self.ui.lineEdit_qnt_cargas.text())
            rendimento=float(self.ui.lineEdit_rend_cargas.text())
            FP=float(self.ui.lineEdit_FP.text())
            tensao=float(self.ui.lineEdit_tensao.text())
            tipo="Cargas Gerais"

            #Atualização do valor de horário fora de ponta
            if self.ui.lineEdit_horas_fora.text() == "":
                horas_fora = 0

            else:
                horas_fora=float(self.ui.lineEdit_horas_fora.text())

            #Atualização do horário de ponta
            if self.ui.lineEdit_horas_ponta.text() == "":
                horas_ponta= 0

            else:
                horas_ponta=float(self.ui.lineEdit_horas_ponta.text())


            corrente=pot/tensao
            corrente=float(corrente)



            conn=MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="cargas_industrial")
            cursor=conn.cursor()
            cursor.execute("""
            INSERT INTO %s(Setor, Tipo, Nome, Potência_W, Quantidade, rendimento, FP, Corrente_A, Tensão_V, HorasfPonta, HorasPonta)
            VALUES ('%s','%s','%s', %s, %d, %s, %s, %.3f, %s, %s, %s)
            """%(tab_outras,setor,tipo,nome_carga,pot,qnt,rendimento,FP, corrente,tensao,horas_fora,horas_ponta))
            conn.commit()
            self.close()

        def closeEvent(self, event):

            self.closed.emit()
            event.accept()


