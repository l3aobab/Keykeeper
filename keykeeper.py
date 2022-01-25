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
	#insertT="INSERT INTO gestor (sitio,usuario,contraseña,email) VALUES ('twitter','l3aobab','abc123.','correofalso@gmail.com')"
	#dbcursor.execute(insertT)
	#ddbb.commit()
	
	#consulta de prueba
	showGestor="SELECT * FROM gestor"
	dbcursor.execute(showGestor)
	showGestorResultado=dbcursor.fetchall()
	for fila in showGestorResultado:
		print(fila)