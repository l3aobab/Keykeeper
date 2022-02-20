# Password Manager
A password manager made in python
#####################
Este proyecto es un gestor de contraseñas hecho en python y mysql con una interfaz de terminal.
A día de hoy, con esta herramienta se pueden consultar una o todas las contraseñas guardadas y actualizar, eliminar y añadir más contraseñas.

Los datos que se guardan en la base de datos son el sitio web o aplicación, el nombre de usuario, el correo electrónico empleado y la contraseña correspondiente. 
Las contraseñas están cifradas con base64, aunque en futuras versiones se implementará un cifrado más seguro.

Para que esta herramienta funcione correctamente, se precisa de un usuario en Mysql. Por otro lado, puedes crear una base de datos en la que guardar las contraseñas e
implementar una contraseña maestra desde dentro de la propia herramienta. Las tablas empleadas para guardar la contraseña maestra y las demás contraseñas, se crean automáticamente.