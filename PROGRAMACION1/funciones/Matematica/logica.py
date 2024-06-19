def validar_entero(cadena:str):
    """ 
    Summary:

    Valida si es un numero entero

    Args: 
    cadena (int): Numero

    Returns: 
    int: Informa si es entero
    """
    retorno = False

    if cadena.isdigit():
        retorno = True

    return retorno

def es_par(numero:int) -> bool:
    '''
   Summary:
     VERIFICAR SI ES PAR O ES IMPAR
     NUMERO: -. INT
     RETURN: -> BOOL
   '''
    return( numero % 2 == 0)

def encontrar_maximo(a : int, b : int, c : int) -> int:
    """
    DEVUELVE UN ENTERO
    
    Args:
    a(int): se debe ingresar un numero
    b(int): se debe ingresar un numero
    c(int): se debe ingresar un numero
    
    Returns:
    int: Devuelve el valor maximo entre estos tres parametros
    """

    
    retorno = None

    if a == b and a == c:
        retorno = a
    else:
        if a > b and a > c:
            retorno = a

        elif b > c:
            retorno = b

        else:
            retorno = c
    return retorno

def verificar_par_impar(numero = int) -> bool:
    """
    Verifica si un número dado es par o impar.

    Args:
        numero (int):El número a comprobar.
    Returns:
        bool: Verdadero si el número es par, Falso si es impar.
    """

    
    retorno = False

    '''exclusion del 0, no es par ni impar'''
    if numero != 0:
        
        if numero < 0 :
            numero *= -1
        '''si el numero es negativo lo multiplico x menos 1'''    

        while numero > 1:
            numero -= 2

        if numero == 0:
            retorno = True
    
    return retorno

def es_par(numero:int) -> bool:
    '''
   Summary:
     VERIFICAR SI ES PAR O ES IMPAR
     NUMERO: -. INT
     RETURN: -> BOOL
   '''
    return( numero % 2 == 0)
par = es_par(1)
print(par)
