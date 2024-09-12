import random
def listar(lista1:list, lista2:list, lista3:list): #se debe pasar 3 listas
    """ 
    Summary:

    Listar

    Args: 
    lista1 (list): lista 1
    lista2 (list): lista 2
    lista3 (list): lista 3

    Returns: 
    list: informa los datos de la lista
    """
    for i in range(len(lista1)):
        if lista1[i] != "LIBRE":
            mostrar(lista2, lista3, i)
            """print(lista[i])"""  

def mostrar(lista:list, lista1:list, indice:int): #2 listas + indice
    """ 
    Summary:

    Listar

    Args: 
    lista (list): lista 1
    lista1 (list): lista 2
    indice (int): indice de la lista

    Returns: 
    list: informa los datos de la lista
    """
    print(f"{lista[indice]}, {lista1[indice]}")  


def buscar(lista:list,dato:str)-> int:
    """
    Summary:

    Busca un dato en una lista.

    Args:
    lista (list): lista
    dato (str): dato de la lista

    Returns:
    Si lo encuentra retorna el indice.
    Si no lo encuentra retorna -1
    """
    retorno = -1
    for i in range(len(lista)):
        if dato == lista[i]:
            retorno = i
            break
    return retorno

def validar_respuesta(rta:str)-> bool:
    """
    Summary:

    Valida la respuesta.

    Args:
    rta (str): valida si "S" o "s" o "N" o "n"

    Returns:
    devuelve un valor booleano
    """
    retorno = False
    if rta == "S" or rta == "s" or rta=="N" or rta == "n":
        retorno = True
    return retorno

def alta(mensaje:str):
    """
    Summary:

    ALTA

    Args:
    mensaje (str): mensaje

    Returns:
    Mensaje
    """
    dato = input(mensaje)
    return dato

def buscar_libre(lista:list,libre:str)->int:
    """
    Summary:

    Busca espacio libre en la lista

    Args:
    lista (list): lista
    libre (str): busca espacio libre

    Returns:
    devuelve un valor entero
    """
    retorno=-1
    for i in range(len(lista)):
        if lista[i] == libre:
            retorno=i
            break
    return retorno

def lista_vacia(lista:list,libre:str)->bool:
    """
    Summary:

    Lista vacia

    Args:
    lista (list): lista
    libre (str): espacio libre

    Returns:
    devuelve un valor boleano
    """
    retorno=True
    for i in range(len(lista)):
        if lista[i]!=libre:
            retorno=False
            break
    return retorno

def swap(lista, indice_uno, indice_dos):
    """
    Summary:

    Intercambia dos valores de una lista

    Args:
    lista (list): lista
    indice_uno (int): primer indice
    indice_dos (int): segundo indice

    Returns:
    lista intercambiada

    """
    
    aux = lista[indice_uno]
    lista[indice_uno] = lista[indice_dos]
    lista[indice_dos] = aux
    return lista

def ordenar_array(lista:list, criterio:str = "ASC")-> list:
    """Ordena Array segun criterio

    Args:
        lista (list): lista
        criterio (str): ASC o DESC

    Returns:
        list: Ordenada segun criterio
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if criterio == "ASC" and lista[i] > lista[j] or criterio == "DESC" and lista[i] < lista[j]:
                    swap(lista, i, j)
    return lista

def ordenar_lista_ascendente(lista:list)-> list: 
    """Ordena lista

    Args:
        lista (list): Ascendente

    Returns:
        list: Lista ordena
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    return lista

def buscar_indice(lista, numero):
    """
    Encuentra el índice de un número dado en una lista.

    Args:
        lista (list): La lista para buscar el número.
        numero (int): El número para encontrar el índice.

    Returns:
        int: el índice del número en la lista, o -1 si no se encuentra el número
    """
    retorno = -1
    for i in range(len(lista)):
        if numero == lista[i]:
            retorno = i
    return retorno

def crear_lista_numeros_random(tope):
    """
    Genera una lista de números aleatorios dentro del rango [0, 99] de la longitud especificada.

    Parameters:
        tope (int): La longitud de la lista que se generará.
    Returns:
        list: Una lista de números aleatorios dentro del rango [0, 99] de la longitud especificada.
    """
    numeros = []
    for i in range (tope):
        numeros.append(random.randint(0, 99))

    return numeros

def sumar_elementos_lista(lista):
    """
    Calcula la suma de todos los elementos de una lista determinada.
    Parameters:
    lista (lista): La lista de números a sumar.
    Returns:
    int: la suma de todos los elementos de la lista.
    """
    acumulador = 0
    for i in range(len(lista)):
        acumulador += lista[i]
    return acumulador

def calcular_promedio(lista):
    """
    Calcula el promedio de una lista determinada de números.
    Parameters:
    lista (lista): una lista de números.
    Returns:
    float: el promedio de los números de la lista. Si la lista está vacía, devuelve 0.
    """
    promedio = 0
    acumulador = sumar_elementos_lista(lista)
    if len(lista) > 0:
        promedio = acumulador / len(lista)
    
    return promedio

def buscar_num_min(lista):
    """
    Encuentra el número mínimo en una lista determinada.
    Parameters:
    - lista (list): La lista de números para buscar.
    Returns:
    - int: el número mínimo en la lista.
    """
    numero_min = lista[0]
    for i in range(len(lista)):
        if lista[i] < numero_min:
            numero_min = lista[i]
    return numero_min