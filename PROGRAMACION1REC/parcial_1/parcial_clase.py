import random
from os import system

def generar_lista_random_alfanumerica(cantidad:int)->list:
    lista = []
    for i in range(cantidad):
        caracter = chr(random.randint(48,90))
        while ord(caracter) < 65 and ord(caracter) > 57:
            caracter = chr(random.randint(48,90))

        lista += [caracter]
           
    return lista


def ordenar_lista(lista:list, criterio:str = "asc")->bool:
    flag = False
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if (criterio == "asc" and lista[i] > lista[j]) or (criterio == "dsc" and lista[i] < lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                flag = True
    return flag

'''
def contador_caracteres(lista:list, caracter:str):
    conteo = [0] * 26  # 26 letras en el alfabeto
    # Contar cada carácter en la lista
    for caracter in lista:
        if 'A' <= caracter <= 'Z':  # Verificar si el carácter es una letra mayúscula
            indice = ord(caracter) - ord('A')  # Calcular el índice correspondiente
            conteo[indice] += 1
    
    return conteo
'''

def contar_caracteres(lista:list):
    # Crear una lista de conteo para las letras de 'A' a 'Z'
    conteo = [0] * 26  # 26 letras en el alfabeto
    # Contar cada carácter en la lista
    for caracter in lista:
        if 'A' <= caracter <= 'Z':  # Verificar si el carácter es una letra mayúscula
            indice = ord(caracter) - ord('A')  # Calcular el índice correspondiente
            conteo[indice] += 1
    return conteo

def mostrar_lista_paralela(lista_a, lista_b) -> None:
    """ 
    muestra lista paralelas
    retorna: None

    """
    for i in range(len(lista_a)):
        print(f"      {lista_a[i]} --> {lista_b[i]}")


def contador_de_caracteres(lista, caracteres):
    """ cuenta los caracteres de una lista 
        caracteres:conjuntos de elementos (list[str])
        retorna la lista con la cantidad de repetido
    """

    cantidad_repetidos = []

    for caracter in (caracteres):
        contador = 0
        for item in lista:
            if caracter == item:
                contador += 1
        cantidad_repetidos += [contador]
    mostrar_lista_paralela(caracteres,cantidad_repetidos)

    return cantidad_repetidos


def inicializar_matriz(cant_filas:int, cant_columnas:int)->list:
    matriz = []
    for _ in range(cant_filas):
        matriz += [[None] * cant_columnas]
    return matriz


def crear_matriz_aleatoria(cantidad_filas:int, cantidad_columnas:int, desde:int, hasta:int)->list:
    matriz = inicializar_matriz(cantidad_filas,cantidad_columnas)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = str(random.randint(desde, hasta))
    return matriz


def mostrar_matriz(matriz):
    """
    Muestra por pantalla una matriz de enteros, con los elementos alineados en columnas.
    
    Parameters:
    matriz (list): La matriz a mostrar.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print(" ")


def validar_numero_entero(cadena:str)->bool:
    flag = True
    for num in cadena:
        if num < "0" or num > "9":
            flag = False
    return flag


def largo_cadena(cadena:str)->int:
    contador = 0
    for _ in cadena:
        contador += 1
    return contador


"""
def contar_caracteres( lista:list, caracter:str)->int:
    '''
    La funcion cuenta cuantas veces aparece un caracter en una lista determinada
    :param lista: Recibe una lista a recorrer
    :param caracter: Recibe un caracter para buscar
    :return: Retorna el numero de veces que se encuentra el caracter
    '''
    contador = 0
    for i in range(len(lista)):
        if lista[i] == caracter:
            contador += 1

    return contador
"""

def identificar_valor_maximo_y_minimo(lista:list)->None:
    '''
    La funcion busca cual es el caracter que se repite mas y menos veces
    :param lista: Recibe como parametro una lista
    :return: No retorna nada ya que muestra su resultado por pantalla
    '''
    numero_menor = None
    numero_mayor = None
    for i in range(len(lista)):
        caracter = lista[i]
        if ord(lista[i]) > 64 and ord(lista[i]) < 91:
            cantidad = contar_caracteres(lista, caracter)

# 4 # Mejorar
def buscar_valor_minimo_y_maximo(lista:list)->None:
    """
    recibe una lista por parametro
    Se busca caracter mayor 
    retorna la lista
    """
    caracter = ""
    contador_mayor = None
    caracter_mayor = ""
    contador_menor = None
    caracter_menor = ""
    for i in range(26):
        contador = 0
        for j in range(len(lista)):
            if(lista[j]==chr(65+i)): 
                caracter=lista[j] 
                contador+=1
        if contador_mayor == None or contador > contador_mayor:
                contador_mayor = contador
                caracter_mayor = caracter
        if contador_menor == None or contador < contador_menor:
                contador_menor = contador
                caracter_menor = caracter
    print (f"{caracter_mayor}   {contador_mayor}")
    print (f"{caracter_menor}   {contador_menor}")
    return []


# Buscar secuencia numerica en matriz
def buscar_secuencia(matriz:list, secuencia:str)-> bool:
    resultado = False
    for i in range(len(matriz)):
        bandera_secuencia = False
        contador_secuencia = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] == secuencia[contador_secuencia]:
                if contador_secuencia < len(secuencia):
                    contador_secuencia += 1
                    bandera_secuencia = True
                if contador_secuencia == len(secuencia) and bandera_secuencia == True:
                    resultado = True
            else:
                bandera_secuencia = False
                contador_secuencia = 0
            if resultado == True:
                break

    if resultado == False:
        print(f"La secuencia numérica {secuencia} no existe en la matriz.")
    else:
        print(f"La secuencia numérica {secuencia} existe en la matriz.")
    return resultado


def mostrar_resultado_punto_3(conteo:int):
    print("CARACTER | CANTIDAD")
    print("---------+---------")
    for i in range(26):
        cantidad = conteo[i]  
        caracter = chr(i + ord('A'))  
        print(f"    {caracter}    |    {cantidad}")


def buscar_valor(matriz:list,valor:int)-> bool:
    """busca el valor dado en la fila de la matriz dada

    Args:
        matriz (list): matriz donde buscar valor
        valor (int): valor que desea allar

    Returns:
        bool: Devuelve True si el valor esta en la matriz, caso contrario false
    """
    resultado = False
    for fila in (matriz):
        if valor in fila:
            resultado = True
    return resultado


def menu_4_case(mensaje_a:str,mensaje_b:str,mensaje_c:str,mensaje_d:str="",mensaje_e:str="",mensaje_f:str="",mensaje_g:str="")->str:
    """Menu basico pseudo generico

    Args:
        mensaje_a (str): Primera opcion del menu
        mensaje_b (str): Segunda
        mensaje_c (str): Tercera
        mensaje_d (str, optional): Cuarta opcion / opcional. Defaults to "".
        mensaje_e (str, optional): Quinta opcion / opcional. Defaults to "".
        mensaje_f (str, optional): sexta opcion / opcional. Defaults to "".
        mensaje_g (str, optional): septima opcion / opcional. Defaults to "". 

    Returns:
        str: Pregunta al usuario para elegir opcion del menu
    """
    limpiar_pantalla()
    print("")
    print("   -------Menu de opciones-------   ")
    print(mensaje_a)
    print(mensaje_b)
    print(mensaje_c)
    print(mensaje_d)
    print(mensaje_e)
    print(mensaje_f)
    print(mensaje_g)
    return input("Ingrese opcion: ")


def limpiar_pantalla():
    """limpia la pantalla de menu para mejor calidad visual"""
    system("cls")

def pausar():
    """Permite pausar el programa para poder ver los print de este"""
    system("pause")


# 7
def confirmar_salir(confirmacion:str)->bool:
    """ espera la confirmacion de salida con "si" o "no

    Args:
        confirmacion (str): imput con la confirmacion de

    Returns:
        bool: retorna true si la confimacion es "si", caso contrario retorna False
    """
    resultado = False
    while confirmacion != "si" and confirmacion != "no":
        confirmacion = input("Error, Elija solamente ['si' o 'no']: ")
    if confirmacion == "si":
        resultado = True
    return resultado

def menu():
    flag = False
    flag_2 = False

    while True:
        match menu_4_case(
            "1- [Generar lista alfanumerica aleatoria]",
            "2- [Ordenar la lista alfanumérica generada]",
            "3- {Buscar e informar cuantas veces se repite cada uno de los caracteres alfabéticos A-Z]",
            "4- [Caracter mas repetido y menos repetido]",
            "5- [Generar matriz aleatoria]",
            "6- [Buscar secuencia numerica y informar]",
            "7- [Salir]"):
            case "1":
                lista_alfanumerica = generar_lista_random_alfanumerica(1000)
                flag = True
            case "2":
                if not flag:
                    print("No puede ordenar los datos si no genera una lista aleatoria!")
                else:
                    criterio = input("Ingrese criterio de ordenamiento: ")
                    while (criterio != "asc" and criterio != "dsc") and (criterio != "ASC" and criterio != "DSC"):
                        criterio = input("ERROR! Solo elegir 'asc' o 'dsc'. Ingrese criterio de ordenamiento: ")
                    ordenar_lista(lista_alfanumerica, criterio)
            case "3":
                if not flag:
                    print("ERROR! Primero debe generar la lista alfanumerica!")
                else:
                    conteo = contar_caracteres(lista_alfanumerica)
                    mostrar_resultado_punto_3(conteo)
            case "4":
                if not flag:
                    print("ERROR! Primero debe generar la lista alfanumerica!")
                else:
                    buscar_valor_minimo_y_maximo(lista_alfanumerica)
            case "5":
                matriz_aleatoria = crear_matriz_aleatoria(10, 10, 1, 10)
                flag_2 = True
            case "6":
                if not flag_2:
                    print("ERROR! Primero debe generar la matriz!")
                else:
                    print(matriz_aleatoria)
                    digit = input("Ingrese una secuencia numerica: ")
                    while not validar_numero_entero(digit):
                        digit = input("Ingrese una secuencia numerica: ")
                    busqueda_digito = buscar_secuencia(matriz_aleatoria, digit)
            case "7":
                opcion = input("Confirma que quiere salir?: ")
                resultado = confirmar_salir(opcion)
                if resultado:
                    break
        pausar()