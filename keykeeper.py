import mysql.connector
import os
from prettytable import PrettyTable
import getpass

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()

print()
print("Bienvenido a Key Keeper, tu gestor de contraseñas")
print("Para continuar, introce los siguientes datos:")
name=input("Nombre de usuario: ")
pswd=getpass.getpass("Contraseña: ")

ddbb=mysql.connector.connect(host="localhost",user=name,passwd=pswd,database="passwd")
dbcursor=ddbb.cursor()
clearConsole()

if ddbb:

	#se crean las tablas master y gestor si no existen
	createMP="CREATE TABLE IF NOT EXISTS master (master varchar(255))"
	dbcursor.execute(createMP)

	createT="CREATE TABLE IF NOT EXISTS gestor (user_id int PRIMARY KEY AUTO_INCREMENT,sitio varchar(50) NOT NULL,usuario varchar(50),contraseña varchar(255) NOT NULL,email varchar(100))"
	dbcursor.execute(createT)
	#insertT="INSERT INTO gestor (sitio,usuario,contraseña,email) VALUES ('instagram','l3aobab','abc.123','correofalso2@gmail.com')"
	#dbcursor.execute(insertT)
	#ddbb.commit()
	
	#funcion para mostrar todas las contraseñas
	def showAll():
		showGestor="SELECT * FROM gestor"
		dbcursor.execute(showGestor)
		showGestorResultado=dbcursor.fetchall()
		return showGestorResultado

	#Hay que poner esto dentro del menu, opcion 1
	selectAll=showAll()
	for fila in selectAll:
		print(fila)

	#funcion para mostrar una linea en concreto
	def showOne():
		app=input("Indica una aplicación: ")
		usr=input("Indica el nombre de usuario: ")
		showGestorOne=("SELECT * FROM gestor WHERE sitio=%s and usuario=%s")
		dbcursor.execute(showGestorOne,(app, usr, ))
		sgor=dbcursor.fetchall()
		return sgor

	#Hay que poner esto dentro del menu, opcion 2
	selectOne=showOne()
	for fila in selectOne:
		print(fila)

	#completar esto mañana
	def updateOne():
		app=input("Indica una aplicación: ")
		usr=input("Indica el nombre de usuario: ")
		psw=input("Introduce la nueva contraseña: ")
		psw2=input("Confirma la nueva contraseña: ")
		if psw==psw2:
