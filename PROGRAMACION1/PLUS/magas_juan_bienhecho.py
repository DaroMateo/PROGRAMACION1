from os import system
import json
from PROGRAMACION1.PLUS.funciones_bienhecho import *

"""
Apellido y nombre: Magas, Juan Manuel
Division: 313-1
Fecha: 11/06/2024
Asignatura: Programacion I
Instancia: Primer Examen Parcial
"""


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

