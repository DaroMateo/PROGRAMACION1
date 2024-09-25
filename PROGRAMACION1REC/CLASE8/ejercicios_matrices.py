import random
'''1- Crear y cargar una matriz de 4x4 con datos numéricos aleatorios entre 1 y 9 inclusive, en formato string.
Mostrar los números pares de esa matriz (en filas y columnas) y reemplazar los números impares con
cadenas vacías para ocultarlos'''
def inicializar_matriz(columna:int,filas:int)->list:
    """
    Crea y devuelve una matriz vacia de tamano columna x filas.
    
    Parameters:
    columna (int): El numero de columnas de la matriz.
    filas (int): El numero de filas de la matriz.
    
    Returns:
    list: La matriz vacia.
    """
    matriz=[]
    for i in range(filas):
        matriz += [[None] * columna]
    return matriz

def crear_matriz_aleatorio(columna:int,filas:int, desde:int, hasta:int)->list:
    """
    Crea y carga una matriz de tamano columna x filas con numeros enteros aleatorios
    entre "desde" y "hasta" inclusive.

    Parameters:
    columna (int): El numero de columnas de la matriz.
    filas (int): El numero de filas de la matriz.
    desde (int): El limite inferior de los numeros aleatorios.
    hasta (int): El limite superior de los numeros aleatorios.

    Returns:
    list: La matriz cargada con los numeros aleatorios.
    """
    matriz=inicializar_matriz(columna,filas)
    for i in range(filas):
        for j in range(columna):
            matriz[i][j]= str(random.randint(desde,hasta))
    return matriz

def mostrar_matriz(matriz:list)->None:
    """
    Muestra por pantalla la matriz pasada como par metro con los elementos alineados en columnas.
    Los elementos se muestran en formato string, con un ancho de 3 caracteres.
    
    Parameters:
    matriz (list): La matriz a mostrar.
    
    Returns:
    None
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}", end=" ")
        print(" ")

def ocultar_impares(matriz:list)->list:
    """
    Reemplaza los elementos impares de la matriz por cadenas vacias.
    
    Parameters:
    matriz (list): La matriz a reemplazar.
    
    Returns:
    list: La matriz reemplazada.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])): 
            if int(matriz[i][j]) % 2 == 0:
                print(f"{matriz[i][j]}", end=" ")
            else:
                print("#", end=" ")
        print(" ")
    return matriz

#matriz = crear_matriz_aleatorio(4,4,1,9)
#mostrar_matriz(matriz)
#print ('-----------------------')
#ocultar_impares(matriz)
#print('-----------------------')
#mostrar_matriz(matriz)



