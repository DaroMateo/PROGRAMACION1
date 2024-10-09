import random

# Función para generar una lista alfanumérica de 1000 elementos usando códigos ASCII
def generar_lista_alfanumerica():
    """
    Genera una lista alfanumérica de 1000 elementos utilizando códigos ASCII. La lista
    contiene 26 caracteres alfabéticos mayúsculas (A-Z) y 10 caracteres numéricos (0-9)
    en orden aleatorio.
    
    Returns:
    list: una lista alfanumérica de 1000 elementos.
    """
    
    lista = []
    for _ in range(1000):
        num = random.randint(0, 35)
        if num < 10:
            lista.append(chr(num + 48))  # 0-9
        else:
            lista.append(chr(num - 10 + 65))  # A-Z
    return lista

# Función para ordenar una lista alfanumérica
def ordenar_lista(lista, criterio='ASC'):
    """
    Ordena una lista alfanumérica en forma ascendente o descendente
    
    Args:
        lista (list): La lista alfanumérica a ordenar.
        criterio (str): El criterio de ordenamiento. Puede ser 'ASC' para ordenar en forma ascendente o 'DESC' para ordenar en forma descendente. Por defecto es 'ASC'.
    
    Returns:
        list: La lista ordenada seg n el criterio seleccionado.
    """
    
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if (criterio == 'ASC' and lista[i] > lista[j]) or (criterio == 'DESC' and lista[i] < lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def mostrar_lista(lista):
    """
    Muestra los elementos de una lista.
    
    Parameters:
    lista (list): la lista a mostrar
    """
    
    for elem in lista:
        print(elem, end=" ")
    print()

def mostrar_matriz(matriz):
    """
    Muestra por pantalla una matriz de enteros, con los elementos alineados en columnas.
    
    Parameters:
    matriz (list): La matriz a mostrar.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

# Función para contar la cantidad de cada carácter alfabético
def contar_caracteres(lista):
    """
    Crea un diccionario que contiene como clave cada carácter alfabético mayúscula
    y como valor la cantidad de veces que se repite en la lista.
    
    Parameters:
    lista (list): lista de caracteres alfanuméricos
    
    Returns:
    dict: diccionario con la cantidad de veces que se repite cada carácter alfabético
    """
    conteo = {}
    # Inicializar el diccionario con todas las letras del alfabeto en mayúsculas
    for i in range(65, 91):  # Códigos ASCII de 'A' a 'Z'
        conteo[chr(i)] = 0
    
    # Contar cada carácter en la lista
    for caracter in lista:
        if 'A' <= caracter <= 'Z':  # Verificar si el carácter es una letra mayúscula
            conteo[caracter] += 1

    return conteo

# Función para obtener el caracter que más y menos se repite
def obtener_max_min(conteo):
    # Inicializar valores máximos y mínimos
    """
    Obtiene el caracter que más y menos se repite en un diccionario de conteo.
    
    Parameters:
    conteo (dict): Diccionario que contiene como clave cada carácter alfabético
                   y como valor la cantidad de veces que se repite.
    
    Returns:
    tuple: Tupla que contiene el caracter que más se repite, la cantidad de veces que se repite,
           el caracter que menos se repite y la cantidad de veces que se repite.
    """
    max_caracter = None
    min_caracter = None
    max_cantidad = -1
    min_cantidad = float('inf')

    # Iterar sobre el diccionario de conteo
    for caracter in conteo:
        cantidad = conteo[caracter]
        if cantidad > max_cantidad:
            max_cantidad = cantidad
            max_caracter = caracter
        if cantidad < min_cantidad:
            min_cantidad = cantidad
            min_caracter = caracter

    return max_caracter, max_cantidad, min_caracter, min_cantidad

# Función para generar una matriz de 10x10 de números enteros
def generar_matriz():
    """
    Genera una matriz de 10x10 de números enteros aleatorios entre 0 y 100.
    
    Returns:
    list: La matriz generada.
    """
    matriz = []
    for i in range(10):
        fila = [0] * 10  # Crear una fila con 10 elementos inicializados a 0
        for j in range(10):
            fila[j] = random.randint(0, 100)  # Asignar un valor aleatorio a cada posición de la fila
        matriz += [fila]  # Agregar la fila a la matriz
    return matriz

# Función para validar el ingreso de un número entero de dos dígitos como mínimo
def validar_ingreso_entero(min_digitos=2):
    """
    Valida el ingreso de un número entero de dos dígitos como mínimo.
    
    Parameters:
    min_digitos (int): La cantidad mínima de dígitos que debe tener el número entero.
    
    Returns:
    str: La entrada del usuario como una cadena de caracteres.
    
    Notes:
    Verifica que la entrada tenga la cantidad mínima de caracteres y que cada carácter sea un dígito.
    Si no es válido, pide al usuario que ingrese nuevamente una secuencia numérica.
    """
    while True:
        entrada = input("Ingrese una secuencia numérica (de dos dígitos como mínimo): ")
        es_valido = True

        # Verificar que la entrada tiene la longitud mínima requerida
        if len(entrada) < min_digitos:
            es_valido = False

        # Verificar que cada carácter en la entrada es un dígito
        for char in entrada:
            if char < '0' or char > '9':
                es_valido = False
                break

        if es_valido:
            return entrada
        else:
            print("El valor ingresado no es una secuencia numérica válida. Intente nuevamente.")


# Función para buscar una secuencia numérica en la matriz de manera horizontal
def buscar_secuencia(matriz, secuencia):
    """
    Busca una secuencia numérica en una matriz de manera horizontal.
    
    Parameters:
    matriz (list): La matriz a buscar.
    secuencia (str): La secuencia numérica a buscar.
    
    Returns:
    bool: True si la secuencia se encuentra en la matriz, False si no.
    """
    for fila in matriz:
        fila_str = ''
        for num in fila:
            fila_str += str(num)
        
        # Comprobar si la secuencia está en fila_str
        encontrado = False
        for i in range(len(fila_str) - len(secuencia) + 1):
            if fila_str[i:i + len(secuencia)] == secuencia:
                encontrado = True
                break
        
        if encontrado:
            return True
    return False

def mostrar_secuencia_en_matriz(matriz, secuencia):
    """
    Muestra la secuencia en la matriz, representando los elementos que se encuentran en la
    secuencia con 'X' y los que no con '0'.
    
    Parameters:
    matriz (list): La matriz a imprimir.
    secuencia (str): La secuencia numérica a buscar en la matriz.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if str(matriz[i][j]) in secuencia:
                print("X", end=" ")
            else:
                print("0", end=" ")
        print()

# Menú de opciones
def menu():
    """
    Menú de opciones para interactuar con la lista alfanumérica y la matriz de números enteros.
    
    Las opciones permiten:
        1 - Generar la lista alfanumérica aleatoria.
        2 - Ordenar la lista alfanumérica.
        3 - Buscar e informar cuantas veces se repite cada carácter alfabético.
        4 - Obtener el carácter que más y menos se repite.
        5 - Generar la matriz aleatoria de números enteros.
        6 - Buscar una secuencia numérica en la matriz.
        7 - Salir.
    
    Se debe generar la lista alfanumérica y la matriz aleatoria de números enteros antes de acceder a las demás opciones.
    """
    lista_alfanumerica = []
    matriz = []
    
    while True:
        print("\nMenú de Opciones:")
        print("1 – Generar la lista alfanumérica aleatoria")
        print("2 – Ordenar la lista alfanumérica")
        print("3 – Buscar e informar cuantas veces se repite cada carácter alfabético")
        print("4 – Obtener el carácter que más y menos se repite")
        print("5 – Generar la matriz aleatoria de números enteros")
        print("6 – Buscar una secuencia numérica en la matriz")
        print("7 – Salir")
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case '1':
                lista_alfanumerica = generar_lista_alfanumerica()
                print("Lista alfanumérica generada.")
                mostrar_lista(lista_alfanumerica)
            case '2':
                if lista_alfanumerica:
                    criterio = input("Ingrese el criterio de ordenamiento (ASC/DESC): ")
                    criterio_convertido = ''
                    for char in criterio:
                        if 'a' <= char <= 'z':
                            criterio_convertido += chr(ord(char) - 32)
                        else:
                            criterio_convertido += char
                    lista_alfanumerica = ordenar_lista(lista_alfanumerica, criterio_convertido)
                    print(f"Lista ordenada ({criterio_convertido}).")
                    mostrar_lista(lista_alfanumerica)
                else:
                    print("Primero debe generar la lista alfanumérica (opción 1).")
            case '3':
                if lista_alfanumerica:
                    conteo = contar_caracteres(lista_alfanumerica)
                    print("CARACTER | CANTIDAD")
                    for caracter in conteo:  
                        cantidad = conteo[caracter]  # Obteniendo cantidad sin métodos
                        print(f"   {caracter}    |    {cantidad}")
                else:
                    print("Primero debe generar la lista alfanumérica (opción 1).")
            case '4':
                if lista_alfanumerica:
                    conteo = contar_caracteres(lista_alfanumerica)
                    max_caracter, max_cantidad, min_caracter, min_cantidad = obtener_max_min(conteo)
                    print(f"El carácter que más veces se repite: {max_caracter} ({max_cantidad})")
                    print(f"El carácter que menos veces se repite: {min_caracter} ({min_cantidad})")
                else:
                    print("Primero debe generar la lista alfanumérica (opción 1).")
            case '5':
                matriz = generar_matriz()
                print("Matriz de 10x10 generada:")
                for fila in matriz:
                    print(fila)
            case '6':
                if not matriz:
                    print("Primero debe generar la matriz aleatoria de números enteros (opción 5).")
                else:
                    secuencia = validar_ingreso_entero()
                    if buscar_secuencia(matriz, secuencia):
                        print(f"La secuencia numérica {secuencia} existe en la matriz.")
                        mostrar_secuencia_en_matriz(matriz, secuencia)
                    else:
                        print(f"La secuencia numérica {secuencia} no existe en la matriz.")
            case '7':
                break
