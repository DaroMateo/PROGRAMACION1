"""
Desarrollar función calcular_fibonacci.
Parámetros: La misma recibirá un número entero (int) mayor o igual a cero (0).
Funcionalidad: La función deberá calcular el número n-ésimo en la sucesión de Fibonacci.
Si n = 0, deberá devolver 0.
Si n = 1, deberá devolver 1.
Para cualquier n > 1, el resultado será la suma de los dos números anteriores de la secuencia.
Retorno: El resultado calculado previamente.
Por ejemplo:
● f 0 = 0
● f 1 = 1
● f 2 = 1
● f 3 = 2
● f 4 = 3
● f 5 = 5
● f 6 = 8
"""
def calcular_fibonacci(numero:int)->int:
    
    """
    Calcula el n-ésimo número en la sucesión de Fibonacci.
    
    Parámetros:
    numero (int): Número entero mayor o igual a cero (0) para calcular el n-ésimo número en la sucesión.
    
    Retorna:
    int: El resultado calculado previamente. Si el parámetro es menor o igual a 2, se devuelve el mismo valor.
    
    Ejemplos:
    >>> calcular_fibonacci(0)
    0
    >>> calcular_fibonacci(1)
    1
    >>> calcular_fibonacci(2)
    1
    >>> calcular_fibonacci(3)
    2
    >>> calcular_fibonacci(4)
    3
    >>> calcular_fibonacci(5)
    5
    >>> calcular_fibonacci(6)
    8
    """

    if numero <=2:
        resultado = numero
    else:
        resultado = (calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2))

    return resultado

#print(calcular_fibonacci(7))

"""Desarrollar función mostrar_serie_fibonacci.
Parámetros: La misma recibirá un número entero (int) mayor o igual a cero (0).
Funcionalidad: La función deberá mostrar la secuencia completa hasta el número n-ésimo en la sucesión de
Fibonacci, incluyendo a este último.
Retorno: None
"""
def mostrar_serie_fibonacci(numero:int)->None:
    """
    Muestra la secuencia completa hasta el número n-ésimo en la sucesión de Fibonacci, incluyendo a este último.
    
    Parámetros:
    numero (int): Número entero mayor o igual a cero (0) que indica la cantidad de términos a mostrar en la
                  sucesión de Fibonacci.
    
    Retorna:
    None
    """
    for i in range(numero + 1):
        print(calcular_fibonacci(i))

#print(mostrar_serie_fibonacci(10))


"""Desarrollar función determinar_suma_consecutiva.
Parámetros: La misma recibirá un número entero (int), y cualquier otro parámetro que considere necesario.
Funcionalidad: Deberá determinar si el número ingresado como parámetro se puede obtener con la suma
de dos (2) números consecutivos anteriores.
Retorno:
True si el número se puede obtener de la suma de números consecutivos anteriores.
False si el número NO se obtiene de la suma de números consecutivos anteriores.
"""
def determinar_suma_consecutiva(numero:int, x=1)->bool:
    
    """
    Determina si el número ingresado como parámetro se puede obtener con la suma
    de dos (2) números consecutivos anteriores.
    
    Parámetros:
    numero (int): Número entero mayor o igual a cero (0) que se quiere determinar si se puede obtener con la sumade dos (2) números consecutivos anteriores.
    x (int): Número entero que representa el primer número de la suma de dos (2) números consecutivos anteriores.Por defecto es 1.
    
    Retorna:
    bool: True si el número se puede obtener de la suma de números consecutivos anteriores.
          False si el número NO se obtiene de la suma de números consecutivos anteriores.
    """
    # dos numeros consecutivos
    if x >= numero:
        resultado = False
    elif x + (x + 1) == numero:
        resultado = True
    else:
        resultado = determinar_suma_consecutiva(numero, x + 1)
    return resultado

    #3 numeros consecutivos
    """if x >= numero:
        resultado = False
    elif x + (x + 1) + (x+2) == numero:
        resultado = True
    else:
        resultado = determinar_suma_consecutiva(numero, x + 1)
    return resultado"""

    #4 numeros consecutivos
    """if x >= numero:
        resultado = False
    elif x + (x + 1) + (x+2) + (x+3) == numero:
        resultado = True
    else:
        resultado = determinar_suma_consecutiva(numero, x + 1)
    return resultado"""

    #5 numeros consecutivos
    """if x >= numero:
        resultado = False
    elif x + (x + 1) + (x+2) + (x+3) + (x+4) == numero:
        resultado = True
    else:
        resultado = determinar_suma_consecutiva(numero, x + 1)
    return resultado"""

    
print(determinar_suma_consecutiva(5))
