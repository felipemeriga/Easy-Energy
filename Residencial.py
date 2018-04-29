
#BILBIOTECAS NECESSÁRIAS
import sys
import MySQLdb
from PyQt4 import QtSql, QtGui
from registro_residencia import *

fix_encoding = lambda s: s.decode('utf8', 'ignore')

#VARIAVEIS GLOBAIS CHECK BOX
kw_hora=0.76683
iluminacao_publica=5.54
bandeira_verde=5


#VARIAVEIS GLOBAIS ATUALIZAR INFORMAÇÕES

concessionaria="COPEL"
dias_do_mes=25
tab=1
database = "carga_residencia"

#CONFIGURAÇÃO BILBIOTECA PYQT4 DE INTERFACE GRAFICA
from PyQt4 import QtCore, QtGui

conn=MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="carga_residencia",charset='utf8')
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

class Cria_janela_cargas(object):
    def setupUi12(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(900, 718)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Fernanda/Google Drive/Engenharia/TCC/Logo/logo_inv.bmp")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.UpdateButton = QtGui.QPushButton(Dialog)
        self.UpdateButton.setGeometry(QtCore.QRect(70, 600, 75, 23))
        self.UpdateButton.setObjectName(_fromUtf8("UpdateButton"))
        self.CancelButton = QtGui.QPushButton(Dialog)
        self.CancelButton.setGeometry(QtCore.QRect(200, 600, 75, 23))
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.InsertButton = QtGui.QPushButton(Dialog)
        self.InsertButton.setGeometry(QtCore.QRect(320, 600, 75, 23))
        self.InsertButton.setObjectName(_fromUtf8("InsertButton"))
        self.DeleteButton = QtGui.QPushButton(Dialog)
        self.DeleteButton.setGeometry(QtCore.QRect(450, 600, 75, 23))
        self.DeleteButton.setObjectName(_fromUtf8("DeleteButton"))
        self.FilterButton = QtGui.QPushButton(Dialog)
        self.FilterButton.setGeometry(QtCore.QRect(320, 240, 75, 23))
        self.FilterButton.setObjectName(_fromUtf8("FilterButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 240, 51, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.prodname = QtGui.QLineEdit(Dialog)
        self.prodname.setGeometry(QtCore.QRect(200, 240, 113, 20))
        self.prodname.setObjectName(_fromUtf8("prodname"))
        self.radioButton = QtGui.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(140, 240, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 260, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 650, 201, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 680, 161, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(190, 670, 118, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(190, 700, 118, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.DeleteButton_2 = QtGui.QPushButton(Dialog)
        self.DeleteButton_2.setGeometry(QtCore.QRect(580, 600, 75, 23))
        self.DeleteButton_2.setObjectName(_fromUtf8("DeleteButton_2"))
        self.DeleteButton_3 = QtGui.QPushButton(Dialog)
        self.DeleteButton_3.setGeometry(QtCore.QRect(710, 600, 75, 23))
        self.DeleteButton_3.setObjectName(_fromUtf8("DeleteButton_3"))
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(140, 290, 601, 291))
        self.tableView.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(-30, -10, 1091, 731))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Fernanda/Google Drive/Engenharia/TCC/Logo/Energia01.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.groupBox_5 = QtGui.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(70, 60, 321, 171))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(60, 20, 111, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 20, 131, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_10 = QtGui.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(60, 50, 111, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 50, 131, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.FilterButton_2 = QtGui.QPushButton(self.groupBox_5)
        self.FilterButton_2.setGeometry(QtCore.QRect(150, 130, 75, 23))
        self.FilterButton_2.setObjectName(_fromUtf8("FilterButton_2"))
        self.label_13 = QtGui.QLabel(self.groupBox_5)
        self.label_13.setGeometry(QtCore.QRect(0, 80, 161, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 80, 131, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(530, 650, 201, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(640, 670, 118, 3))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(530, 680, 201, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(640, 700, 118, 3))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(230, 10, 441, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Kozuka Gothic Pr6N B"))
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(620, 60, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.listWidget_tarifa = QtGui.QListWidget(Dialog)
        self.listWidget_tarifa.setGeometry(QtCore.QRect(600, 80, 201, 91))
        self.listWidget_tarifa.setObjectName(_fromUtf8("listWidget_tarifa"))
        self.pushButton_selecionar = QtGui.QPushButton(Dialog)
        self.pushButton_selecionar.setGeometry(QtCore.QRect(670, 190, 75, 23))
        self.pushButton_selecionar.setObjectName(_fromUtf8("pushButton_selecionar"))
        self.groupBox_bandeira = QtGui.QGroupBox(Dialog)
        self.groupBox_bandeira.setGeometry(QtCore.QRect(420, 60, 161, 121))
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
        self.label_2.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.DeleteButton_2.raise_()
        self.DeleteButton_3.raise_()
        self.tableView.raise_()
        self.groupBox_5.raise_()
        self.label_7.raise_()
        self.line_3.raise_()
        self.label_8.raise_()
        self.line_4.raise_()
        self.label_4.raise_()
        self.label_9.raise_()
        self.listWidget_tarifa.raise_()
        self.pushButton_selecionar.raise_()
        self.groupBox_bandeira.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Easy Energy", None))
        self.UpdateButton.setText(_translate("Dialog", "Atualizar", None))
        self.CancelButton.setText(_translate("Dialog", "Cancelar", None))
        self.InsertButton.setText(_translate("Dialog", "Adicionar", None))
        self.DeleteButton.setText(_translate("Dialog", "Deletar", None))
        self.FilterButton.setText(_translate("Dialog", "Filtrar", None))
        self.label.setText(_translate("Dialog", "Filtrar por:", None))
        self.radioButton.setText(_translate("Dialog", "Nome", None))
        self.radioButton_2.setText(_translate("Dialog", "Potência", None))
        self.label_2.setText(_translate("Dialog", "Potência Total Instalada:", None))
        self.label_3.setText(_translate("Dialog", " Número de Cargas:", None))
        self.DeleteButton_2.setText(_translate("Dialog", "Deletar Tudo", None))
        self.DeleteButton_3.setText(_translate("Dialog", "Registrar", None))
        self.groupBox_5.setTitle(_translate("Dialog", "Atualizar Dados", None))
        self.label_6.setText(_translate("Dialog", "  Concessionária:", None))
        self.label_10.setText(_translate("Dialog", "       kWh(Preço):", None))
        self.FilterButton_2.setText(_translate("Dialog", "Atualizar", None))
        self.label_13.setText(_translate("Dialog", "            Periodo Ativo do mês:", None))
        self.label_7.setText(_translate("Dialog", "  Consumo Total(kWh):", None))
        self.label_8.setText(_translate("Dialog", "                 Fatura(R$):", None))
        self.label_4.setText(_translate("Dialog", "Diagnóstico Consumo Residencial/Comercial", None))
        self.label_9.setText(_translate("Dialog", "Selecionar tipo de tarifa:", None))
        self.pushButton_selecionar.setText(_translate("Dialog", "Selecionar", None))
        self.groupBox_bandeira.setTitle(_translate("Dialog", "Bandeira Tarifária", None))
        self.radioButton_verde.setText(_translate("Dialog", "Verde", None))
        self.radioButton_amarelo.setText(_translate("Dialog", "Amarela", None))
        self.radioButton_vermelho.setText(_translate("Dialog", "Vermelha", None))



#CRIAR CONEXAO BANCO DE DADOS
def createConnection():
    db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName('localhost')
    db.setDatabaseName("%s"%database)
    db.setUserName('root')
    db.setPassword('iloverpg1')
    db.open()
    print(db.lastError().text())
    return True


#CLASSE PARA INICIAR A INTERFACE GRAFICA E TODA SUA FUNCIONALIDADE
class MyForm(QtGui.QDialog):
    #DEFINIÇÕES
    def __init__(self,tabela):
        QtGui.QWidget.__init__(self)
        self.ui = Cria_janela_cargas()
        self.ui.setupUi12(self)
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("%s"%tabela)
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()
        QtGui.QWidget.setWindowTitle(self, "Easy Energy - Residencial/Comercial - %s"%(tabela))
        self.ui.tableView.setModel(self.model)
        self.lista_classes_tarifarias()


        #TRIGGERS
        QtCore.QObject.connect(self.ui.UpdateButton, QtCore.SIGNAL('clicked()'), self.UpdateRecords)
        QtCore.QObject.connect(self.ui.CancelButton, QtCore.SIGNAL('clicked()'), self.CancelChanges)
        QtCore.QObject.connect(self.ui.InsertButton, QtCore.SIGNAL('clicked()'), self.InsertRecords)
        QtCore.QObject.connect(self.ui.DeleteButton, QtCore.SIGNAL('clicked()'), self.DeleteRecords)
        QtCore.QObject.connect(self.ui.FilterButton, QtCore.SIGNAL('clicked()'), self.Filtrar)
        QtCore.QObject.connect(self.ui.DeleteButton_3, QtCore.SIGNAL('clicked()'),self.novo_item)
        QtCore.QObject.connect(self.ui.DeleteButton_2, QtCore.SIGNAL('clicked()'),self.DeleteAll)
        QtCore.QObject.connect(self.ui.pushButton_selecionar, QtCore.SIGNAL('clicked()'),self.configura_globais_tarifação)
        QtCore.QObject.connect(self.ui.FilterButton_2, QtCore.SIGNAL('clicked()'),self.atualizar_informações_consultoria)

        #ATALHOS


        global tab
        tab = tabela

        self.ui.radioButton.setChecked(1)

    def novo_item(self):

        self.registra_janela = Form1(tab)
        QtCore.QObject.connect(self.registra_janela, QtCore.SIGNAL('finished(int)'),self.show)
        QtCore.QObject.connect(self.registra_janela, QtCore.SIGNAL('finished(int)'),self.UpdateRecords)
        QtCore.QObject.connect(self.registra_janela, QtCore.SIGNAL('finished(int)'),self.model.submitAll)
        self.registra_janela.show()
        self.hide()

    def atualizar_colunas_de_energia(self):

        cursor=conn.cursor()
        b=self.model.rowCount()
        self.ui.label_3.setText(" Número de Cargas: %s"%b)
        pototal=0
        energtotal=0
        consumo=0
        consumo_total=0



        for i in range(b):
            self.record=self.model.record(i)
            if self.record.value("Potência_Watts")==None:
                pot=0
            else:
                pot = float(self.record.value("Potência_Watts"))

            if self.record.value("Horas")==None:
                horas=0
            else:
                horas = float(self.record.value("Horas"))

            nome=str(self.record.value("Nome"))

            qnt=int(self.record.value("Quantidade"))


            pototal=pototal+pot*qnt

            energ=qnt*pot*horas

            energ=energ/1000
            energtotal=energtotal+energ

            consumo=energ*kw_hora

            consumo_total=consumo_total+consumo



            cursor.execute("SELECT * from %s where Nome='%s'" %(tab,nome))
            cursor.execute("UPDATE %s set Energia_kWh=%.3f where Nome='%s'" %(tab,energ,nome))
            conn.commit()
        energtotal=energtotal*dias_do_mes
        consumo_total=consumo_total*dias_do_mes

        if consumo_total==0:
            consumo_total=0
        if energtotal==0:
            energtotal=0

        if pototal==0:
            pototal=0
        else:
            pototal=pototal/1000

        #PARTE REFERENTE AS BANDEIRAS TARIFARIAS
        if(self.ui.radioButton_amarelo.isChecked()):
            consumo_total=consumo_total+energtotal*0.015

        if(self.ui.radioButton_vermelho.isChecked()):
            consumo_total=consumo_total+energtotal*0.030

        self.ui.label_2.setText("Potência Total Instalada: %.3f kW"%pototal)
        self.ui.label_7.setText("  Consumo Total(kWh):%.3f kWh"%energtotal)
        self.ui.label_8.setText("                 Fatura(R$): %.2f"%consumo_total)



    def atualizar_informações_consultoria(self):

        global dias_do_mes
        global kw_hora
        global concessionaria


        if self.ui.lineEdit_2.text()!="":
            concessionaria=self.ui.lineEdit_2.text()
        if self.ui.lineEdit_6.text()!="":
            dias_do_mes=self.ui.lineEdit_6.text()
            dias_do_mes=int(dias_do_mes)
        if self.ui.lineEdit_3.text()!="":
            kw_hora=self.ui.lineEdit_3.text()
            kw_hora=float(kw_hora)


    def UpdateRecords(self):
        self.model.submitAll()
        self.atualizar_colunas_de_energia()



    def CancelChanges(self):
        self.model.revertAll()

    def InsertRecords(self):
        self.model.insertRow(self.ui.tableView.currentIndex().row())


    def DeleteRecords(self):
        self.model.removeRow(self.ui.tableView.currentIndex().row())
        self.model.submitAll()

    def Filtrar(self):

        if self.ui.radioButton.isChecked()==True:

            self.model.setFilter("Nome like '"+self.ui.prodname.text()+"%'")
        else:

            self.model.setFilter("Potência_Watts like '"+self.ui.prodname.text()+"%'")

    def DeleteAll(self):

        numero_de_linhas=self.model.rowCount()
        for i in range(numero_de_linhas):
            self.model.removeRow(i)

    def configura_globais_tarifação(self):

        #REDEFINIR VARIAVEIS GLOBAIS
        global kw_hora


        if(self.ui.listWidget_tarifa.currentItem()!=True):

            grupo_b_nome=self.ui.listWidget_tarifa.currentItem().text()
            grupo_b_nome=str(grupo_b_nome)
            conexao=MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="grupo_b")
            cursor=conexao.cursor()
            cursor.execute("SELECT * from tarifas where tipo='%s'" %grupo_b_nome)#Nesta etapa será procurado a tarifa selecionada no banco de dados
            row=cursor.fetchone()
            kw_hora=row[1]



        """if self.ui.radioButton_5.isChecked()==True:
            kw_hora=0.76683
        if self.ui.radioButton_6.isChecked()==True:
            kw_hora=0.45464
        if self.ui.radioButton_12.isChecked()==True:
            kw_hora=0.76683
        if self.ui.radioButton_13.isChecked()==True:
            kw_hora=0.50612
        if self.ui.radioButton_14.isChecked()==True:
            kw_hora=0.76683"""


    def lista_classes_tarifarias(self):

        conexao=MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="grupo_b")
        cursor=conexao.cursor()
        cursor.execute("SELECT * FROM tarifas")
        global grupo
        grupo="B"

        for row in cursor:
            self.ui.listWidget_tarifa.addItem(row[0])

