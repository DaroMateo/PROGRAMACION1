def contar_caracteres (variable:str)->int:
    contador = 0
    for letra in variable:
        contador  = contador + 1

    return contador

def capitalizar (variable:str):
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
    Convierte una cadena determinada a minúsculas iterando sobre cada carácter y verificando si es una letra mayúscula.
    Si un carácter es una letra mayúscula, se convierte a su equivalente en minúscula utilizando los valores ASCII.
    Si un carácter no es una letra mayúscula, se agrega tal cual a la cadena minúscula resultante.
    
    Parameters:
        variable (str): La cadena que se va a convertir a minúsculas.
    
    Returns:
        str: La versión en minúscula de la cadena de entrada.
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
