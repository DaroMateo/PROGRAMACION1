"""import aritmetica
from aritmetica import potencia, sumar,restar"""

from funciones.Matematica.aritmetica import *
from funciones.Matematica.calculo import *

"""from Matematica import aritmetica
from Matematica import calculo"""



print(potencia(4,3))

print(sumar(2,5))
print(restar(2,5))




'''import matematica.aritmetica'''

'''print(matematica.aritmetica.sumar(2,5))'''

'''from matematica.aritmetica import 
from matematica.calculo import *'''



#print(potencia(2,16))

'''print(sumar(2,5))
print(restar(2,5))
print(multiplicar(2,5))
print(potencia(2,5))

'''
'''from aritmetica import sumar, restar

#print(potencia(2,16))

print(sumar(2,5))
print(restar(2,5))'''

'''import aritmetica

#print(potencia(2,16))

print(aritmetica.sumar(2,5))
print(aritmetica.restar(2,5))'''



#Factorial cantidad de posibilidades segun el numero natural

#3! = 3*2*1
#4! = 4*3*2*1

#Excluye el 4
"""def calcularfactorial(natural:int) -> int:
    resultado = 1

    for numero in range(1,natural+1): 
        resultado *= numero
    
    return resultado

print(calcularfactorial(4))"""

#De atras para adelante decreyente

"""def calcularfactorial(natural:int) -> int:
    resultado = 1

    for numero in range(natural-1, 0,-1): 
        resultado *= numero
    
    return resultado

print(calcularfactorial(4))"""

#si pongo 0

def calcularfactorial(natural:int) -> int:
    """
    Summary:
    Esta funcion toma un numero natural y realiza la operacion factorial
    
    Args:
    natural(int): se debe ingresar un numero
    
    Returns:
    int: Devuelve resultado. En caso de un Arg negativo retornara como error -999
    """
    resultado = 1
    if natural>= 0:
        for numero in range(natural, 0, -1): 
          resultado *= numero
    else:
       resultado = -999
    return resultado

print(calcularfactorial(-1))