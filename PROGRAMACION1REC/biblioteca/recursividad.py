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