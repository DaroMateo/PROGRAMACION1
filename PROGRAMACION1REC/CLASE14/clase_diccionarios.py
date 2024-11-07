def validar_existencia_alumno(lista_alumno:list[dict],clave:str)->bool:
    retorno=False
    # if len(lista_alumno)>0:
    #     retorno=True
    for alumno in lista_alumno:
        if alumno[clave] == True:
            retorno = True
            break
    return retorno


def cargar_diccionario(lista_claves:list, mensaje:str,estado:str)-> dict:
    diccionario_alumno = {}

    for clave in lista_claves:
        if clave == estado:
            diccionario_alumno.update({clave:True})
        else:
            valor = input(mensaje.format(clave))
            diccionario_alumno.update({clave:valor})
    return diccionario_alumno



# 2) Desarrolle una función que muestre una lista de alumnos y sus respectivos datos en filas y columnas,
# donde cada fila representa un alumno y cada columna representa uno de sus datos.

def mostrar_alumno(diccionario_alumno: dict) -> None:

    for clave in diccionario_alumno:
        if clave != "activo":
            print(f"{diccionario_alumno[clave]:^10}", end= "")
        
    print("")

def mostrar_encabezado(diccionario: dict):
    for clave in diccionario:                          #De este modo solo recorre CLAVES, recordar relación entre Clave y Valor (similar a Listas pero con Claves, no Ind).
        if clave != "activo":
            print(f"{clave.upper():^10}", end= "")

    cantidad_guiones = (len(diccionario.keys())-1) * 10
    separador = "\n" + ("-"*cantidad_guiones)
    print(separador)
    #print("\n---------------------------------------------")

def mostrar_lista_alumnos(lista_de_alumnos: list, clave) -> None:
    
    if len(lista_de_alumnos) > 0:
        
        mostrar_encabezado(lista_de_alumnos[0])
        for alumno in lista_de_alumnos:
            if alumno[clave] == True:
                mostrar_alumno(alumno)
    else:
        print("La lista está vacía.")


""" 3 - Modificación: Desarrolle una función que permita calcular el promedio de calificaciones a partir de
una lista de alumnos. Recibe una lista de diccionarios por parámetro, calcula el promedio y lo agrega
como un ítem más al diccionario."""

#ABM/CRUD

def calcular_promedio (lista_de_alumnos:list[dict], clave_parametro :str, ident:str) -> bool: # CADA ELEMENTO DE LA LISTA VA A SER UN DICCIONARIO
    retorno = False

    for alumno in lista_de_alumnos: 
       
        acumulador = 0
        contador = 0
       
        for clave in alumno.keys():
            if clave[0:4] == ident:
                acumulador += int(alumno[clave])
                contador += 1

        #promedio = (int(alumno["nota_pp"]) + int(alumno["nota_sp"])) / 2
        promedio = acumulador / contador
        alumno.update({clave_parametro:promedio})
        retorno = True

    return retorno

# 4) Desarrolle una función que informe por cada alumno de la lista su estado académico (promedio de 1 al
# 4: desaprobado, 4 o 5: aprobado, y 6 o más: promocionado).

def mostrar_estado_aprobacion(lista_alumno:list[dict], ident:str, diccionario_estados:dict, msj:str, nombre:str, msj2:str)->None:
    for alumno in lista_alumno:
        if ident in alumno.keys(): 
            promedio_alumno=alumno[ident]
            for clave in diccionario_estados.keys():
                desde=diccionario_estados[clave][0]
                hasta=diccionario_estados[clave][-1]
                if promedio_alumno >= desde and promedio_alumno < hasta:
                    print(msj.format(alumno[nombre],clave))
        else:
            print (msj2.format(alumno[nombre]))
            """ if promedio_alumno < 4:
                print(f"El alumno {alumno['nombre']} esta desaprobado.")
            elif promedio_alumno < 6 :
                print(f"El alumno {alumno['nombre']} esta aprobado.")
            else:
                print(f"El alumno {alumno['nombre']} esta promocionado.")
         """
