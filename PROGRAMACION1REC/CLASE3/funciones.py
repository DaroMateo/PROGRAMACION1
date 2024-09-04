#1) Desarrollar una función que determine si un número entero es par o impar. Debe recibir un número por
#parámetro y devolver True en caso de que sea par, de lo contrario devolverá False.

def determinar_par_impar (numero:int)->bool:
    """
    Determina si un numero entero es par o impar

    Parameters
    ----------
    numero : int
        El numero a evaluar

    Returns
    -------
    bool
        True si el numero es par, False si es impar
    """
    retorno = False
    if (numero%2)==0:
        retorno = True
    else:
        retorno = False
    return retorno

#2) Desarrollar una función que reciba un carácter y determine si ese carácter está comprendido entre a...z o
#A...Z, en caso afirmativo devolverá True, de lo contrario False.
def determinar_letra (letra:str)->bool:
    """
    Determina si una letra es mayuscula o minuscula

    Parameters
    ----------
    letra : str
        La letra a evaluar

    Returns
    -------
    bool
        True si la letra es mayuscula, False si es minuscula
    """
    retorno = False
    #if (ord(letra)>=65 and ord(letra)<=90) or (ord(letra)>=97 and ord(letra)<=122):
    if (letra>= 'A' and letra<= 'Z') or (letra>= 'a' and letra<= 'z'):
        retorno = True
    else:
        retorno = False
    return retorno

def convertidor_de_mayuscula(letra:str)->str:
    """
    Convierte una letra a mayúscula

    Parameters
    ----------
    letra : str
        La letra a convertir

    Returns 
    -------
    str
        La letra convertida a mayúscula
    """

    if (letra>= 'a' and letra<= 'z'):
        letra = chr(ord(letra)-32)
    return letra
    

#3) Desarrollar una función que reciba un carácter y determine si ese carácter está comprendido entre 0...9,
#devolverá un valor boolean indicando si el carácter recibido es numérico o no.

def determinar_digito (caracter:str)->bool:
    """
    Determina si una caracter es digito

    Parameters
    ----------
    caracter : str
        La caracter a evaluar

    Returns
    -------
    bool
        True si la caracter es digito, False si no lo es
    """
    retorno = False
    #if caracter >= '0' and caracter <= '9':
    if (ord(caracter)>=48 and ord(caracter)<=57):
        retorno = True
    return retorno

#4) Desarrollar una función que permita validar un número entero. Deberá recibir por parámetro el número a
#validar, y dos números que representan el rango mínimo y máximo permitido. Devolverá True en caso de
#ser válido, False de lo contrario.
def determinar_min_max(numero:int, min:int, max:int)->bool:
    """
    Determina si un numero es mayor o menor a un minimo y maximo

    Parameters
    ----------
    numero : int
        El numero a evaluar
    min : int
        El minimo permitido
    max : int
        El maximo permitido

    Returns
    -------
    bool
        True si el numero es mayor o igual al minimo y menor o igual al maximo, False de lo contrario
    """
    retorno = False
    if (numero>=min and numero<=max):
        retorno = True
    return retorno

#5)Desarrollar una función que se encargue de solicitar un número entero al usuario, validarlo (reutilizando la
#función del punto anterior) y retornar el número validado y transformado a entero. Deberá recibir por
#parámetro un mensaje que se le mostrará al usuario y los rangos de validación.
def determinar_si_es_cadena_numerica(cadena:str)->bool:
    """
    Determina si una cadena es numerica

    Parameters
    ----------
    cadena : str
        La cadena a evaluar

    Returns
    -------
    bool
        True si la cadena es numerica, False de lo contrario
    """
    bandera = True
    for num in cadena:
        if determinar_digito(num) != True:
            bandera = False
            break
    return bandera
    
def solicitar_entero(mensaje:str, min:int, max:int)->int:
    """
    Valida un numero entero

    Parametro
    ----------
    mensaje : str
        El mensaje que se mostrara al usuario
    min : int
        El minimo permitido
    max : int
        El maximo permitido

    Retorno
    -------
    int
        El numero validado
    """
    numero = input(mensaje)
       
    while determinar_si_es_cadena_numerica(numero) != True: # esta hace que la cadena no sea numerica
        numero = input(mensaje)
    
    numero = int(numero)
    while determinar_min_max (numero, min, max) != True: #esta hace que el numero no este dentro del rango
        if determinar_min_max (numero, min, max) == False: # esta hace que el numero no este dentro del rango
            numero = input(mensaje)
            while determinar_si_es_cadena_numerica(numero) != True: # esta hace que la cadena no sea numerica
                numero = input(mensaje)
            numero = int(numero)
    return numero
