
import MySQLdb



conn=MySQLdb.connect(host="localhost", user="root", passwd="iloverpg1", db="grupo_b")
cursor=conn.cursor()



#ATUALIZAÇÃO GRUPO B

"""
nome_banco="tarifas"
cursor.execute('create table tarifas (tipo char(50),kilowatthora float)')
conn.commit()"""




#ATUALIZAÇÃO GRUPO A

"""
nome_banco="tarifas"
cursor.execute('create table tarifas (nome char(50),tipo char(50),kilowatthora_fponta float,kilowatthora_ponta float,demanda_unica float,ultrapassagem_unica float,demanda_fponta float,demanda_ponta float,ultrapassagem_fponta float,ultrapassagem_ponta float)')
conn.commit()"""

"""
cursor.execute("
        INSERT INTO tarifas(nome,tipo,kilowatthora_fponta,kilowatthora_ponta,demanda_unica,ultrapassagem_unica,demanda_fponta,demanda_ponta,ultrapassagem_fponta,ultrapassagem_ponta)
            VALUES ("AS horo-sazonal azul","azul",0.44986,0.62984,0,0,17.07,85.43,34.15,170.87)
            ")
conn.commit()"""


price=0.64543
tipo="B1-Convencional"

cursor.execute("UPDATE tarifas set kilowatthora=%f where tipo='%s'" %(price,tipo))
conn.commit()
