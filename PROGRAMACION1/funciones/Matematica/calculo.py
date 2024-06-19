def potencia(base:int ,exponente:int):
    """ 
    Summary:

    Recibe dos argumentos, base y exponente, calcula la potencia

    Args: 
    base (int): Numero
    exponenete (int): cuantas veces se multiplica la base

    Returns: 
    int: Devuelve el resultado de la base elevada a la potencia
    """
    if exponente == 0:
        resultado=1
    else:
        resultado = 1 

        for exponente in range(exponente):
           resultado *= base
    return resultado

#Factorial cantidad de posibilidades segun el numero natural

#3! = 3*2*1
#4! = 4*3*2*1

def calcular_factorial (natural:int) -> int:
    """
    Summary:
    Esta funcion toma un numero natural y realiza la operacion factorial.
    
    Args:
    natural (int): Numero natural >= 0.
    
    Returns:
    int: Devuelve resultado. En caso de un argumento negativo retornara como error "-999".
    """
    resultado = 1

    if natural >= 0:
        for numero in range(natural, 0, -1):
            resultado *= numero
    else:
        resultado = -999
    return resultado


