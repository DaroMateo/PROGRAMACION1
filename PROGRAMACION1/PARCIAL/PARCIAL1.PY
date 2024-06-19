"""
Apellido y nombre Mateo Dario Ezequiel
Division: 313-1
Fecha: 11/06/2024
Asignatura: Programacion I
Instancia: Primer Examen Parcial
"""
#Menú de opciones:  
#A – Cargar el archivo data.json.  Luego de la carga del archivo (ítem A) realizar las siguientes opciones del menú:  
#B – Alta de datos con sus respectivas validaciones. [Id, Aerolínea, DNI (número), Precio, 
#Origen, Destino, Origen y Destino distintos, Clase, Fecha (numero)].  
#C – Modificar datos: Listar id y nombre de todos pasajes, luego buscarlo por id y realizar la 
#modificación del DNI, apellido y nombre o la fecha (Realizar un submenú => “ej: Ingrese id, 
#tipo y dato a modificar”).  
#D – Borrar datos: Listar id y nombre de todos los pasajes, luego buscarlo por id y realizar la 
#baja correspondiente.  
#E – Listar todos los pasajes cuyo encabezado deberá ser formateado de la siguiente manera: Fecha | Aerolínea | Clase | Origen | Destino | Precio | DNI | Apellido y nombre  

# F – Salir   

from os import system
import json
from funcionesparcial import *

bandera = False
continuar = True

while continuar:

    print("Menu de opciones:\n\nA – Cargar el archivo data.json.\nB – Alta de datos.\nC – Modificar datos.\nD – Borrar datos.\nE – Listar todos los pasajes\nF - Submenu\nG – Salir.\n")
    
    opcion = input("Ingrese una opcion: ")
    opcion = opcion.capitalize()
    
    system('cls')
    
    if opcion == "A" and bandera != True:
        pasajeros = leer_json("data.json", "pasajeros")
        print("Los datos han sido cargados exitosamente.\n")
        bandera = True
    
    elif bandera == True:
        match opcion:
            case "B":
                system('cls')
                alta_pasajero(pasajeros)
                print("El pasajero a sido dado de alta exitosamente.\n")
            
            case "C":
                system('cls')
                modificar_pasajero(pasajeros)
                print("Los datos han sido modificados exitosamente.\n")
            
            case "D":
                system('cls')
                borrar_pasajero(pasajeros)
                print("Los datos del pasajero han sido borrados exitosamente.\n")
            
            case "E":
                system('cls')
                listar_pasajeros(pasajeros)

            case "F":
                system('cls')
                submenu(pasajeros)
            
            case "G":
                continuar = False
            
            case _:
                print("Opcion invalida.\n")