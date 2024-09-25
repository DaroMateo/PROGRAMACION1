import random
def sumar_enteros(lista:list)->int:
    """
    Calcula la suma de todos los elementos de una lista determinada.
    
    Parameters:
    lista (list): la lista de enteros a sumar.
    
    Returns:
    int: la suma de todos los elementos de la lista.
    """
    total_suma = 0
    for i in range(len(lista)):
        total_suma += lista[i]
    return total_suma

def mostrar_elemento(lista: list, indice:int, mensaje:str) -> None:
    """
    Muestra el elemento en la posicion dada de una lista con un mensaje.
    
    Parameters:
    lista (list): la lista que contiene el elemento a mostrar
    indice (int): la posicion del elemento en la lista
    mensaje (str): el mensaje a mostrar antes del elemento
    """
    print(f"{mensaje}: {lista[indice]}")


def mostrar_promedio(lista:list)-> None:
    """
    Muestra el promedio de las dos notas de un alumno.
    
    Parameters:
    lista (list): una lista que contiene el nombre del alumno y sus dos notas como elementos.
    """
    print(f"Nombre del alumno: {lista[0]} y su promedio es {(lista[1] + lista[2])/2}")

def contador_mayores(lista:list, minimo:int)-> int:
    """
    Contador de elementos en una lista que son superiores a un minimo
    
    Parameters:
    lista (list): la lista a contar
    minimo (int): el minimo para comparar
    
    Returns:
    int: la cantidad de elementos en la lista que son superiores al minimo
    """
    
    contador = 0
    for elemento in lista:
        if elemento > minimo:
            contador += 1
    return contador


def filtrar_lista(lista:list, valor_superior_igual:int)->list:
    
    """
    Filtra una lista y devuelve una nueva lista solo con los elementos
    que son superiores o iguales al valor_superior_igual.
    
    Parameters:
    lista (list): la lista a filtrar
    valor_superior_igual (int): el valor a comparar
    
    Returns:
    list: la lista filtrada
    """
    lista_numeros = []

    for i in range(len(lista)):
        if lista[i] >= valor_superior_igual:
            lista_numeros += [lista[i]]

    return lista_numeros

def cargar_lista_aleatoria(numero:int, valor_desde:int , valor_hasta:int)->list:

    """
    Carga una lista con numeros aleatorios entre un rango
    determinado.

    Parameters:
    numero (int): La cantidad de elementos de la lista.
    valor_desde (int): El valor desde el cual se empieza a
        generar los numeros aleatorios.
    valor_hasta (int): El valor hasta el cual se generan los
        numeros aleatorios.

    Returns:
    list: La lista con los numeros aleatorios.
    """
    lista_random = []
    
    for _ in range(numero):
        lista_random += [random.randint(valor_desde,valor_hasta)]    
    
    return lista_random

def contar_numeros_pares(lista:list)->int:

    """
    Contador de elementos en una lista que son pares.

    Parameters:
    lista (list): la lista a contar

    Returns:
    int: la cantidad de elementos en la lista que son pares
    """
    contador = 0

    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            contador += 1 

    return contador

def cargar_palabras_en_lista(mensaje:str, cantidad:int)->list:
    '''
    La funcion carga strings en una lista
    Recibe un mensaje con lo que se pide y la cantidad de elementos de la lista
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    
    lista = []
    
    for _ in range(cantidad):
        nombre_ingresado = input(mensaje)
        lista += [nombre_ingresado]
        
    return lista

def contar_caracteres(lista:list, cantidad:int)->int:
    """
    Contador de elementos en una lista que tienen una cantidad determinada de caracteres
    
    Parameters:
    lista (list): la lista a contar
    cantidad (int): la cantidad de caracteres a comparar
    
    Returns:
    int: la cantidad de elementos en la lista que tienen una cantidad determinada de caracteres
    """
    contador = 0
    for elemento in lista:
        if len(elemento) >= cantidad:
            contador += 1
            
    return contador

def cargar_lista_enteros(mensaje:str, cantidad:int)->list:
    '''
    La funcion carga enteros en una lista
    Recibe un mensaje con lo que se pide y la cantidad de elementos de la lista
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    
    lista = []
    
    for _ in range(cantidad):
        entero_ingresado = int(input(mensaje))
        lista += [entero_ingresado]
        
    return lista

def mostrar_lista(lista:list)->None:
    """
    Muestra los elementos de una lista.

    Parameters:
    lista (list): la lista a mostrar
    """
    for elem in lista:
        print(elem)

def cargar_lista_enteros_por_teclado(mensaje:str, valor_break)->list:
    '''
    La funcion carga enteros en una lista
    Recibe un mensaje con lo que se pide y la cantidad de elementos de la lista
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    
    lista = []
    
    while True:
        numero = input(mensaje)
        if numero == valor_break:
            break

        lista += [int(numero)]

    return lista

def cargar_lista(mensaje:str, cantidad:int, tipo:type)->list:
    '''
    La funcion carga datos en una lista con el tipo especificado
    Recibe un mensaje con lo que se pide, la cantidad de elementos de la lista y el tipo de dato
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    
    lista = []

    for _ in range(cantidad):
        valor_ingresado = input(mensaje)

        valor_ingresado = tipo(valor_ingresado)


        lista += [valor_ingresado]
        
    return lista

