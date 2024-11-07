menu= """
1 (ALTA)
2 (MOSTRAR ALUMNOS)
3 (PROMEDIO)
4 (ESTADO ACADEMICO)
0 (SALIR)
"""

# 1)Alta: Desarrolle una función que permita cargar un diccionario a partir de los datos que ingresa el
# usuario por consola, los datos se componen por un nombre de alumno y 2 calificaciones (primer y
# segundo examen parcial)

def cargar_diccionario(lista_claves:list, mensaje:str)-> dict:
    diccionario_alumno = {}

    for clave in lista_claves:
        valor = input(mensaje.format(clave))
        diccionario_alumno.update({clave:valor})
    return diccionario_alumno


# 2) Desarrolle una función que muestre una lista de alumnos y sus respectivos datos en filas y columnas,
# donde cada fila representa un alumno y cada columna representa uno de sus datos.

def mostrar_alumno(diccionario_alumno: dict) -> None:

    for claves in diccionario_alumno:
        print(f"{diccionario_alumno[claves]:^10}", end= "")
        
    print("")

def mostrar_encabezado(diccionario: dict):
    for clave in diccionario:                                #De este modo solo recorre CLAVES, recordar relación entre Clave y Valor (similar a Listas pero con Claves, no Ind).
        print(f"{clave.upper():^10}", end= "")
        
    print("\n---------------------------------------------")

def mostrar_lista_alumnos(lista_de_alumnos: list) -> None:
    if len(lista_de_alumnos) > 0:
        mostrar_encabezado(lista_de_alumnos[0])
        for alumno in lista_de_alumnos:
            mostrar_alumno(alumno)
    else:
        print("La lista está vacía.")


#print(menu_dicc(menu))


# 3) Modificación: Desarrolle una función que permita calcular el promedio de calificaciones a partir de
# una lista de alumnos. Recibe una lista de diccionarios por parámetro, calcula el promedio y lo agrega
# como un ítem más al diccionario.

def calcular_promedio (lista_de_alumnos:list[dict], clave_parametro :str, ident:str) -> bool: # CADA ELEMENTO DE LA LISTA VA A SER UN DICCIONARIO
    retorno = False

    for alumno in lista_de_alumnos: 
       
        acumulador = 0
        contador = 0
       
        for clave in alumno.keys():
            if clave[0:4] == ident:
                if alumno.get("Nota") is not None:
                    acumulador += int(alumno["Nota"])
                    contador += 1

        #promedio = (int(alumno["nota_pp"]) + int(alumno["nota_sp"])) / 2
        if contador > 0:
            promedio = acumulador / contador
            alumno.update({clave_parametro:promedio})
            retorno = True

    return retorno
# 4) Desarrolle una función que informe por cada alumno de la lista su estado académico (promedio de 1 al
# 4: desaprobado, 4 o 5: aprobado, y 6 o más: promocionado).
def estado_academico(alumno: dict,clave_parametro:str) -> bool:
    retorno = False
    if int(alumno) >= 6:
        alumno.update({clave_parametro:"promocionado"})
        retorno = True
    elif int(alumno) >= 4:
        alumno.update({clave_parametro:"aprobado"})
        retorno = True
    else:
        alumno.update({clave_parametro:"desaprobado"})
        retorno = True
    return retorno
# 5) Desarrolle una función que informe las notas y el promedio del alumno cuyo nombre recibe por
# parámetro, en caso de no encontrarlo deberá imprimir un mensaje de error.
# 6) Baja Física: Desarrolle una función que pueda eliminar a un alumno de la lista de alumnos. El alumno
# a eliminar deberá seleccionarlo el usuario por terminal, validar que exista antes de eliminarlo, y en
# caso de que no exista mostrar un mensaje de error.
# 7) Baja Lógica: Desarrolle una función que pueda dar de baja lógicamente a un alumno de la lista.
# Deberá recibir por parámetro el nombre del alumno a eliminar y agregarle un estado (bool) activo o
# inactivo. Modificar la función que muestra los alumnos haciendo que ignore a todos los alumnos
# inactivos.
# 8) Desarrolle una función que busque al alumno con el mejor o con el peor promedio. Informar sus
# nombres y sus respectivos promedios.
# 9) Desarrolle una función que ordene a los alumnos por promedio ASC/DESC.
# 10) Desarrolle una función que calcule e informe la cantidad de alumnos según su estado académico
# (desaprobado, aprobado o promocionado).

def menu_dicc(mensaje_menu:str):

    lista_claves = ["nombre", "nota_pp", "nota_sp"]
    mensaje_input =  "Ingrese {} del alumno: "
    lista_alumnos = []
    while True:

        print(mensaje_menu)
        opcion_elegida = input("Ingrese Opcion: ")


        match opcion_elegida:

            case "1":
                alumno = cargar_diccionario(lista_claves,mensaje_input)
                lista_alumnos.append(alumno)
            
            case "2":
                mostrar_lista_alumnos(lista_alumnos)

            case "3":
                calcular_promedio(lista_alumnos,"Promedio","nota")

            case "4":
                for alumno in lista_alumnos:
                    estado_academico(alumno,"Estado Academico")

            case "0":
                print("Gracias vuelva prontos")
                break

            case _:
                print("Opción Invalida")

print(menu_dicc(menu))