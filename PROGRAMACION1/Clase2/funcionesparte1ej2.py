'''2. Crear una función que verifique si un número dado por argumento es par o impar. lLa función debe imprimir un mensaje indicando si el número es par o impar.'''

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


"""5"""

def verificar_par_impar(numero = int) -> bool:
    
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

verificacion = verificar_par_impar(7)

print(verificacion)


'''3'''

def validar_entero():
    numero = input("Por favor, ingrese un número entero: ")
    
    while not numero.isdigit():
        numero + input("REINGRESE UN NUMERO ENTERO: ")

    numero = int(numero)

    return numero

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

print(encontrar_maximo(3,2,1))

# 1 1 1
#2 2 1
#2 1 2
#1 2 2

#1 1 2
#1 2 1
#2 1 1

#1 2 3
#1 3 2
#2 1 3
#2 3 1
#3 1 2
#3 2 1

'''def funcion(num1, num2, num3):
    """Encontrar el numero maximo"""
    maximo = num1
    if num2 > maximo:
        maximo = num2
    if num3 > maximo:
        maximo = num3
    return maximo

print(funcion(3, 1, 2))
'''
