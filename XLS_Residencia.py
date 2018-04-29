

import xlrd
import MySQLdb

from PyQt4 import QtCore, QtGui

nome_criado=""


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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(383, 417)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo\logo_inv.bmp")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-30, -10, 471, 631))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Kozuka Gothic Pr6N R"))
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users\Fernanda\Google Drive\Engenharia\TCC\Logo/Energia01.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 80, 171, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 80, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 80, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 140, 171, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(60, 160, 256, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 360, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(130, 110, 161, 16))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(140, 390, 101, 16))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Easy Energy ", None))
        self.label_2.setText(_translate("Form", "Importar Arquivo XLS", None))
        self.label_3.setText(_translate("Form", "Criar a Partir de novo arquivo:", None))
        self.pushButton_2.setText(_translate("Form", "Criar", None))
        self.label_4.setText(_translate("Form", "Inserir em Arquivo Existente:", None))
        self.pushButton_3.setText(_translate("Form", "Selecionar", None))

class FormXLS(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL("clicked()"),self.criar_nova_tabela)
        QtCore.QObject.connect(self.ui.pushButton_3,QtCore.SIGNAL("clicked()"),self.carregar_tabela_existente)

        global setar
        setar=1
        connection = MySQLdb.connect(
                host = 'localhost',
                user = 'root',
                passwd = 'iloverpg1')  # create the connection
        cursor = connection.cursor()     # get the cursor


        cursor.execute("USE carga_residencia") # select the database

        cursor.execute("SHOW TABLES")    # execute 'SHOW TABLES' (but data is not returned)

        tables = cursor.fetchall()

        for (table_name,) in cursor:
            self.ui.listWidget.addItem(table_name)


    def criar_nova_tabela(self):

        global nome_criado
        conn = MySQLdb.connect(host="localhost", user = "root", passwd = "iloverpg1", db = "carga_residencia")
        cursor = conn.cursor()
        nome_criado = str(self.ui.lineEdit_2.text())

        if nome_criado=="":
            self.ui.label_5.setText("Não Foi inserido nenhum nome")
        else:
            try:
                cursor.execute('create table %s (Local char(50),Nome char(50),Potência_Watts varchar(50),Quantidade smallint,Horas varchar(50),Energia_kWh varchar(50))'%nome_criado)
                conn.commit()
                self.ui.label_5.clear()
                self.ui.label_5.setText("Criado com sucesso!")
                self.converter_XLS_MYSQL()

            except:
                self.ui.label_3.setText("Este nome já esta em uso")

    def carregar_tabela_existente(self):

        global nome_criado

        if(nome_criado==""):
            nome_criado=self.ui.listWidget.currentItem().text()
            nome_criado=str(nome_criado)
        self.converter_XLS_MYSQL()


    def converter_XLS_MYSQL(self):


        name=QtGui.QFileDialog.getOpenFileName()
        name=str(name)
        book = xlrd.open_workbook("%s"%name)
        sheet = book.sheet_by_name("Sheet1")


        conn = MySQLdb.connect(host="localhost", user = "root", passwd = "iloverpg1", db = "carga_residencia")
        cursor = conn.cursor()

        if nome_criado!="":
            # Create the INSERT INTO sql query
            # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
            for r in range(1, sheet.nrows):
                local = sheet.cell(r,0).value
                nome_carga = sheet.cell(r,1).value
                pot = sheet.cell(r,2).value
                qnt = sheet.cell(r,3).value
                horas = sheet.cell(r,4).value
                # Assign values from each row
                values = (local,nome_carga,pot,qnt,horas)
                # Execute sql Query
                cursor.execute("INSERT INTO %s (Local, Nome, Potência_Watts, Quantidade, Horas) VALUES ('%s','%s',%s,%s,%s)"%(nome_criado,local,nome_carga,pot,qnt,horas))

        self.ui.label_6.setText("Concluido!")
        cursor.close()
        conn.commit()
        conn.close()





