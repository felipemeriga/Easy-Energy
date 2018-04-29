# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DEFINITIVOINDUSTRIA.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import QtSql, QtGui
import MySQLdb

fix_encoding = lambda s: s.decode('utf8', 'ignore')

from registro_motores import *
from registro_industria_outras_cargas import *

# VARIAVEIS GLOBAIS ATUALIZAR INFORMAÇÕES

grupo = 0
tab = 1
database = "cargas_industrial"
libera_tabela = 0

# VARIAVEIS GLOBAIS PARA GRUPO B

grupo_b_nome = 0
kilowatt_hora = 0.76683

# VARIAVEIS GLOBAIS PARA GRUPO A

grupo_a_nome = 0
grupo_a_tipo = 0
kilowatt_hora_a_fponta = 0
kilowatt_hora_a_ponta = 0
demanda_unica = 0
ultrapassagem_unica = 0
demanda_fponta = 0
demanda_ponta = 0
ultrapassagem_fponta = 0
ultrapassagem_ponta = 0

# VARIAVEIS GLOBAIS INFORMAÇÕES GERAIS

demanda_contratada_fora = 0
demanda_contratada_ponta = 0
dias_ativos = 25
ultrapassagem_fponta_informada = 0
ultrapassagem_ponta_informada = 0
demanda_maxima = 0

conn = MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="cargas_industrial", charset='utf8')

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


