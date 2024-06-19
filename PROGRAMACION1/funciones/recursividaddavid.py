#Recursividad
#3
# un numero tiene limites, y ocupa muchos recursos
def factorial(natural):
    """
        Calcula el factorial de un número dado mediante recursividad.

        Parameters:
        natural (int): El número para el cual se va a calcular el factorial.

        Returns:
        int: El factorial del número dado.
    """
    if natural == 0:
        retorno =  1
    else:
        retorno = natural * factorial(natural - 1) 
    
    return retorno


print(factorial(3))