"""echo por el profe mas simplificado"""
    #numero = min -1
    #while determinar_min_max (numero, min, max) == False:
    #    numero = input(mensaje)
    #    while determinar_si_es_cadena_numerica(numero) != True:
    #        numero = input(mensaje)
    #    numero = int(numero)
    #return numero

#print(solicitar_entero("ingrese un numero: ", 0, 10))

#6) Desarrollar una función que se encargue de solicitar una cadena de caracteres al usuario, validarla y
#retornar la misma. Deberá recibir como parámetro un mensaje para indicarle al usuario y 1, 2 o 3 cadenas
#de caracteres que representarán las opciones válidas de ingreso.
def validar_cadena(mensaje:str, cadena_1:str, cadena_2:str = None, cadena_3:str = None)->str:
    """
    Valida una cadena de caracteres

    Parametro
    ----------
    mensaje : str
        El mensaje que se mostrara al usuario
    cadena_1 : str
        La cadena 1
    cadena_2 : str
        La cadena 2
    cadena_3 : str
        La cadena 3

    Retorno
    -------
    str
        La cadena validada
    """
    cadena_ingresada = input(mensaje)
    while cadena_ingresada != cadena_1 and cadena_ingresada != cadena_2 and cadena_ingresada != cadena_3:
        cadena_ingresada = input(mensaje)
    return cadena_ingresada


#print(validar_cadena("Ingrese un genero: ", "M", "F", "NB"))

#7) Desarrollar una función que se encargue de medir el largo de una cadena de caracteres, deberá recibir por
#parámetro la cadena de caracteres a evaluar y devolverá un número entero representando la longitud de
#la cadena recibida.
def largo_cadena(cadena:str)->int:
    """
    Calcula el largo de una cadena de caracteres

    Parameters
    ----------
    cadena : str
        La cadena de caracteres a evaluar

    Returns
    -------
    int
        El largo de la cadena
    """
    contador = 0
    for _ in cadena: # el _ es un placeholder, no se usa en este caso
        contador += 1
    return contador

print(largo_cadena("Hola Mundo"))


#8) Desarrollar una función que determine si un número que recibirá por parámetro es primo. Si es primo
#deberá devolver un True, de lo contrario False.
def es_primo(numero:int)->bool:
    """
    Determina si un numero es primo

    Parameters
    ----------
    numero : int
        El numero a evaluar

    Returns
    -------
    bool
        True si el numero es primo, False de lo contrario
    """
    for i in range(2,numero):
        if (numero%i==0):
            return False
    return True
#9) Desarrollar una función que recibirá un número entero por parámetro, y devolverá el resultado del
#factorial de ese número.
def factorial(numero:int)->int:
    """
    Calcula el factorial de un numero

    Parameters
    ----------
    numero : int
        El numero a evaluar

    Returns
    -------
    int
        El factorial del numero
    """
    resultado = 1
    for i in range(1,numero+1):
        resultado *= i
    return resultado
#10) Desarrollar una función que verifique el DNI de una persona, la misma recibirá una cadena de caracteres
#(se asume que solamente contiene caracteres numéricos). Si la cantidad de caracteres es menor a 6 o
#mayor a 8, retornara False. Si la cantidad de caracteres está comprendida entre 6 y 8 devolverá True.
def es_dni(cadena:str)->bool:
    """
    Determina si una cadena de caracteres es un dni

    Parameters
    ----------
    cadena : str
        La cadena de caracteres a evaluar

    Returns
    -------
    bool
        True si la cadena es un dni, False de lo contrario
    """
    for caracter in cadena:
        if not (caracter.isdigit()):
            return False
    return len(cadena)>=6 and len(cadena)<=8
#11) Desarrollar una función que complete el número de DNI de una persona. Recibirá una cadena de
#caracteres (se asume que solamente contiene caracteres numéricos), deberá medirla y completar con ceros
#a la izquierda hasta llegar a un total de 8 caracteres, y devolviendo la cadena resultante. Ej: Se ingresa
#“123456”, y devolverá “00123456”.
#12) Desarrollar una función que transforme una cadena de caracteres numérica a su equivalente en letras.
#Recibirá por parámetro la cadena a transformar y devolverá el resultado en letras. Ej: “987” ->
#"novecientos ochenta y siete". Como máximo tomar el número más grande de 3 dígitos.