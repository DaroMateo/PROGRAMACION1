def contar_caracteres (variable:str)->int:
    """
    Cuenta la cantidad de caracteres de un string
    
    Parameters:
    variable (str): el string a contar
    Returns:
    int: la cantidad de caracteres en el string
    """
    contador = 0
    for _ in variable:
        contador  = contador + 1

    return contador

def capitalizar (variable:str):
    """
    Convierte el primer caracter de un string a mayuscula y mantiene el resto del string igual
    
    Parameters:
    variable (str): el string a capitalizar
    Returns:
    str: el string capitalizado
    """
    cantidad = contar_caracteres(variable)
    if ord(variable[0]) >= 97 and ord(variable[0]) <= 122:
        for i in range (cantidad):
            if i == 0 :
                inicial = chr(ord(variable[i])-32)
                #print(inicial) 
                retorno = inicial
            else:
                retorno += variable[i]
    else:
        retorno = variable
    return retorno


def convertir_mayuscula (variable:str):
    """
    Convierte todos los caracteres de un string a mayuscula
    
    Parameters:
    variable (str): el string a convertir
    Returns:
    str: el string convertido a mayuscula
    """
    cantidad = contar_caracteres(variable)
    mayuscula = ''
    for i in range (cantidad):
        if ord(variable[i]) >= 97 and ord(variable[i]) <= 122:
            letra = chr(ord(variable[i])-32)
            mayuscula += letra
        else:
            mayuscula += variable[i]
    
    return mayuscula

def convertir_minuscula (variable:str):
    """
    Convierte todos los caracteres de un string a minuscula
    
    Parameters:
    variable (str): el string a convertir
    Returns:
    str: el string convertido a minuscula
    """
    cantidad = contar_caracteres(variable)
    minuscula = ''
    for i in range (cantidad):
        if ord(variable[i]) >= 65 and ord(variable[i]) <= 90:
            letra = chr(ord(variable[i])+32)
            minuscula += letra
        else:
            minuscula += variable[i]
        
    return minuscula

def ordenar_por_largo(lista):
    # Crear una copia de la lista para no modificar la original
    """
    Ordena una lista de cadenas por su largo de menor a mayor utilizando el algoritmo de ordenamiento por burbuja.
    
    Parameters:
    lista (list): la lista de cadenas a ordenar
    Returns:
    list: la lista ordenada por su largo
    """
    lista_copia = lista[:] 
    
    lista_ordenada = len(lista_copia)
    for i in range(lista_ordenada):
        for j in range(0, lista_ordenada - i - 1): # n-i-1 porque ya se han ordenado los primeros i elementos
            if len(lista_copia[j]) > len(lista_copia[j + 1]):
                aux = lista_copia[j]
                lista_copia[j] = lista_copia[j + 1]
                lista_copia[j + 1] = aux
    
    return lista_copia

def ordenar_cadenas(lista:list) -> list:
    """
    Ordena una lista de cadenas por su largo de menor a mayor.
    
    Parameters:
    lista (list): la lista de cadenas a ordenar
    Returns:
    list: la lista ordenada por su largo
    """
    lista_ordenada = []
    largo_maximo = len(lista[0])
    for cadena in lista:
        if len(cadena) > largo_maximo:
            largo_maximo = len(cadena)
    contador = 0
    cantidad_caracteres = 0
    while contador <= largo_maximo:
        for cadena in lista:
            if len(cadena) == cantidad_caracteres:
                lista_ordenada += [cadena]
        cantidad_caracteres += 1
        contador += 1
    return lista_ordenada

def determinar_cantidad_de_palabras(cadena):
    """
    determina la cantidad de palabras de una cadena de caracteres.
    
    Parameters:
    cadena (str): la cadena de caracteres a analizar.
    Returns:
    int: la cantidad de palabras encontradas en la cadena.
    """
    contador = 1
    if len(cadena) != 0:
        for _ in range(len(cadena)):
            if cadena[_] == ' ':
                contador += 1
    else:
        contador = 0
    return contador