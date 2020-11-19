import random 
import os
import sqlite3
connection = sqlite3.connect("prueba.db")

cursor = connection.cursor()
array=[]
archivo = open('nombres.txt', 'r')
nombres = archivo.readlines()

nombre=[]
for name in nombres:
    nombre.append( "".join(name.split("\n")))

archivo = open('apellidos.txt', 'r')
apellidos = archivo.readlines()
#https://github.com/olea/lemarios/blob/master/apellidos-es.txt
apellido=[]
for lastname in apellidos:
    apellido.append( "".join(lastname.split("\n")))


dni = []
for _ in range(30):
    dni.append(random.randint(300000000, 400000000))


lista=[[l, n, a, d] for l, (n, a, d) in enumerate(zip(nombre, apellido, dni))]

#print (lista)

#from pathlib import Path
#def list_from_filename(filename):
 #   return [l.strip() for l in Path(filename).read_text().split(",")]

#liste = [[l, n, a] for l, (n, a) in enumerate(zip(list_from_filename("nombres.txt"), list_from_filename("apellidos.txt")))]
#print(liste)


sql_command = """
CREATE TABLE employee ( 
id INTEGER PRIMARY KEY,
nombre VARCHAR(20),
apellido VARCHAR(20),
dni INTEGER 
);"""

cursor.execute(sql_command)

#sql_command = """INSERT INTO employee (id, nombre, apellido, dni, telefono, ciudad)
#    VALUES (0, "William", "Shekeaspere", 34907555, 4948432, Codoba);"""
#cursor.executemany('INSERT INTO employee VALUES(?,?,?,?,?,?);', lista);

cursor.executemany('INSERT INTO employee VALUES(?,?,?,?);', lista);

connection.commit()

connection.close()