# 5) Desarrolle una función que informe las notas y el promedio del alumno cuyo nombre recibe por
# parámetro, en caso de no encontrarlo deberá imprimir un mensaje de error.

def buscar_alumno(lista_alumnos:list[dict], nombre_alumno:str)->dict:
    retorno = None
    for alumno in lista_alumnos:
        if nombre_alumno in alumno.values(): #if alumno["nombre"] == nombre:
            retorno = alumno
            break
    return retorno
    

# 6) Baja Física: Desarrolle una función que pueda eliminar a un alumno de la lista de alumnos. El alumno
# a eliminar deberá seleccionarlo el usuario por terminal, validar que exista antes de eliminarlo, y en
# caso de que no exista mostrar un mensaje de error.

def borrar_alumno (lista:list[dict], alumno:dict):
    lista.remove(alumno)

# 7) Baja Lógica: Desarrolle una función que pueda dar de baja lógicamente a un alumno de la lista.
# Deberá recibir por parámetro el nombre del alumno a eliminar y agregarle un estado (bool) activo o
# inactivo. Modificar la función que muestra los alumnos haciendo que ignore a todos los alumnos
# inactivos.
def borrar_alumno_logico(alumno:dict, clave:str, valor:any):
    alumno[clave] = valor

# 8) Desarrolle una función que busque al alumno con el mejor o con el peor promedio. Informar sus
# nombres y sus respectivos promedios.
def buscar_min_max_promedio (lista_alumnos:list[dict],criterio:str, clave:str)->dict:
    max_min = None
    for alumno in lista_alumnos:
        if criterio == "max" and (max_min is None or max_min[clave] < alumno[clave]) or criterio == "min" and (max_min is None or max_min[clave] > alumno[clave]):
                max_min = alumno

    return max_min

def validar_criterio(msj:str, criterio_validado:str)->str:
    criterio = ""
    while criterio not in criterio_validado:
        criterio = input(msj)
        criterio = criterio.lower()
    return criterio




# 9) Desarrolle una función que ordene a los alumnos por promedio ASC/DESC.

def definir_orden(diccionario:dict):
    return diccionario["promedio"]

def ordenar_alumnos(lista_alumno:list[dict],orden:str)->list[dict]:
    if orden == "asc":
        lista_alumno.sort(key=definir_orden)
    elif orden == "desc":
        lista_alumno.sort(key=definir_orden, reverse=True)
    
# 10) Desarrolle una función que calcule e informe la cantidad de alumnos según su estado académico
# (desaprobado, aprobado o promocionado).
def cantidad_alumnos_por_estado(lista_alumnos: list[dict], diccionario_estados: dict, ident: str) -> None:
    estados = {"desaprobado": 0, "aprobado": 0, "promocionado": 0}

    for alumno in lista_alumnos:
        if ident in alumno:
            promedio = alumno[ident]
            for estado, rango in diccionario_estados.items():
                desde, hasta = rango
                if desde <= promedio < hasta:
                    estados[estado] += 1
    
    print("Cantidad de alumnos por estado académico:")
    for estado, cantidad in estados.items():
        print(f"{estado.capitalize()}: {cantidad}")


