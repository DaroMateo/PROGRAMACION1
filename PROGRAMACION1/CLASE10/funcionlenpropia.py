from os import system

def contar_caracteres (variable:str)->int:
    """
    Cuenta la cantidad de caracteres de un string
    
    Parameters:
    variable (str): el string a contar
    Returns:
    int: la cantidad de caracteres en el string
    """
    contador = 0
    for letra in variable:
        contador  = contador + 1

    return contador


#print(contar_caracteres(nombre))
system("cls")

print(chr(ord('A')+32))

print(ord('A'))

print(chr(97))

print(97-65)
nombre = "chilindrina"

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

nombre = capitalizar(nombre)

print(nombre)

# ENTRE(mayuscula) 65 - 90 Y ENTRE (minuscula) 97 - 122
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

print(convertir_mayuscula(nombre))




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

print(convertir_minuscula(nombre))