'''2- Generar una matriz de 3x3 cargando datos numéricos del 1 al 9 inclusive en celdas aleatorias, sin que se
repitan los números (al estilo Sudoku).'''
def  repetir_numeros(matriz:list,desde:int,hasta:int)->list:
    """
    Revisa si hay elementos repetidos en la matriz.
    
    Parameters:
    matriz (list): La matriz a revisar.
    desde (int): El limite inferior de los numeros aleatorios.
    hasta (int): El limite superior de los numeros aleatorios.
    
    Returns:
    list: La matriz reemplazada.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if int(matriz[i][j]) in range(desde,hasta):
                while int(matriz[i][j]) in range(desde,hasta):
                    matriz[i][j] = str(random.randint(desde,hasta))
    return matriz

def buscar_valor(matriz:list, valor:int)-> bool:
    resultado = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                resultado = True
                break 
        if resultado == True:
            break
    return resultado

def generar_matriz_sudoku(matriz:list, desde:int, hasta:int)-> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numero = random.randint(desde, hasta)
            while buscar_valor(matriz, numero) == True:
                numero = random.randint(desde, hasta)
            matriz[i][j] = numero

#matriz = inicializar_matriz(3,3)
#generar_matriz_sudoku(matriz,1,9)
#mostrar_matriz(matriz)

"""3- Desarrollar una función que reciba 2 matrices, los sume y devuelva la matriz resultante, sin modificar las
matrices originales."""
def sumar_matrices(matriz_1, matriz_2):
    """
    Suma dos matrices y devuelve la matriz resultante. La suma se realiza
    elemento a elemento, sin modificar las matrices originales.
    
    Parameters:
    matriz_1 (list): La primera matriz a sumar.
    matriz_2 (list): La segunda matriz a sumar.
    
    Returns:
    list: La matriz resultante de la suma.
    """
    matriz_resultante = inicializar_matriz(len(matriz_1), len(matriz_1[0]))
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            matriz_resultante[i][j] = int(matriz_1[i][j]) + int(matriz_2[i][j])
    return matriz_resultante

"""matriz1 = crear_matriz_aleatorio(4,4,1,9)
matriz2 = crear_matriz_aleatorio(4,4,5,15)
mostrar_matriz(matriz1)
print("------------")
mostrar_matriz(matriz2)
print("------------")
resultado = sumar_matrices(matriz1, matriz2)
mostrar_matriz(resultado)"""

'''4- Desarrollar una función que reciba una matriz y un número escalar, multiplicar la matriz por el número
escalar y retornar la matriz resultante, sin modificar la matriz original
'''

def multipliacar_matriz_con_esacalar(matriz:list,escalar:int)->list:
    """
    Multiplica una matriz por un número escalar y devuelve la matriz resultante.
    
    Parameters:
    matriz (list): La matriz a multiplicar.
    escalar (int): El número escalar por el que se multiplica la matriz.
    
    Returns:
    list: La matriz resultante de la multiplicación.
    """

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(matriz[i][j]) * escalar
    return matriz

#matriz = crear_matriz_aleatorio(4,4,1,9)
#mostrar_matriz(matriz)
#print("------------")
#matriz_escalar = multipliacar_matriz_con_esacalar(matriz,4)
#mostrar_matriz(matriz_escalar)

"""5- Desarrollar una función que reciba dos matrices, y las multiplique entre sí. Se debe validar que las matrices
recibidas por parámetro se puedan multiplicar entre sí y devolver la matriz resultante, sin alterar las matrices
originales, caso contrario la función devolverá un None"""

def validar_matriz_multiplicable(matriz_1: list, matriz_2: list) -> bool:
    """
    Valida si dos matrices se pueden multiplicar entre ellas.
    """
    resultado = False
    if len(matriz_1[0]) == len(matriz_2):
        resultado = True
    return resultado

def inicializar_matriz(columnas: int, filas: int) -> list:
    """
    Crea y devuelve una matriz vacía de tamaño columnas x filas.
    
    Parameters:
    columnas (int): El número de columnas de la matriz.
    filas (int): El número de filas de la matriz.
    
    Returns:
    list: La matriz vacía.
    """
    matriz = []
    for _ in range(filas):
        fila = [0] * columnas  # Crea una nueva fila con ceros
        matriz.append(fila)    # Agrega la fila a la matriz
    return matriz

def multiplicar_matrices(matriz_1: list, matriz_2: list) -> list:
    """
    Multiplica dos matrices y devuelve la matriz resultante. La multiplicación se realiza
    de acuerdo a la regla de multiplicación de matrices, sin modificar las matrices originales.
    
    Parameters:
    matriz_1 (list): La primera matriz a multiplicar.
    matriz_2 (list): La segunda matriz a multiplicar.
    
    Returns:
    list: La matriz resultante de la multiplicación, o None si no se pueden multiplicar.
    """
    # Validar que las matrices se pueden multiplicar
    if not validar_matriz_multiplicable(matriz_1, matriz_2):
        return None

    filas_resultante = len(matriz_1)
    columnas_resultante = len(matriz_2[0])
    matriz_resultante = inicializar_matriz(columnas_resultante, filas_resultante)

    for i in range(filas_resultante):
        for j in range(columnas_resultante):
            for k in range(len(matriz_2)):  
                matriz_resultante[i][j] += int(matriz_1[i][k]) * int(matriz_2[k][j])
    return matriz_resultante



'''matriz1 = crear_matriz_aleatorio(3,2,1,9)
matriz2 = crear_matriz_aleatorio(2,3,5,15)
mostrar_matriz(matriz1)
print("------------")
mostrar_matriz(matriz2)
print("------------")
resultado = multiplicar_matrices(matriz1, matriz2)
mostrar_matriz(resultado)'''

'''6- Desarrollar un programa que cuente con un menú y las siguientes opciones:
a) Generar una matriz con números aleatorios. Las dimensiones y los rangos de números se deben pasar
por parámetros de la función generadora. No se debe poder acceder a las demás opciones si la matriz
no fue generada.
b) Mostrar la matriz generada.
c) Determinar si la matriz contiene series de números consecutivos (en horizontal o en vertical).
d) Determinar la cantidad total de series (las series de números consecutivos de más de dos números
cuentan como una sola).
e) Determinar el largo de la serie más corta, y mostrar todas las series de ese largo.
f) Determinar el largo de la serie más larga, y mostrar todas las series de ese largo.
g) Salir.'''

def contiene_series_consecutivas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    series_horizontales = []  # Lista para almacenar series consecutivas en filas
    series_verticales = []     # Lista para almacenar series consecutivas en columnas

    # Verificar consecutivos en filas (horizontal)
    for i in range(filas):
        serie_actual = []  # Lista para la serie actual en la fila
        for j in range(columnas - 1):
            if int(matriz[i][j]) + 1 == int(matriz[i][j + 1]):
                serie_actual.append(int(matriz[i][j]))  # Agregar el número actual a la serie
            else:
                if serie_actual:  # Si hay una serie en curso, la cerramos
                    serie_actual.append(int(matriz[i][j]))  # Agregar el último número
                    series_horizontales += [serie_actual]  # Agregar la serie a la lista
                    serie_actual = []  # Reiniciar la serie actual
        if serie_actual:  # Si hay una serie al final de la fila
            serie_actual += [int(matriz[i][columnas - 1])]  # Agregar el último número
            series_horizontales += [serie_actual]  # Agregar la serie a la lista

    # Verificar consecutivos en columnas (vertical)
    for j in range(columnas):
        serie_actual = []  # Lista para la serie actual en la columna
        for i in range(filas - 1):
            if int(matriz[i][j]) + 1 == int(matriz[i + 1][j]):
                serie_actual += [int(matriz[i][j])]  # Agregar el número actual a la serie
            else:
                if serie_actual:  # Si hay una serie en curso, la cerramos
                    serie_actual.append(int(matriz[i][j]))  # Agregar el último número
                    series_verticales += [serie_actual]  # Agregar la serie a la lista
                    serie_actual = []  # Reiniciar la serie actual
        if serie_actual:  # Si hay una serie al final de la columna
            serie_actual += [int(matriz[filas - 1][j])]  # Agregar el último número
            series_verticales += [serie_actual]  # Agregar la serie a la lista

    return series_horizontales, series_verticales

def encontrar_series(matriz):
    series_horizontales = contiene_series_consecutivas(matriz)[0]
    series_verticales = contiene_series_consecutivas(matriz)
    suma = len(series_horizontales) + len(series_verticales)
    return suma

def cantidad_series(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    cantidad_total_series = 0

    # Verificar consecutivos en filas (horizontal)
    for i in range(filas):
        serie_actual = 0  # Contador para la serie actual en la fila
        for j in range(columnas - 1):
            if int(matriz[i][j]) + 1 == int(matriz[i][j + 1]):
                serie_actual += 1  # Aumenta el contador si son consecutivos
            else:
                if serie_actual > 0:  # Si hay una serie en curso
                    cantidad_total_series += 1  # Aumentar el total de series
                    serie_actual = 0  # Reiniciar el contador
        if serie_actual > 0:  # Comprobar si hay una serie al final de la fila
            cantidad_total_series += 1

    # Verificar consecutivos en columnas (vertical)
    for j in range(columnas):
        serie_actual = 0  # Contador para la serie actual en la columna
        for i in range(filas - 1):
            if int(matriz[i][j]) + 1 == int(matriz[i + 1][j]):
                serie_actual += 1  # Aumenta el contador si son consecutivos
            else:
                if serie_actual > 0:  # Si hay una serie en curso
                    cantidad_total_series += 1  # Aumentar el total de series
                    serie_actual = 0  # Reiniciar el contador
        if serie_actual > 0:  # Comprobar si hay una serie al final de la columna
            cantidad_total_series += 1

    return cantidad_total_series

def series_por_largo(matriz, largo):
    series = encontrar_series(matriz)
    for serie in series:
        if len(serie) == largo:
            resultado = serie
    return resultado
def mostrar_series(matriz):
    series = encontrar_series(matriz)
    for i in range(len(series)):
        for j in range(len(series[i])):
            print(f"{series[i][j]}", end=" ")
        print(" ")
    

def menu():
    matriz = None
    
    while True:
        print("\n--- Menú ---")
        print("a) Generar matriz con números aleatorios")
        print("b) Mostrar matriz generada")
        print("c) Determinar si la matriz contiene series de números consecutivos")
        print("d) Determinar la cantidad total de series")
        print("e) Determinar el largo de la serie más corta y mostrar todas las series de ese largo")
        print("f) Determinar el largo de la serie más larga y mostrar todas las series de ese largo")
        print("g) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == 'a':
            filas = int(input("Ingrese el numero de filas: "))
            columnas = int(input("Ingrese el numero de columnas: "))
            desde = int(input("Ingrese el valor mínimo del rango: "))
            hasta = int(input("Ingrese el valor máximo del rango: "))
            matriz = crear_matriz_aleatorio(columnas,filas, desde, hasta)
            print("Matriz generada exitosamente.")

        elif opcion == 'b':
            if matriz:
                print("Matriz generada:")
                mostrar_matriz(matriz)
            else:
                print("Debe generar la matriz primero.")

        elif opcion == 'c':
            if matriz:
                series_horizontales= contiene_series_consecutivas(matriz)
                series_verticales = contiene_series_consecutivas(matriz)
                if series_horizontales or series_verticales:
                    print("La matriz contiene las siguientes series:")
                    print("Series horizontales:")
                    mostrar_matriz(series_horizontales)
                    print("Series verticales:")
                    mostrar_matriz(series_verticales)
                else:
                    print("No se encontraron series.")
            else:
                print("Debe generar la matriz primero.")

        elif opcion == 'd':
            if matriz:
                total_series = cantidad_series(matriz)
                print(f"Cantidad total de series: {total_series}")
            else:
                print("Debe generar la matriz primero.")

        elif opcion == 'e':
            if matriz:
                series = encontrar_series(matriz)
                if series:
                    if series:
                        largo_min = 0  # Inicializa largo_min a 0
                        for serie in series:  # Recorre cada serie en la lista
                            largo_actual = len(serie)  # Calcula la longitud de la serie actual
                            if largo_actual > largo_min:  # Compara con el largo máximo encontrado
                                largo_min = largo_actual
                    print(f"Largo de la serie más corta: {largo_min}")
                    series_cortas = series_por_largo(matriz, largo_min)
                    print("Series de ese largo:")
                    mostrar_series(series_cortas)
                else:
                    print("No se encontraron series.")
            else:
                print("Debe generar la matriz primero.")

        elif opcion == 'f':
            if matriz:
                series = encontrar_series(matriz)
                if series:
                    largo_max = 0  # Inicializa largo_max a 0
                    for serie in series:  # Recorre cada serie en la lista
                        largo_actual = len(serie)  # Calcula la longitud de la serie actual
                        if largo_actual > largo_max:  # Compara con el largo máximo encontrado
                            largo_max = largo_actual
                    print(f"Largo de la serie más larga: {largo_max}")
                    series_largas = series_por_largo(matriz, largo_max)
                    print("Series de ese largo:")
                    mostrar_series(series_largas)
                else:
                    print("No se encontraron series.")
            else:
                print("Debe generar la matriz primero.")

        elif opcion == 'g':
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()