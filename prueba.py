import os
import sqlite3
connection = sqlite3.connect("prueba.db")

cursor = connection.cursor()

archivo = open('nombres.txt', 'r')
for linea in archivo:
    l=linea.split(", ")

archivo = open('apellidos.txt', 'r')
for linea in archivo:
    l2=linea.split(", ")

nombres=[]
for n in l: 
    if n == "\n":
        break
    nombres.append(n)

apellidos=[]
for a in l2: 
    if a == "\n":
        break
    apellidos.append(a)

lista=[[l, n, a] for l, (n, a) in enumerate(zip(nombres, apellidos))]



#from pathlib import Path
#def list_from_filename(filename):
 #   return [l.strip() for l in Path(filename).read_text().split(",")]

#liste = [[l, n, a] for l, (n, a) in enumerate(zip(list_from_filename("nombres.txt"), list_from_filename("apellidos.txt")))]
#print(liste)


sql_command = """
CREATE TABLE employee ( 
id INTEGER PRIMARY KEY,
nombre VARCHAR(20),
apellido VARCHAR(20)
);"""

cursor.execute(sql_command)

#sql_command = """INSERT INTO employee (id, nombre, apellido, dni, telefono, ciudad)
#    VALUES (0, "William", "Shekeaspere", 34907555, 4948432, Codoba);"""
#cursor.executemany('INSERT INTO employee VALUES(?,?,?,?,?,?);', lista);

cursor.executemany('INSERT INTO employee VALUES(?,?,?);', lista);

connection.commit()

connection.close()