class Ui_Dialog_Industrial1(object):
    def setupUi(self, Dialog_Industrial1):
        Dialog_Industrial1.setObjectName(_fromUtf8("Dialog_Industrial1"))
        Dialog_Industrial1.resize(1266, 716)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo\logo_inv.png")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_Industrial1.setWindowIcon(icon)
        self.UpdateButton = QtGui.QPushButton(Dialog_Industrial1)
        self.UpdateButton.setGeometry(QtCore.QRect(50, 590, 131, 23))
        self.UpdateButton.setAutoFillBackground(False)
        self.UpdateButton.setAutoDefault(True)
        self.UpdateButton.setDefault(False)
        self.UpdateButton.setFlat(False)
        self.UpdateButton.setObjectName(_fromUtf8("UpdateButton"))
        self.CancelButton = QtGui.QPushButton(Dialog_Industrial1)
        self.CancelButton.setGeometry(QtCore.QRect(210, 590, 131, 23))
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.InsertButton = QtGui.QPushButton(Dialog_Industrial1)
        self.InsertButton.setGeometry(QtCore.QRect(390, 590, 131, 23))
        self.InsertButton.setObjectName(_fromUtf8("InsertButton"))
        self.DeleteButton = QtGui.QPushButton(Dialog_Industrial1)
        self.DeleteButton.setGeometry(QtCore.QRect(580, 590, 131, 23))
        self.DeleteButton.setObjectName(_fromUtf8("DeleteButton"))
        self.FilterButton = QtGui.QPushButton(Dialog_Industrial1)
        self.FilterButton.setGeometry(QtCore.QRect(290, 280, 75, 23))
        self.FilterButton.setObjectName(_fromUtf8("FilterButton"))
        self.label = QtGui.QLabel(Dialog_Industrial1)
        self.label.setGeometry(QtCore.QRect(30, 280, 51, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.prodname = QtGui.QLineEdit(Dialog_Industrial1)
        self.prodname.setGeometry(QtCore.QRect(160, 280, 113, 21))
        self.prodname.setObjectName(_fromUtf8("prodname"))
        self.radioButton = QtGui.QRadioButton(Dialog_Industrial1)
        self.radioButton.setGeometry(QtCore.QRect(90, 280, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Dialog_Industrial1)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 300, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label_Pot_total = QtGui.QLabel(Dialog_Industrial1)
        self.label_Pot_total.setGeometry(QtCore.QRect(10, 640, 251, 16))
        self.label_Pot_total.setObjectName(_fromUtf8("label_Pot_total"))
        self.label_numero_diversas = QtGui.QLabel(Dialog_Industrial1)
        self.label_numero_diversas.setGeometry(QtCore.QRect(20, 670, 201, 20))
        self.label_numero_diversas.setObjectName(_fromUtf8("label_numero_diversas"))
        self.line = QtGui.QFrame(Dialog_Industrial1)
        self.line.setGeometry(QtCore.QRect(160, 660, 118, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog_Industrial1)
        self.line_2.setGeometry(QtCore.QRect(160, 690, 118, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.DeleteButton_all = QtGui.QPushButton(Dialog_Industrial1)
        self.DeleteButton_all.setGeometry(QtCore.QRect(750, 590, 131, 23))
        self.DeleteButton_all.setObjectName(_fromUtf8("DeleteButton_all"))
        self.registrar_outras_button = QtGui.QPushButton(Dialog_Industrial1)
        self.registrar_outras_button.setGeometry(QtCore.QRect(940, 590, 131, 23))
        self.registrar_outras_button.setObjectName(_fromUtf8("registrar_outras_button"))
        self.tableView_industria = QtGui.QTableView(Dialog_Industrial1)
        self.tableView_industria.setGeometry(QtCore.QRect(50, 340, 1171, 231))
        self.tableView_industria.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableView_industria.setObjectName(_fromUtf8("tableView_industria"))
        self.label_5 = QtGui.QLabel(Dialog_Industrial1)
        self.label_5.setGeometry(QtCore.QRect(-40, 0, 1401, 831))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(
            QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo\industriaaaa.jpg")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.groupBox_5 = QtGui.QGroupBox(Dialog_Industrial1)
        self.groupBox_5.setGeometry(QtCore.QRect(110, 50, 561, 221))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(60, 20, 111, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_Concessonaria = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_Concessonaria.setGeometry(QtCore.QRect(150, 20, 91, 20))
        self.lineEdit_Concessonaria.setObjectName(_fromUtf8("lineEdit_Concessonaria"))
        self.label_10 = QtGui.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(-10, 50, 161, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_kWh_fponta = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_kWh_fponta.setGeometry(QtCore.QRect(150, 50, 91, 20))
        self.lineEdit_kWh_fponta.setObjectName(_fromUtf8("lineEdit_kWh_fponta"))
        self.label_13 = QtGui.QLabel(self.groupBox_5)
        self.label_13.setGeometry(QtCore.QRect(0, 110, 161, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_ativo_mes = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_ativo_mes.setGeometry(QtCore.QRect(150, 110, 91, 20))
        self.lineEdit_ativo_mes.setObjectName(_fromUtf8("lineEdit_ativo_mes"))
        self.label_12 = QtGui.QLabel(self.groupBox_5)
        self.label_12.setGeometry(QtCore.QRect(-10, 80, 161, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_kWh_Ponta = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_kWh_Ponta.setGeometry(QtCore.QRect(150, 80, 91, 20))
        self.lineEdit_kWh_Ponta.setObjectName(_fromUtf8("lineEdit_kWh_Ponta"))
        self.label_14 = QtGui.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(0, 140, 161, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_dcontratadaponta = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_dcontratadaponta.setGeometry(QtCore.QRect(150, 140, 91, 20))
        self.lineEdit_dcontratadaponta.setObjectName(_fromUtf8("lineEdit_dcontratadaponta"))
        self.label_11 = QtGui.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(280, 20, 171, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_15 = QtGui.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(270, 50, 171, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(240, 80, 211, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.lineEdit_dcontratadafponta = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_dcontratadafponta.setGeometry(QtCore.QRect(450, 20, 91, 20))
        self.lineEdit_dcontratadafponta.setObjectName(_fromUtf8("lineEdit_dcontratadafponta"))
        self.lineEdit_ultrapassagemponta = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_ultrapassagemponta.setGeometry(QtCore.QRect(450, 50, 91, 20))
        self.lineEdit_ultrapassagemponta.setObjectName(_fromUtf8("lineEdit_ultrapassagemponta"))
        self.lineEdit_ultrapassagem_fponta = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_ultrapassagem_fponta.setGeometry(QtCore.QRect(450, 80, 91, 20))
        self.lineEdit_ultrapassagem_fponta.setObjectName(_fromUtf8("lineEdit_ultrapassagem_fponta"))
        self.atualiazar_info_button = QtGui.QPushButton(self.groupBox_5)
        self.atualiazar_info_button.setGeometry(QtCore.QRect(210, 180, 151, 23))
        self.atualiazar_info_button.setObjectName(_fromUtf8("atualiazar_info_button"))
        self.label_17 = QtGui.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(210, 110, 241, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.lineEdit_demanda_faturavel_fora = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_demanda_faturavel_fora.setGeometry(QtCore.QRect(450, 110, 91, 20))
        self.lineEdit_demanda_faturavel_fora.setObjectName(_fromUtf8("lineEdit_demanda_faturavel_fora"))
        self.label_numero_motores = QtGui.QLabel(Dialog_Industrial1)
        self.label_numero_motores.setGeometry(QtCore.QRect(280, 640, 201, 16))
        self.label_numero_motores.setObjectName(_fromUtf8("label_numero_motores"))
        self.line_3 = QtGui.QFrame(Dialog_Industrial1)
        self.line_3.setGeometry(QtCore.QRect(380, 660, 118, 3))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_consumo = QtGui.QLabel(Dialog_Industrial1)
        self.label_consumo.setGeometry(QtCore.QRect(300, 680, 201, 16))
        self.label_consumo.setObjectName(_fromUtf8("label_consumo"))
        self.line_4 = QtGui.QFrame(Dialog_Industrial1)
        self.line_4.setGeometry(QtCore.QRect(380, 695, 118, 3))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_4 = QtGui.QLabel(Dialog_Industrial1)
        self.label_4.setGeometry(QtCore.QRect(470, 10, 381, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Kozuka Gothic Pr6N B"))
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.registrar_motor_button = QtGui.QPushButton(Dialog_Industrial1)
        self.registrar_motor_button.setGeometry(QtCore.QRect(1110, 590, 131, 23))
        self.registrar_motor_button.setObjectName(_fromUtf8("registrar_motor_button"))
        self.radioButton_3 = QtGui.QRadioButton(Dialog_Industrial1)
        self.radioButton_3.setGeometry(QtCore.QRect(90, 320, 82, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.listWidget_classes = QtGui.QListWidget(Dialog_Industrial1)
        self.listWidget_classes.setGeometry(QtCore.QRect(880, 110, 251, 121))
        self.listWidget_classes.setObjectName(_fromUtf8("listWidget_classes"))
        self.label_9 = QtGui.QLabel(Dialog_Industrial1)
        self.label_9.setGeometry(QtCore.QRect(890, 50, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.pushButton_grupoA = QtGui.QPushButton(Dialog_Industrial1)
        self.pushButton_grupoA.setGeometry(QtCore.QRect(910, 80, 75, 23))
        self.pushButton_grupoA.setObjectName(_fromUtf8("pushButton_grupoA"))
        self.pushButton_grupoB = QtGui.QPushButton(Dialog_Industrial1)
        self.pushButton_grupoB.setGeometry(QtCore.QRect(1030, 80, 75, 23))
        self.pushButton_grupoB.setObjectName(_fromUtf8("pushButton_grupoB"))
        self.pushButton_sel_classes = QtGui.QPushButton(Dialog_Industrial1)
        self.pushButton_sel_classes.setGeometry(QtCore.QRect(970, 250, 75, 23))
        self.pushButton_sel_classes.setObjectName(_fromUtf8("pushButton_sel_classes"))
        self.label_FD = QtGui.QLabel(Dialog_Industrial1)
        self.label_FD.setGeometry(QtCore.QRect(530, 640, 201, 16))
        self.label_FD.setObjectName(_fromUtf8("label_FD"))
        self.line_5 = QtGui.QFrame(Dialog_Industrial1)
        self.line_5.setGeometry(QtCore.QRect(630, 660, 118, 3))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label_FP = QtGui.QLabel(Dialog_Industrial1)
        self.label_FP.setGeometry(QtCore.QRect(530, 670, 201, 16))
        self.label_FP.setObjectName(_fromUtf8("label_FP"))
        self.line_6 = QtGui.QFrame(Dialog_Industrial1)
        self.line_6.setGeometry(QtCore.QRect(630, 690, 118, 3))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_tarifa = QtGui.QLabel(Dialog_Industrial1)
        self.label_tarifa.setGeometry(QtCore.QRect(770, 640, 201, 16))
        self.label_tarifa.setObjectName(_fromUtf8("label_tarifa"))
        self.line_7 = QtGui.QFrame(Dialog_Industrial1)
        self.line_7.setGeometry(QtCore.QRect(820, 660, 118, 3))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.groupBox_bandeira = QtGui.QGroupBox(Dialog_Industrial1)
        self.groupBox_bandeira.setGeometry(QtCore.QRect(700, 50, 161, 121))
        self.groupBox_bandeira.setObjectName(_fromUtf8("groupBox_bandeira"))
        self.radioButton_verde = QtGui.QRadioButton(self.groupBox_bandeira)
        self.radioButton_verde.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_verde.setObjectName(_fromUtf8("radioButton_verde"))
        self.radioButton_amarelo = QtGui.QRadioButton(self.groupBox_bandeira)
        self.radioButton_amarelo.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioButton_amarelo.setObjectName(_fromUtf8("radioButton_amarelo"))
        self.radioButton_vermelho = QtGui.QRadioButton(self.groupBox_bandeira)
        self.radioButton_vermelho.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_vermelho.setObjectName(_fromUtf8("radioButton_vermelho"))
        self.label_5.raise_()
        self.UpdateButton.raise_()
        self.CancelButton.raise_()
        self.InsertButton.raise_()
        self.DeleteButton.raise_()
        self.FilterButton.raise_()
        self.label.raise_()
        self.prodname.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.label_Pot_total.raise_()
        self.label_numero_diversas.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.DeleteButton_all.raise_()
        self.registrar_outras_button.raise_()
        self.tableView_industria.raise_()
        self.groupBox_5.raise_()
        self.label_numero_motores.raise_()
        self.line_3.raise_()
        self.label_consumo.raise_()
        self.line_4.raise_()
        self.label_4.raise_()
        self.registrar_motor_button.raise_()
        self.radioButton_3.raise_()
        self.listWidget_classes.raise_()
        self.label_9.raise_()
        self.pushButton_grupoA.raise_()
        self.pushButton_grupoB.raise_()
        self.pushButton_sel_classes.raise_()
        self.label_FD.raise_()
        self.line_5.raise_()
        self.label_FP.raise_()
        self.line_6.raise_()
        self.label_tarifa.raise_()
        self.line_7.raise_()
        self.groupBox_bandeira.raise_()

        self.retranslateUi(Dialog_Industrial1)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Industrial1)

    def retranslateUi(self, Dialog_Industrial1):
        Dialog_Industrial1.setWindowTitle(_translate("Dialog_Industrial1", "Easy Energy", None))
        self.UpdateButton.setText(_translate("Dialog_Industrial1", "Atualizar", None))
        self.CancelButton.setText(_translate("Dialog_Industrial1", "Cancelar", None))
        self.InsertButton.setText(_translate("Dialog_Industrial1", "Adicionar", None))
        self.DeleteButton.setText(_translate("Dialog_Industrial1", "Deletar", None))
        self.FilterButton.setText(_translate("Dialog_Industrial1", "Filtrar", None))
        self.label.setText(_translate("Dialog_Industrial1", "Filtrar por:", None))
        self.radioButton.setText(_translate("Dialog_Industrial1", "Nome", None))
        self.radioButton_2.setText(_translate("Dialog_Industrial1", "Potência", None))
        self.label_Pot_total.setText(_translate("Dialog_Industrial1", " Potência Total Instalada(kW):", None))
        self.label_numero_diversas.setText(_translate("Dialog_Industrial1", " Número de Cargas Diversas:", None))
        self.DeleteButton_all.setText(_translate("Dialog_Industrial1", "Deletar Tudo", None))
        self.registrar_outras_button.setText(_translate("Dialog_Industrial1", "Registrar Outras Cargas", None))
        self.groupBox_5.setTitle(_translate("Dialog_Industrial1", "Atualizar Dados", None))
        self.label_6.setText(_translate("Dialog_Industrial1", "  Concessionária:", None))
        self.label_10.setText(_translate("Dialog_Industrial1", "       kWh(Preço) Fora de Ponta:", None))
        self.label_13.setText(_translate("Dialog_Industrial1", "            Periodo Ativo do mês:", None))
        self.label_12.setText(_translate("Dialog_Industrial1", "                    kWh(Preço) Ponta:", None))
        self.label_14.setText(_translate("Dialog_Industrial1", " Demanda Contratada Ponta:", None))
        self.label_11.setText(_translate("Dialog_Industrial1", "Demanda Contratada Fora Ponta:", None))
        self.label_15.setText(_translate("Dialog_Industrial1", "      Ultrapassagem Demanda Ponta:", None))
        self.label_16.setText(_translate("Dialog_Industrial1", "   Ultrapassagem Demanda Fora de Ponta:", None))
        self.atualiazar_info_button.setText(_translate("Dialog_Industrial1", "Atualizar", None))
        self.label_17.setText(
            _translate("Dialog_Industrial1", "                                                Demanda Máxima:", None))
        self.label_numero_motores.setText(_translate("Dialog_Industrial1", "Número de Motores:", None))
        self.label_consumo.setText(_translate("Dialog_Industrial1", "Consumo Total:", None))
        self.label_4.setText(_translate("Dialog_Industrial1", "Diagnóstico Consumo Industrial", None))
        self.registrar_motor_button.setText(_translate("Dialog_Industrial1", "Registrar Motores", None))
        self.radioButton_3.setText(_translate("Dialog_Industrial1", "Tipo", None))
        self.label_9.setText(_translate("Dialog_Industrial1", "Selecionar Classe e tipo de Tarifa:", None))
        self.pushButton_grupoA.setText(_translate("Dialog_Industrial1", "Grupo A", None))
        self.pushButton_grupoB.setText(_translate("Dialog_Industrial1", "Grupo B", None))
        self.pushButton_sel_classes.setText(_translate("Dialog_Industrial1", "Selecionar", None))
        self.label_FD.setText(_translate("Dialog_Industrial1", "Fator de Demanda:", None))
        self.label_FP.setText(_translate("Dialog_Industrial1", "Fator de Potência:", None))
        self.label_tarifa.setText(_translate("Dialog_Industrial1", "Tarifa(R$):", None))
        self.groupBox_bandeira.setTitle(_translate("Dialog_Industrial1", "Bandeira Tarifária", None))
        self.radioButton_verde.setText(_translate("Dialog_Industrial1", "Verde", None))
        self.radioButton_amarelo.setText(_translate("Dialog_Industrial1", "Amarela", None))
        self.radioButton_vermelho.setText(_translate("Dialog_Industrial1", "Vermelha", None))


# CRIAR CONEXAO BANCO DE DADOS
def createConnection():
    db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName('localhost')
    db.setDatabaseName("%s" % database)
    db.setUserName('root')
    db.setPassword('iloverpg1')
    db.open()
    print(db.lastError().text())
    return True


# CLASSE PARA INICIAR A INTERFACE GRAFICA E TODA SUA FUNCIONALIDADE
class MyForm_Industrial(QtGui.QDialog):
    # DEFINIÇÕES
    def __init__(self, tabela):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Dialog_Industrial1()
        self.ui.setupUi(self)
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("%s" % tabela)
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()
        QtGui.QWidget.setWindowTitle(self, "Easy Energy - Industrial - %s" % (tabela))
        self.ui.tableView_industria.setModel(self.model)

        # TRIGGERS
        QtCore.QObject.connect(self.ui.registrar_motor_button, QtCore.SIGNAL('clicked()'), self.registrar_motores)
        QtCore.QObject.connect(self.ui.registrar_outras_button, QtCore.SIGNAL('clicked()'),
                               self.registrar_outras_cargas)
        QtCore.QObject.connect(self.ui.UpdateButton, QtCore.SIGNAL('clicked()'), self.UpdateRecords)
        QtCore.QObject.connect(self.ui.CancelButton, QtCore.SIGNAL('clicked()'), self.CancelChanges)
        QtCore.QObject.connect(self.ui.InsertButton, QtCore.SIGNAL('clicked()'), self.InsertRecords)
        QtCore.QObject.connect(self.ui.DeleteButton, QtCore.SIGNAL('clicked()'), self.DeleteRecords)
        QtCore.QObject.connect(self.ui.FilterButton, QtCore.SIGNAL('clicked()'), self.Filtrar)
        QtCore.QObject.connect(self.ui.DeleteButton_all, QtCore.SIGNAL('clicked()'), self.DeleteAll)
        QtCore.QObject.connect(self.ui.pushButton_grupoB, QtCore.SIGNAL('clicked()'), self.tabela_muda_grupoB)
        QtCore.QObject.connect(self.ui.pushButton_grupoA, QtCore.SIGNAL('clicked()'), self.tabela_muda_grupoA)
        QtCore.QObject.connect(self.ui.pushButton_sel_classes, QtCore.SIGNAL('clicked()'),
                               self.seleciona_classe_tarifaria)
        QtCore.QObject.connect(self.ui.atualiazar_info_button, QtCore.SIGNAL('clicked()'),
                               self.atualiza_informações_gerais)
        # ATALHOS

        global tab
        tab = tabela
        self.ui.radioButton.setChecked(1)

    # FUNÇÃO PARA CHAMAR JANELA DE REGISTRO DE MOTORES
    def registrar_motores(self):

        self.registra_motores = Form_Motores(tab)
        QtCore.QObject.connect(self.registra_motores, QtCore.SIGNAL('finished(int)'), self.show)
        QtCore.QObject.connect(self.registra_motores, QtCore.SIGNAL('finished(int)'), self.UpdateRecords)
        QtCore.QObject.connect(self.registra_motores, QtCore.SIGNAL('finished(int)'), self.model.submitAll)
        self.registra_motores.show()
        self.hide()

    # FUNÇÃO PARA CHAMAR JANELA DE REGISTRO DE OUTRAS CARGAS
    def registrar_outras_cargas(self):

        self.registra_outras = Form_Outras_Cargas(tab)
        QtCore.QObject.connect(self.registra_outras, QtCore.SIGNAL('finished(int)'), self.show)
        QtCore.QObject.connect(self.registra_outras, QtCore.SIGNAL('finished(int)'), self.UpdateRecords)
        QtCore.QObject.connect(self.registra_outras, QtCore.SIGNAL('finished(int)'), self.model.submitAll)
        self.registra_outras.show()
        self.hide()

    # FUNÇÃO PARA CALCULO DE TODAS VARIÁVEIS DE CONSUMO
    def atualizar_colunas_de_energia(self):

        file = open("testfile.txt", "w")
        pototal_label = 0
        energtotal = 0
        consumo = 0
        consumo_total_label = 0
        numero_cargas_diversas_label = 0
        numero_motores_label = 0
        fator_demanda_label = 0
        fator_potencia_label = 0
        contagem_motor = 0
        contagem_outras_cargas = 0

        cursor = conn.cursor()
        b = self.model.rowCount()

        for i in range(b):
            self.record = self.model.record(i)
            # POTENCIA
            if self.record.value("Potência_W") == None:
                pot_w = 0
            else:
                pot_w = float(self.record.value("Potência_W"))
            # QUANTIDADE
            if self.record.value("Quantidade") == None:
                qnt = 0
            else:
                qnt = self.record.value("Quantidade")
            # RENDIMENTO
            if self.record.value("rendimento") == None:
                rendimento = 0
            else:
                rendimento = float(self.record.value("rendimento"))
            # FATOR DE POTENCIA
            if self.record.value("FP") == None:
                fp = 0
            else:
                fp = float(self.record.value("FP"))
            # CORRENTE
            if self.record.value("Corrente_A") == None:
                corrente = 0
            else:
                corrente = float(self.record.value("Corrente_A"))
            # TENSAO
            if self.record.value("Tensão_V") == None:
                tensao = 0
            else:
                tensao = float(self.record.value("Tensão_V"))
            # HORAS FORA DE PONTA
            if self.record.value("HorasfPonta") == None:
                horasfponta = 0
            else:
                horasfponta = float(self.record.value("HorasfPonta"))
            # HORAS DE PONTA
            if self.record.value("HorasPonta") == None:
                horasponta = 0
            else:
                horasponta = float(self.record.value("HorasPonta"))

            nome = str(self.record.value("Nome"))

            energ = (qnt * pot_w * (horasponta + horasfponta)) / 1000

            cursor.execute("SELECT * from %s where Nome='%s'" % (tab, nome))
            cursor.execute("UPDATE %s set Energia_kWh=%.3f where Nome='%s'" % (tab, energ, nome))
            conn.commit()
            if (self.record.value("Tipo") == "Motor Trifásico"):
                contagem_motor = contagem_motor + qnt
                corrente_calcula = float((((pot_w / rendimento) / fp) / (1.732050808 * tensao)))

                if (corrente > corrente_calcula):
                    file.write(
                        "        %s\nCorrente Informada: %.3f\nCorrente Calculada: %.3f\n Sub-dimensionado\n\n" % (
                        nome, corrente, corrente_calcula))
                else:
                    file.write(
                        "        %s\nCorrente Informada: %.3f\nCorrente Calculada: %.3f\n Super-dimensionado\n\n" % (
                        nome, corrente, corrente_calcula))
            else:
                contagem_outras_cargas = contagem_outras_cargas + qnt

            if grupo == "A":

                if (grupo_a_tipo == "verde"):
                    pototal_label = pototal_label + pot_w * qnt
                    consumo = (pot_w * qnt * horasfponta * kilowatt_hora_a_fponta) / 1000 + (
                                pot_w * qnt * horasponta * kilowatt_hora_a_ponta) / 1000
                    consumo_total_label = consumo + consumo_total_label
                    energtotal = energ + energtotal
                    fator_potencia_label = fp * qnt + fator_potencia_label

                if (grupo_a_tipo == "azul"):
                    pototal_label = pototal_label + pot_w * qnt
                    consumo = (pot_w * qnt * horasfponta * kilowatt_hora_a_fponta) / 1000 + (
                                pot_w * qnt * horasponta * kilowatt_hora_a_ponta) / 1000
                    consumo_total_label = consumo + consumo_total_label
                    energtotal = energ + energtotal
                    fator_potencia_label = fp * qnt + fator_potencia_label

                if (grupo_a_tipo == "convencional"):
                    pototal_label = pototal_label + pot_w * qnt
                    consumo = (pot_w * qnt * horasfponta * kilowatt_hora_a_fponta) / 1000 + (
                                pot_w * qnt * horasponta * kilowatt_hora_a_ponta) / 1000
                    consumo_total_label = consumo + consumo_total_label
                    energtotal = energ + energtotal
                    fator_potencia_label = fp * qnt + fator_potencia_label

            if grupo == "B":
                pototal_label = pototal_label + pot_w * qnt
                consumo = (pot_w * qnt * horasfponta * kilowatt_hora) / 1000 + (
                            pot_w * qnt * horasponta * kilowatt_hora) / 1000
                consumo_total_label = consumo + consumo_total_label
                energtotal = energ + energtotal
                fator_potencia_label = fp * qnt + fator_potencia_label

        if (grupo == "A"):
            consumo_total_label = consumo_total_label * dias_ativos
            energtotal = energtotal * dias_ativos
            fator_potencia_medio = fator_potencia_label / (contagem_motor + contagem_outras_cargas)

            if (grupo_a_tipo == "verde"):
                consumo_total_label = consumo_total_label + demanda_unica * (demanda_contratada_fora) + (
                            ultrapassagem_ponta_informada + ultrapassagem_fponta_informada) * ultrapassagem_unica * 2

            if (grupo_a_tipo == "azul"):
                consumo_total_label = consumo_total_label + (demanda_contratada_ponta * demanda_ponta) + (
                            demanda_contratada_fora * demanda_fponta) + (
                                                  ultrapassagem_fponta_informada * ultrapassagem_fponta * 2) + (
                                                  ultrapassagem_ponta_informada * ultrapassagem_ponta * 2)

            if (grupo_a_tipo == "convencional"):
                consumo_total_label = consumo_total_label + demanda_unica * demanda_contratada_fora * 2

            pototal_label = pototal_label / 1000
            fator_demanda_label = demanda_contratada_fora / pototal_label

            if (fator_potencia_medio < 0.92):
                fer = energtotal * ((0.92 / fator_potencia_medio) - 1) * kilowatt_hora_a_fponta
                if (demanda_maxima > demanda_contratada_fora):
                    if (grupo_a_tipo == "azul"):
                        fdr = float(
                            (demanda_maxima * (0.92 / fator_potencia_medio) - demanda_contratada_fora) * demanda_fponta)
                        consumo_total_label = consumo_total_label + fer + fdr
                    if (grupo_a_tipo == "verde"):
                        fdr = float(
                            (demanda_maxima * (0.92 / fator_potencia_medio) - demanda_contratada_fora) * demanda_unica)
                        consumo_total_label = consumo_total_label + fer + fdr

                else:
                    consumo_total_label = consumo_total_label + fer

            # PARTE REFERENTE AS BANDEIRAS TARIFARIAS
            if (self.ui.radioButton_amarelo.isChecked()):
                consumo_total_label = consumo_total_label + energtotal * 0.015

            if (self.ui.radioButton_vermelho.isChecked()):
                consumo_total_label = consumo_total_label + energtotal * 0.030

            self.ui.label_Pot_total.setText("Potência Total Instalada(kW): %.3f kW" % pototal_label)
            self.ui.label_numero_diversas.setText("Número de Cargas Diversas: %d" % contagem_outras_cargas)
            self.ui.label_numero_motores.setText("Número de Motores: %d" % contagem_motor)
            self.ui.label_consumo.setText("Consumo Total: %.3f kWh" % energtotal)
            self.ui.label_FP.setText("Fator de Potência: %.3f" % fator_potencia_medio)
            self.ui.label_tarifa.setText("Fatura(R$): %.2f" % consumo_total_label)
            self.ui.label_FD.setText("Fator de Demanda: %.3f" % fator_demanda_label)
        if (grupo == "B"):
            consumo_total_label = consumo_total_label * dias_ativos
            energtotal = energtotal * dias_ativos
            fator_potencia_medio = fator_potencia_label / (contagem_motor + contagem_outras_cargas)
            pototal_label = pototal_label / 1000
            self.ui.label_Pot_total.setText("Potência Total Instalada(kW): %.3f kW" % pototal_label)
            self.ui.label_numero_diversas.setText("Número de Cargas Diversas: %d" % contagem_outras_cargas)
            self.ui.label_numero_motores.setText("Número de Motores: %d" % contagem_motor)
            self.ui.label_consumo.setText("Consumo Total: %.3f kWh" % energtotal)
            self.ui.label_FP.setText("Fator de Potência: %.3f" % fator_potencia_medio)
            self.ui.label_tarifa.setText("Tarifa(R$): %.4f" % consumo_total_label)
            file.close()

    # ATUALIZAR COLUNAS E LINHAS
    def UpdateRecords(self):
        self.model.submitAll()
        self.atualizar_colunas_de_energia()

    # CANCELAR MUDANÇAS
    def CancelChanges(self):
        self.model.revertAll()

    # INSERIR LINHA
    def InsertRecords(self):
        self.model.insertRow(self.ui.tableView_industria.currentIndex().row())

    # DELETAR LINHA
    def DeleteRecords(self):
        self.model.removeRow(self.ui.tableView_industria.currentIndex().row())
        self.model.submitAll()

    # FILTRAR LINHA
    def Filtrar(self):

        if self.ui.radioButton.isChecked() == True:
            self.model.setFilter("Nome like '" + self.ui.prodname.text() + "%'")

        if self.ui.radioButton_2.isChecked() == True:
            self.model.setFilter("Potência_W like '" + self.ui.prodname.text() + "%'")

        if self.ui.radioButton_3.isChecked() == True:
            self.model.setFilter("Tipo like '" + self.ui.prodname.text() + "%'")

    # DELETAR TODAS AS LINHAS
    def DeleteAll(self):

        numero_de_linhas = self.model.rowCount()
        for i in range(numero_de_linhas):
            self.model.removeRow(i)

    # FUNÇÃO PARA MOSTRAR NA TABELA AS TARIFAS DO GRUPO B
    def tabela_muda_grupoA(self):

        self.ui.listWidget_classes.clear()
        conexao = MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="grupo_a")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tarifas")
        global grupo
        grupo = "A"
        for row in cursor:
            self.ui.listWidget_classes.addItem(row[0])

    # FUNÇÃO PARA MOSTRAR NA TABELA AS TARIFAS DO GRUPO B
    def tabela_muda_grupoB(self):

        self.ui.listWidget_classes.clear()
        conexao = MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="grupo_b")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tarifas")
        global grupo
        grupo = "B"

        for row in cursor:
            self.ui.listWidget_classes.addItem(row[0])

    # FUNÇAO PARA SELECIONAR A CLASSE TARIFÁRIA E MODIFICAR AS VARIÁVEIS GLOBAIS
    def seleciona_classe_tarifaria(self):

        # ATUALIZAR INFORMAÇÕES GRUPO B
        global kilowatt_hora
        global grupo_b_nome

        if (grupo == "B"):

            if (self.ui.listWidget_classes.currentItem() != True):
                grupo_b_nome = self.ui.listWidget_classes.currentItem().text()
                grupo_b_nome = str(grupo_b_nome)
                conexao = MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="grupo_b")
                cursor = conexao.cursor()
                cursor.execute(
                    "SELECT * from tarifas where tipo='%s'" % grupo_b_nome)  # Nesta etapa será procurado a tarifa selecionada no banco de dados
                row = cursor.fetchone()
                kilowatt_hora = row[1]

        # ATUALIZAR INFORMAÇÕES GRUPO A
        global grupo_a_nome
        global grupo_a_tipo
        global kilowatt_hora_a_fponta
        global kilowatt_hora_a_ponta
        global demanda_unica
        global ultrapassagem_unica
        global demanda_fponta
        global demanda_ponta
        global ultrapassagem_fponta
        global ultrapassagem_ponta

        if (grupo == "A"):

            if (self.ui.listWidget_classes.currentItem() != True):
                grupo_a_nome = self.ui.listWidget_classes.currentItem().text()
                grupo_a_nome = str(grupo_a_nome)
                conexao = MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="grupo_a")
                cursor = conexao.cursor()
                cursor.execute("SELECT * from tarifas where nome='%s'" % grupo_a_nome)
                row = cursor.fetchone()
                grupo_a_tipo = row[1]
                kilowatt_hora_a_fponta = row[2]
                kilowatt_hora_a_ponta = row[3]
                demanda_unica = row[4]
                ultrapassagem_unica = row[5]
                demanda_fponta = row[6]
                demanda_ponta = row[7]
                ultrapassagem_fponta = row[8]
                ultrapassagem_ponta = row[9]

    def atualiza_informações_gerais(self):

        global demanda_contratada_fora
        global demanda_contratada_ponta
        global dias_ativos
        global concessionaria
        global ultrapassagem_fponta_informada
        global ultrapassagem_ponta_informada
        global demanda_maxima

        if self.ui.lineEdit_Concessonaria.text() != "":
            concessionaria = str(self.ui.lineEdit_Concessonaria.text())

        if self.ui.lineEdit_ativo_mes.text() != "":
            dias_ativos = float(self.ui.lineEdit_ativo_mes.text())

        if self.ui.lineEdit_dcontratadaponta.text() != "":
            demanda_contratada_ponta = float(self.ui.lineEdit_dcontratadaponta.text())

        if self.ui.lineEdit_dcontratadafponta.text() != "":
            demanda_contratada_fora = float(self.ui.lineEdit_dcontratadafponta.text())

        if self.ui.lineEdit_ultrapassagemponta.text() != "":
            ultrapassagem_ponta_informada = float(self.ui.lineEdit_ultrapassagemponta.text())

        if self.ui.lineEdit_ultrapassagem_fponta.text() != "":
            ultrapassagem_fponta_informada = float(self.ui.lineEdit_ultrapassagem_fponta.text())

        if self.ui.lineEdit_kWh_fponta.text() != "":
            kilowatt_hora_a_fponta = float(self.ui.lineEdit_kWh_fponta.text())

        if self.ui.lineEdit_kWh_Ponta.text() != "":
            kilowatt_hora_a_ponta = float(self.ui.lineEdit_kWh_Ponta.text())

        if self.ui.lineEdit_demanda_faturavel_fora.text() != "":
            demanda_maxima = float(self.ui.lineEdit_demanda_faturavel_fora.text())
