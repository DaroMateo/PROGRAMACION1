from os import system
import json
from fun import *

"""Desarrollar en Python: 
 De una empresa de viajes se tienen los siguientes datos:

 Id (debe comenzar en 1 y ser autoincremental) 
 Aerolínea (AA, LATAM o IBERIA) 
 Apellido_Nombre_Pasajero (Hasta de 30 caracteres) 
 DNI_Pasajero 
 Precio (Entre 500.000 y 2.000.000) 
 Origen (Buenos Aires, Madrid, París, Miami, Roma o Tokio) 
 Destino (Buenos Aires, Madrid, París, Miami, Roma o Tokio) 
 Clase (Turista o Ejecutivo) 
 Fecha (formato AAAAMMDD)  

Menú de opciones:  
A – Cargar el archivo data.json.  Luego de la carga del archivo (ítem A) realizar las siguientes opciones del menú:  
B – Alta de datos con sus respectivas validaciones. [Id, Aerolínea, DNI (número), Precio, 
Origen, Destino, Origen y Destino distintos, Clase, Fecha (numero)].  
C – Modificar datos: Listar id y nombre de todos pasajes, luego buscarlo por id y realizar la 
modificación del DNI, apellido y nombre o la fecha (Realizar un submenú => “ej: Ingrese id, 
tipo y dato a modificar”).  
D – Borrar datos: Listar id y nombre de todos los pasajes, luego buscarlo por id y realizar la 
baja correspondiente. 
E – Listar todos los pasajes cuyo encabezado deberá ser formateado de la siguiente manera: Fecha | Aerolínea | Clase | Origen | Destino | Precio | DNI | Apellido y nombre
F – Salir   

NOTAS: 
Nota 0: No se podrá acceder a ningún ítem del menú, sin antes haber cargado el archivo. En tal sentido, realizar la 
validación correspondiente. 
Nota 1:  Los  puntos  deben  ser  accedidos  mediante  un  menú.  Para  todas  las  opciones,  validar  lo  ingresado  por 
consola. Cada ítem del menú deberá ser una función. 
Nota 2: Se deberá desarrollar biblioteca y funciones propias. 
Nota 3: El set de datos proviene de un json. 
Nota 4: Utilizar las funciones propias desarrolladas durante la cursada en lugar de los métodos o funciones propias 
del lenguaje. """


bandera = False
continuar = True

while continuar:

    print("A – Cargar el archivo data.json.\nB – Alta de datos.\nC – Modificar datos.\nD – Borrar datos.\nE – Listar todos los pasajes\nF – Salir.")
    opcion = input("Ingrese una opcion: ")
    opcion = opcion.capitalize()
    system('cls')
    if opcion == "A" and bandera != True:
        pasajeros = leer_json("Simulacro\data.json", "pasajeros")
        bandera = True
    
    elif bandera == True:
        match opcion:
            case "B":
                alta_pasajero(pasajeros)
                print("El pasajero a sido dado de alta exitosamente.")
                print(pasajeros)
            case "C":
                modificar_pasajero(pasajeros)
                print("Los datos han sido modificados exitosamente.")
            case "D":
                borrar_pasajero(pasajeros)
                print("Los datos del pasajero han sido borrados exitosamente.")
            case "E":
                listar_pasajeros(pasajeros)
            case "F":
                continuar = False
            case _:
                print("Opcion invalida.")
