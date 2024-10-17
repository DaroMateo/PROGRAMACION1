import random
def inicializar_matriz(cant_filas:int, cant_columnas:int)->list:
    '''
    Inicializa una matriz de 2x2
    recibe cantidad de filas y columnas
    Retorna una matriz inicializada en 0s
    '''
    matriz =[]
    for _ in range(cant_filas):
        fila= [0] * cant_columnas
        matriz += [fila]
    return matriz

def imprimir_matriz(matriz:list)->None:
    '''
    Imprime la matriz de 2x2
    Recibe una matriz
    No tiene retorno
    '''
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            print(f"{matriz[i][j]:3}", end=" ")
        print(" ")

def buscar_coordenada_matriz(matriz:list, dato:int)->list: #Print mas lista con coordenada
    '''
    Busca las coordenadas de un dato en una matriz de 2x2
    Recibe una matriz y un dato parametro
    Devuelve una lista con la coordenada
    '''
    coordenada = []
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == dato:
                print(f"La coordenada del elemento {dato} es {i},{j}")
                coordenada += [i]
                coordenada += [j]
    return coordenada

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
    """
    Busca un valor dentro de una matriz y devuelve True si lo encuentra, False si no.
    
    Parameters:
    matriz (list): La matriz a buscar.
    valor (int): El valor a buscar.
    
    Returns:
    bool: True si el valor se encuentra en la matriz, False si no.
    """
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
    """
    Genera una matriz de sudoku con valores aleatorios entre el rango dado.
    
    Parameters:
    matriz (list): La matriz a generar.
    desde (int): El limite inferior de los numeros aleatorios.
    hasta (int): El limite superior de los numeros aleatorios.
    
    Returns:
    None: La funcion no devuelve nada, modifica la matriz pasada por parametro.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numero = random.randint(desde, hasta)
            while buscar_valor(matriz, numero) == True:
                numero = random.randint(desde, hasta)
            matriz[i][j] = numero

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

def validar_matriz_multiplicable(matriz_1: list, matriz_2: list) -> bool:
    """
    Valida si dos matrices se pueden multiplicar entre ellas.
    """
    resultado = False
    if len(matriz_1[0]) == len(matriz_2):
        resultado = True
    return resultado


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

def contiene_series_consecutivas(matriz):
    """
    Verifica si una matriz contiene series de números consecutivos en filas y columnas.
    
    Parameters:
    matriz (list): La matriz a verificar.
    
    Returns:
    tuple: Un par de listas, la primera para series horizontales y la segunda para series verticales. Cada serie
    es una lista con los números consecutivos.
    """
    
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
    """
    Encuentra la cantidad total de series (las series de números consecutivos de más de dos números
    cuentan como una sola) en una matriz.

    Parameters
    ----------
    matriz : list of list
        Matriz en la que se buscarán las series de números consecutivos.

    Returns
    -------
    int
        Cantidad total de series en la matriz.

    """
    series_horizontales = contiene_series_consecutivas(matriz)[0]
    series_verticales = contiene_series_consecutivas(matriz)
    suma = len(series_horizontales) + len(series_verticales)
    return suma

def cantidad_series(matriz):
    """
    Determina la cantidad total de series (las series de números consecutivos de más de dos números
    cuentan como una sola) en una matriz.

    Parameters
    ----------
    matriz : list of list
        Matriz en la que se buscarán las series de números consecutivos.

    Returns
    -------
    int
        Cantidad total de series en la matriz.

    """
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
    """
    Recibe una matriz y un largo, y devuelve una serie que est  en la matriz y tiene ese largo.
    Si no se encuentra una serie con ese largo, devuelve None.
    """
    series = encontrar_series(matriz)
    for serie in series:
        if len(serie) == largo:
            resultado = serie
    return resultado
def mostrar_series(matriz):
    """
    Muestra por pantalla todas las series de n meros consecutivos horizontales y verticales
    presentes en la matriz.
    """
    
    series = encontrar_series(matriz)
    for i in range(len(series)):
        for j in range(len(series[i])):
            print(f"{series[i][j]}", end=" ")
        print(" ")
    