menu= """
1 (ALTA)
2 (MOSTRAR ALUMNOS)
3 (CALCULAR PROMEDIOS)
4 (ESTADO ACADEMICO)
5 (BUSCAR ALUMNO)
6 (BORRAR ALUMNO)
7 (BAJA LOGICA)
8 (BUSCAR MEJOR O PEOR PROMEDIO)
9 (ORDENAR POR PROMEDIO)
10 (CANTIDAD DE ALUMNOS POR ESTADO ACADEMICO)
0 (SALIR)
"""
def menu_dicc(mensaje_menu:str):

    lista_claves = ["nombre", "nota_pp", "nota_sp", "activo"]
    mensaje_input =  "Ingrese {} del alumno: "
    lista_alumnos = []
    diccionario={"desaprobado":[1,4],
             "aprobado": [4,6],
             "promocionado":[6,11]
    }
    while True:


        print(mensaje_menu)
        opcion_elegida = input("Ingrese Opcion: ")


        match opcion_elegida:

            case "1":
                alumno = cargar_diccionario(lista_claves,mensaje_input,"activo")
                lista_alumnos.append(alumno)
            
            case "2":
                if validar_existencia_alumno(lista_alumnos, "activo")==True:
                    mostrar_lista_alumnos(lista_alumnos, "activo")
                else:
                    print("ERROR.No hay alumnos para mostrar.")

            case "3":
                if validar_existencia_alumno(lista_alumnos,"activo")==True:
                    calcular_promedio(lista_alumnos,"promedio","nota")
                    print("SE CALCULARON LOS PROMEDIOS EXISTOSAMENTE :)")
                else:
                    print("ERROR.No hay alumnos para mostrar.")     
            
            case "4":
                if validar_existencia_alumno(lista_alumnos,"activo")==True:
                    mostrar_estado_aprobacion(lista_alumnos,"promedio",diccionario,"El alumno {} esta {}.","nombre","ERROR.El alumno {} no tiene promedio calculado")
                else:
                    print("ERROR.No hay alumnos para mostrar.") 
            case "5":
                if validar_existencia_alumno(lista_alumnos,"activo")==True:
                    nombre_buscar = input("ingrese el nombre del alumno a buscar: ")
                    alumno_encontrado = buscar_alumno(lista_alumnos,nombre_buscar)
                    if alumno_encontrado == None:
                        print("alumno no encontrado")
                    else:
                        mostrar_encabezado(alumno_encontrado)
                        mostrar_alumno(alumno_encontrado)  
                else:
                    print("ERROR.No hay alumnos para mostrar.")

            case "6":
                if validar_existencia_alumno(lista_alumnos, "activo")==True:
                    nombre_buscar = input("ingrese el nombre del alumno a eliminar: ")
                    alumno_encontrado = buscar_alumno(lista_alumnos,nombre_buscar)
                    if alumno_encontrado == None:
                        print("alumno no encontrado")
                    else:
                        borrar_alumno(lista_alumnos, alumno_encontrado)
                        print("Alumno eliminado.")              
                else:
                    print("ERROR. No hay alumnos para mostrar.") 
            
            case "7":
                if validar_existencia_alumno(lista_alumnos, "activo")==True:
                    nombre_buscar = input("ingrese el nombre del alumno a dar de baja: ")
                    alumno_encontrado = buscar_alumno(lista_alumnos,nombre_buscar)
                    if alumno_encontrado == None:
                        print("alumno no encontrado")
                    else:
                        borrar_alumno_logico(alumno_encontrado, "activo", False)
                        print("Alumno dado de baja.")              
                else:
                    print("ERROR. No hay alumnos para mostrar.") 

            case "8":
                if validar_existencia_alumno(lista_alumnos, "activo")==True:
                    calcular_promedio(lista_alumnos, "promerdio", "nota")
                    criterio = validar_criterio("ingrese el criterio max o min: ", ["max", "min"])
                    min_max = buscar_min_max_promedio(lista_alumnos,criterio, "promerdio")
                    mostrar_encabezado(min_max)
                    mostrar_alumno(min_max)

                else:
                    print("ERROR. No hay alumno para mostrar.")

            case "9":
                if validar_existencia_alumno(lista_alumnos, "activo")==True:
                    calcular_promedio(lista_alumnos, "promerdio", "nota")
                    criterio = validar_criterio("ingrese el criterio ASC o DESC: ", ["asc", "desc"])
                    ordenar_alumnos(lista_alumnos, criterio)
                    print("SE ORDENARON LOS ALUMNOS EXISTOSAMENTE :", criterio)
                else:
                    print("ERROR. No hay alumno para mostrar.")
            
            case "10":
                if validar_existencia_alumno(lista_alumnos, "activo") == True:
                    cantidad_alumnos_por_estado(lista_alumnos, diccionario, "promedio")
                else:
                    print("ERROR. No hay alumnos para mostrar.")
                    
            case "0":
                print("Gracias vuelva prontos")
                break

            case _:
                print("Opción Invalida")

menu_dicc(menu)