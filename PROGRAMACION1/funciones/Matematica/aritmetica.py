def sumar(operando1,operando2):
    """ 
        Summary:

        Suma dos operadores

        Args: 
        operando1 (int): Numero
        operando2 (int): Numero

        Returns: 
        int: Devuelve el resultado de la suma
        """
    return operando1+operando2

def restar(operando1,operando2):
    """ 
        Summary:

        Resta dos operadores

        Args: 
        operando1 (int): Numero
        operando2 (int): Numero

        Returns: 
        int: Devuelve el resultado de la resta
        """
    return operando1-operando2

def multiplicacion(operando1,operando2):
    """ 
        Summary:

        Multiplicacion dos operadores

        Args: 
        operando1 (int): Numero
        operando2 (int): Numero

        Returns: 
        int: Devuelve el resultado de la multiplicacion
        """
    return operando1*operando2

def division(operando1, operando2):
    """ 
        Summary:

        division dos operadores

        Args: 
        operando1 (int): Numero
        operando2 (int): Numero

        Returns: 
        int: Devuelve el resultado de la division
        """
    resultado = 0
    if(operando2 != 0):
        resultado = operando1 / operando2
    return resultado

