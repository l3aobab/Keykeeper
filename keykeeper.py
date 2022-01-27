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

#elegir una accion en el menu
def showOpcion():
	op=None
	try:
		op=int(input("Selecciona una opcion: "))
	except ValueError:
		print('Error, debes seleccionar un numero del 1 al 6 para seleccionar una opcion')
	return op

if ddbb:

	#se crean las tablas master y gestor si no existen
	createMP="CREATE TABLE IF NOT EXISTS master (master varchar(255))"
	dbcursor.execute(createMP)

	createT="CREATE TABLE IF NOT EXISTS gestor (user_id int PRIMARY KEY AUTO_INCREMENT,sitio varchar(50) NOT NULL,usuario varchar(50),contraseña varchar(255) NOT NULL,email varchar(100))"
	dbcursor.execute(createT)
	
	#mostrar todas las contraseñas
	def showAll():
		showGestor="SELECT * FROM gestor"
		dbcursor.execute(showGestor)
		showGestorResultado=dbcursor.fetchall()
		return showGestorResultado

	#mostrar una linea en concreto
	def showOne():
		app=input("Indica una aplicación: ")
		usr=input("Indica el nombre de usuario: ")
		showGestorOne=("SELECT * FROM gestor WHERE sitio=%s and usuario=%s")
		dbcursor.execute(showGestorOne,(app, usr, ))
		sgor=dbcursor.fetchall()
		return sgor

	#actualizar una contraseña
	def updateOne():
		app=input("Indica una aplicación: ")
		usr=input("Indica el nombre de usuario: ")
		psw=getpass.getpass("Introduce la nueva contraseña: ")
		psw2=getpass.getpass("Confirma la nueva contraseña: ")
		if psw==psw2:
			showUpdate="UPDATE gestor SET contraseña=%s WHERE sitio=%s and usuario=%s"
			dbcursor.execute(showUpdate,(psw, app, usr, ))
			sur=dbcursor.fetchall()
			ddbb.commit()
			return sur

	#borrar todos los datos de un determinado sitio
	def deletePass():
		app=input("Indica una aplicación: ")
		usr=input("Indica el nombre de usuario: ")
		doDelete="DELETE FROM gestor WHERE sitio=%s and usuario=%s"
		dbcursor.execute(doDelete,(app, usr, ))
		doDeleteRes=dbcursor.fetchall()
		ddbb.commit()
		return doDeleteRes

	#añadir una nueva contraseña
	def addOne():
		app=input("Indica una aplicación: ")
		usr=input("Indica el nombre de usuario: ")
		psw=getpass.getpass("Introduce la nueva contraseña: ")
		psw2=getpass.getpass("Confirma la nueva contraseña: ")
		eml=input("Indica el correo electronico: ")
		if psw==psw2:
			insertT="INSERT INTO gestor (sitio,usuario,contraseña,email) VALUES (%s,%s,%s,%s)"
			dbcursor.execute(insertT,(app, usr, psw, eml, ))
			addOneRes=dbcursor.fetchall()
			ddbb.commit()
			return addOneRes

	salir=False
	opcion=0

	while not salir:
		print("""
----------------------------------------------------------------------------------------

Bienvendio """+ name +""" a tu gestor de contraseñas.
Para continuar, por favor, selecciona una de las siguientes opciones:

1)Mostrar todas las contraseñas
2)Mostrar una contraseña en concreto
3)Actualizar una contraseña
4)Eliminar una contraseña
5)Añadir una nueva contraseña
6)Salir

----------------------------------------------------------------------------------------
			""")

		opcion=showOpcion()

		if opcion==1:
			clearConsole()
			selectAll=showAll()
			for fila in selectAll:
				print(fila)
			pass
		elif opcion==2:
			clearConsole()
			selectOne=showOne()
			for fila in selectOne:
				print(fila)
		elif opcion==3:
			clearConsole()
			updateOne()
			clearConsole()
			selectAll=showAll()
			for fila in selectAll:
				print(fila)
			pass
		elif opcion==4:
			clearConsole()
			deletePass()
			clearConsole()
			selectAll=showAll()
			for fila in selectAll:
				print(fila)
			pass
		elif opcion==5:
			clearConsole()
			addOne()
			clearConsole()
			selectAll=showAll()
			for fila in selectAll:
				print(fila)
			pass
		elif opcion==6:
			clearConsole()
			salir=True
