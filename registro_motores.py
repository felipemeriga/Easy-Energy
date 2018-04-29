# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registro_motores.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!



from PyQt4 import QtCore, QtGui
import MySQLdb


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
        Dialog.resize(447, 633)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Fernanda/Google Drive/Engenharia/TCC/Logo/logo_inv.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Mistral"))
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 111, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 150, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 141, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_add = QtGui.QPushButton(Dialog)
        self.pushButton_add.setGeometry(QtCore.QRect(150, 370, 75, 23))
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.pushButton_cancel = QtGui.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(240, 370, 75, 23))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.lineEdit_nome = QtGui.QLineEdit(Dialog)
        self.lineEdit_nome.setGeometry(QtCore.QRect(160, 90, 171, 20))
        self.lineEdit_nome.setObjectName(_fromUtf8("lineEdit_nome"))
        self.lineEdit_pot = QtGui.QLineEdit(Dialog)
        self.lineEdit_pot.setGeometry(QtCore.QRect(160, 120, 171, 20))
        self.lineEdit_pot.setObjectName(_fromUtf8("lineEdit_pot"))
        self.lineEdit_qnt = QtGui.QLineEdit(Dialog)
        self.lineEdit_qnt.setGeometry(QtCore.QRect(160, 150, 171, 20))
        self.lineEdit_qnt.setObjectName(_fromUtf8("lineEdit_qnt"))
        self.lineEdit_rend = QtGui.QLineEdit(Dialog)
        self.lineEdit_rend.setGeometry(QtCore.QRect(160, 180, 171, 20))
        self.lineEdit_rend.setObjectName(_fromUtf8("lineEdit_rend"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(-20, -10, 541, 721))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Fernanda/Google Drive/Engenharia/TCC/Logo/industria.jpg")))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_setor = QtGui.QLineEdit(Dialog)
        self.lineEdit_setor.setGeometry(QtCore.QRect(160, 60, 171, 20))
        self.lineEdit_setor.setObjectName(_fromUtf8("lineEdit_setor"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(70, 60, 81, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 210, 141, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_FP = QtGui.QLineEdit(Dialog)
        self.lineEdit_FP.setGeometry(QtCore.QRect(160, 210, 171, 20))
        self.lineEdit_FP.setObjectName(_fromUtf8("lineEdit_FP"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 240, 161, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_corrente = QtGui.QLineEdit(Dialog)
        self.lineEdit_corrente.setGeometry(QtCore.QRect(160, 240, 171, 20))
        self.lineEdit_corrente.setObjectName(_fromUtf8("lineEdit_corrente"))
        self.lineEdit_tensao = QtGui.QLineEdit(Dialog)
        self.lineEdit_tensao.setGeometry(QtCore.QRect(160, 270, 171, 20))
        self.lineEdit_tensao.setObjectName(_fromUtf8("lineEdit_tensao"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(20, 270, 161, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(20, 300, 161, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_horas_fora = QtGui.QLineEdit(Dialog)
        self.lineEdit_horas_fora.setGeometry(QtCore.QRect(160, 300, 171, 20))
        self.lineEdit_horas_fora.setObjectName(_fromUtf8("lineEdit_horas_fora"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(20, 330, 161, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_horas_ponta = QtGui.QLineEdit(Dialog)
        self.lineEdit_horas_ponta.setGeometry(QtCore.QRect(160, 330, 171, 20))
        self.lineEdit_horas_ponta.setObjectName(_fromUtf8("lineEdit_horas_ponta"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 430, 221, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit_converte = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_converte.setGeometry(QtCore.QRect(100, 40, 113, 20))
        self.lineEdit_converte.setObjectName(_fromUtf8("lineEdit_converte"))
        self.radioButtonCV = QtGui.QRadioButton(self.groupBox)
        self.radioButtonCV.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButtonCV.setObjectName(_fromUtf8("radioButtonCV"))
        self.radioButton_Watts = QtGui.QRadioButton(self.groupBox)
        self.radioButton_Watts.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_Watts.setObjectName(_fromUtf8("radioButton_Watts"))
        self.label_Conv_Result = QtGui.QLabel(self.groupBox)
        self.label_Conv_Result.setGeometry(QtCore.QRect(20, 100, 181, 16))
        self.label_Conv_Result.setObjectName(_fromUtf8("label_Conv_Result"))
        self.pushButton_converte = QtGui.QPushButton(self.groupBox)
        self.pushButton_converte.setGeometry(QtCore.QRect(120, 70, 75, 23))
        self.pushButton_converte.setObjectName(_fromUtf8("pushButton_converte"))
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton_add.raise_()
        self.pushButton_cancel.raise_()
        self.lineEdit_nome.raise_()
        self.lineEdit_pot.raise_()
        self.lineEdit_qnt.raise_()
        self.lineEdit_rend.raise_()
        self.lineEdit_setor.raise_()
        self.label_8.raise_()
        self.label_6.raise_()
        self.lineEdit_FP.raise_()
        self.label_10.raise_()
        self.lineEdit_corrente.raise_()
        self.lineEdit_tensao.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.lineEdit_horas_fora.raise_()
        self.label_13.raise_()
        self.lineEdit_horas_ponta.raise_()
        self.groupBox.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_setor, self.lineEdit_nome)
        Dialog.setTabOrder(self.lineEdit_nome, self.lineEdit_pot)
        Dialog.setTabOrder(self.lineEdit_pot, self.lineEdit_qnt)
        Dialog.setTabOrder(self.lineEdit_qnt, self.lineEdit_rend)
        Dialog.setTabOrder(self.lineEdit_rend, self.lineEdit_FP)
        Dialog.setTabOrder(self.lineEdit_FP, self.lineEdit_corrente)
        Dialog.setTabOrder(self.lineEdit_corrente, self.lineEdit_tensao)
        Dialog.setTabOrder(self.lineEdit_tensao, self.lineEdit_horas_fora)
        Dialog.setTabOrder(self.lineEdit_horas_fora, self.lineEdit_horas_ponta)
        Dialog.setTabOrder(self.lineEdit_horas_ponta, self.pushButton_add)
        Dialog.setTabOrder(self.pushButton_add, self.pushButton_cancel)
        Dialog.setTabOrder(self.pushButton_cancel, self.radioButtonCV)
        Dialog.setTabOrder(self.radioButtonCV, self.radioButton_Watts)
        Dialog.setTabOrder(self.radioButton_Watts, self.lineEdit_converte)
        Dialog.setTabOrder(self.lineEdit_converte, self.pushButton_converte)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Easy Energy", None))
        self.label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Mistral\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:600; font-style:italic; color:#005500;\">Cadastro de Motores</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "Nome da Carga:", None))
        self.label_3.setText(_translate("Dialog", "           Potência(CV):", None))
        self.label_4.setText(_translate("Dialog", "      Quantidade:", None))
        self.label_5.setText(_translate("Dialog", "               Rendimento:", None))
        self.pushButton_add.setText(_translate("Dialog", "Adicionar", None))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancelar", None))
        self.label_8.setText(_translate("Dialog", "                Setor:", None))
        self.label_6.setText(_translate("Dialog", "      Fator de Potência:", None))
        self.label_10.setText(_translate("Dialog", "Corrente média nas fases:", None))
        self.label_11.setText(_translate("Dialog", "    Tensão de linha nominal:", None))
        self.label_12.setText(_translate("Dialog", "      Horário Fora de ponta:", None))
        self.label_13.setText(_translate("Dialog", "              Horário de ponta:", None))
        self.groupBox.setTitle(_translate("Dialog", "Conversor Watts para CV/HP", None))
        self.radioButtonCV.setText(_translate("Dialog", "CV", None))
        self.radioButton_Watts.setText(_translate("Dialog", "HP", None))
        self.label_Conv_Result.setText(_translate("Dialog", "Resultado:", None))
        self.pushButton_converte.setText(_translate("Dialog", "Converter", None))



class Form_Motores(QtGui.QDialog):
    def __init__(self,tabela):
        QtGui.QWidget.__init__(self,)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_add,QtCore.SIGNAL('clicked()'),self.cadastro)
        QtCore.QObject.connect(self.ui.pushButton_cancel,QtCore.SIGNAL('clicked()'),self.close)
        QtCore.QObject.connect(self.ui.pushButton_converte,QtCore.SIGNAL('clicked()'),self.converte_cavalo)
        global tab_motor
        tab_motor=tabela
        QtGui.QWidget.setWindowTitle(self, "Easy Energy - Industrial - %s"%(tab_motor))
        print(tab_motor)


    def converte_cavalo(self):


        if(self.ui.radioButtonCV.isChecked()==True):

            valor=self.ui.lineEdit_converte.text()
            print("porra")
            if(valor!=""):
                valor=float(valor)
                resultado=valor/735.5
                self.ui.label_Conv_Result.setText("Resultado: %.3f CV"%resultado)
                self.ui.lineEdit_converte.clear()

        if(self.ui.radioButton_Watts.isChecked()==True):

            valor_w=self.ui.lineEdit_converte.text()

            if(valor_w!=""):

                valor_w=float(valor_w)
                resultado_w=valor_w/745.69
                self.ui.label_Conv_Result.setText("Resultado: %.3f HP"%resultado_w)
                self.ui.lineEdit_converte.clear()

    def cadastro(self):

        if(self.ui.lineEdit_setor.text()==""or self.ui.lineEdit_nome.text()=="" or self.ui.lineEdit_pot.text()==""or self.ui.lineEdit_qnt.text()=="" or self.ui.lineEdit_rend.text()=="" or self.ui.lineEdit_FP.text()=="" or self.ui.lineEdit_corrente.text()=="" or self.ui.lineEdit_tensao.text()==""):
            self.close()
        else:
            setor=str(self.ui.lineEdit_setor.text())
            nome_carga=str(self.ui.lineEdit_nome.text())
            pot=float(self.ui.lineEdit_pot.text())
            qnt=int(self.ui.lineEdit_qnt.text())
            rendimento=float(self.ui.lineEdit_rend.text())
            FP=float(self.ui.lineEdit_FP.text())
            corrente=float(self.ui.lineEdit_corrente.text())
            tensao=float(self.ui.lineEdit_tensao.text())
            tipo="Motor Trifásico"

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

            pot=pot*735.5
            pot=pot/rendimento

            conn=MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="cargas_industrial")
            cursor=conn.cursor()
            cursor.execute("""
            INSERT INTO %s(Setor, Tipo, Nome, Potência_W, Quantidade, rendimento, FP, Corrente_A, Tensão_V, HorasfPonta, HorasPonta)
            VALUES ('%s','%s','%s', %s, %d, %s, %s, %s, %s, %s, %s)
            """%(tab_motor,setor,tipo,nome_carga,pot,qnt,rendimento,FP,corrente,tensao,horas_fora,horas_ponta))
            conn.commit()
            self.close()

        def closeEvent(self, event):

            self.closed.emit()
            event.accept()