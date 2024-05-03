#Crear un Base de datos "databaseexample.bd"

#Crear un tabla "productos" con los siguientes 3 campos:    
# 1.- id: Identificador del producto tipo numerico
# 2.- nombre: Nombre del producto tipo texto 
# 3.- precio: Precio del producto tipo numerico

#Inserta 3 productos en la tabla "productos"
# 1.- Impresora, 300
# 2.- Raton, 250 
# 3.- Ordenador, 600

#Consultar los productos de la tabla "productos"
#Cerrar la base de datos "databaseexample.bd"

import sqlite3
import sqlite3
#Crear un Base de datos "databaseexample.bd"
conexion = sqlite3.connect('databaseexample.db')
cursor = conexion.cursor()

##Crear un tabla "productos"
cursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER, NOMBRE TEXT, PRECIO INTEGER)")
#Guardar cambios
conexion.commit()

#Inserta 3 productos en la tabla "productos"
lista_productos = [ ('1', 'Impresora', 300),('2','Raton', 250),('3','Ordenador', 600) ]
cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", lista_productos)
#Guardar cambios
conexion.commit()

#Consultar los productos de la tabla "productos"
cursor.execute("SELECT * FROM PRODUCTOS")
productos = cursor.fetchall()
for producto in productos:
    print(producto) 
 

#Guardar cambios
conexion.commit()
#Cerrar las base de datos
conexion.close()

