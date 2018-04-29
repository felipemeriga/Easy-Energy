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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(439, 350)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo\logo_inv.bmp")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 261, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 111, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 180, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 141, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 270, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 270, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit_nome = QtGui.QLineEdit(Dialog)
        self.lineEdit_nome.setGeometry(QtCore.QRect(160, 120, 171, 20))
        self.lineEdit_nome.setObjectName(_fromUtf8("lineEdit_nome"))
        self.lineEdit_pot = QtGui.QLineEdit(Dialog)
        self.lineEdit_pot.setGeometry(QtCore.QRect(160, 150, 171, 20))
        self.lineEdit_pot.setObjectName(_fromUtf8("lineEdit_pot"))
        self.lineEdit_qnt = QtGui.QLineEdit(Dialog)
        self.lineEdit_qnt.setGeometry(QtCore.QRect(160, 180, 171, 20))
        self.lineEdit_qnt.setObjectName(_fromUtf8("lineEdit_qnt"))
        self.lineEdit_horas = QtGui.QLineEdit(Dialog)
        self.lineEdit_horas.setGeometry(QtCore.QRect(160, 210, 171, 20))
        self.lineEdit_horas.setObjectName(_fromUtf8("lineEdit_horas"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(-40, -30, 541, 561))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo/Energia01.png")))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_local = QtGui.QLineEdit(Dialog)
        self.lineEdit_local.setGeometry(QtCore.QRect(160, 90, 171, 20))
        self.lineEdit_local.setObjectName(_fromUtf8("lineEdit_local"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(70, 90, 81, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_nome.raise_()
        self.lineEdit_pot.raise_()
        self.lineEdit_qnt.raise_()
        self.lineEdit_horas.raise_()
        self.lineEdit_local.raise_()
        self.label_8.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Easy Energy", None))
        self.label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#005500;\">Cadastro de Cargas</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "Nome da Carga:", None))
        self.label_3.setText(_translate("Dialog", "            Potência(W):", None))
        self.label_4.setText(_translate("Dialog", "      Quantidade:", None))
        self.label_5.setText(_translate("Dialog", "    Horas de Utilização:", None))
        self.pushButton.setText(_translate("Dialog", "Adicionar", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar", None))
        self.label_8.setText(_translate("Dialog", "                Local:", None))

class Form1(QtGui.QDialog):
    def __init__(self,tabela):
        QtGui.QWidget.__init__(self,)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.cadastro)
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL('clicked()'),self.close)
        global tab1
        tab1=tabela
        QtGui.QWidget.setWindowTitle(self, "Easy Energy - Residencial/Comercial - %s"%(tab1))
        print(tab1)



    def cadastro(self):

        if(self.ui.lineEdit_nome.text()=="" or self.ui.lineEdit_pot.text()==""or self.ui.lineEdit_qnt.text()=="" or self.ui.lineEdit_local.text()==""):

            self.close()
        else:
            nome_carga=str(self.ui.lineEdit_nome.text())
            pot=float(self.ui.lineEdit_pot.text())
            qnt=int(self.ui.lineEdit_qnt.text())
            local=str(self.ui.lineEdit_local.text())

            if self.ui.lineEdit_horas.text() == "":
                horas = 0

            else:
                horas=float(self.ui.lineEdit_horas.text())

            conn=MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="carga_residencia")
            cursor=conn.cursor()
            cursor.execute("""
            INSERT INTO %s(Local, Nome, Potência_Watts, Quantidade, Horas)
            VALUES ('%s','%s', %s, %d, %s)
            """%(tab1,local,nome_carga,pot,qnt,horas))
            conn.commit()
            self.close()



        def closeEvent(self, event):

            self.closed.emit()
            event.accept()