def calcular_promedio(lista:list)->float|None:
    '''
    La funcion recibe una lista y calcula el promedio, si está vacia devuelve None
    '''
    if len(lista) == 0:
        promedio = None
    else:
        acumulador = 0

        for element in lista:
            acumulador += element

        promedio = acumulador / len(lista)

    return promedio

def contar_superen_promedio (lista:list,promedio:float)->int:
    """
    Contador de elementos en una lista que son superiores a un promedio

    Parameters:
    lista (list): la lista a contar
    promedio (float): el promedio a comparar

    Returns:
    int: la cantidad de elementos en la lista que son superiores al promedio
    """
    contador = 0 

    for elemento in lista:
        if elemento > promedio:
            contador +=1
    return contador

def identificar_valor_maximo(lista:list)->int|None:
    """
    Retorna None cuando se produjo un error o la lista está vacía, caso contrario retorna el valor máximo
    """
    numero_mayor = None 

    for i in range (len(lista)):

        if(numero_mayor == None or lista[i] > numero_mayor):
            numero_mayor = lista[i]

    
    return numero_mayor

def identificar_valor_minimo (lista:list)->int|None:
    """
    Retorna None cuando se produjo un error o la lista está vacía, caso contrario retorna el valor mínimo
    """
    numero_menor = None 

    for i in range (len(lista)):

        if(numero_menor == None or lista[i] < numero_menor):
            numero_menor = lista[i]

    
    return numero_menor

def posicion_numero_minimo(lista:list, numero_menor:int)->list:
    """
    Retorna una lista con las posiciones en las que se encuentra el número mínimo en la lista

    Parameters:
    lista (list): la lista que contiene el número
    numero_menor (int): el número que se busca

    Returns:
    list: una lista con las posiciones en la que se encuentra el número
    """
    lista_indice = []
    for i in range(len(lista)):
        if lista[i] == numero_menor:
            lista_indice += [i]
    return lista_indice

def determinar_repetidos(lista:list, valor:int)->int:
    """
    Cuenta la cantidad de veces que se repite un valor en una lista

    Parameters:
    lista (list): la lista que contiene el valor
    valor (int): el valor que se busca

    Returns:
    int: la cantidad de veces que se encuentra el valor en la lista
    """
    contador = 0
    for elemento in lista:
        if elemento == valor:
            contador += 1
    return contador

def cargar_listas_paralelas(cantidad:int, mensaje_a:str, mensaje_b:str, lista_a:list, lista_b:list)->list:
    
    """
    Carga una cantidad determinada de nombres y edades en dos listas paralelas.
    
    Args:
        cantidad (int): Cantidad de nombres y edades a cargar.
        mensaje_a (str): Mensaje a mostrar para pedir el nombre.
        mensaje_b (str): Mensaje a mostrar para pedir la edad.
        lista_a (list): Lista de nombres.
        lista_b (list): Lista de edades.
    
    Returns:
        list: Una lista con los nombres y otra con las edades, ambas de igual longitud.
    """
    for _ in range (cantidad):
        valor_a = input(mensaje_a)
        valor_b = input(mensaje_b)
        lista_a += [valor_a]
        lista_b += [valor_b]
    return lista_a, lista_b

def mostrar_mayores(lista_a, lista_b, valor_b)->None:

    """
    Muestra los nombres en la lista_a que tienen una edad en la lista_b mayor o igual a valor_b.

    Parameters:
    lista_a (list): lista de nombres
    lista_b (list): lista de edades
    valor_b (int): edad a comparar
    """
    for i in range(len(lista_b)):
        if int(lista_b[i]) >= valor_b:
            print(lista_a[i])

def contar_mayor_que_primero(lista:list)->int:
    """
    Contador de elementos en una lista que son superiores al primer elemento
    
    Parameters:
    lista (list): la lista a contar
    
    Returns:
    int: la cantidad de elementos en la lista que son superiores al primer elemento
    """
    contador = 0
    for i in range(len(lista)):
        if i == 0:
            primer_valor = lista[i]
        elif lista[i] > primer_valor:
            contador += 1
    return contador

def sumar_listas (lista_a:list, lista_b: list) -> list:
    """
    Suma los elementos de dos listas y devuelve una nueva lista con los resultados
    
    Parameters:
    lista_a (list): la primera lista
    lista_b (list): la segunda lista
    
    Returns:
    list: una lista con la suma de los elementos de las dos listas
    """
    lista_c = []
    for i in range(len(lista_a)):
        lista_c += [int(lista_a[i]) + int(lista_b[i])]
    return lista_c
