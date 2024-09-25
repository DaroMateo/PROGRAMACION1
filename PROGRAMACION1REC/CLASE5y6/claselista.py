import random
# 1) Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

def sumar_enteros(lista:list)->int:
    total_suma = 0
    for i in range(len(lista)):
        total_suma += lista[i]
    return total_suma

#lista_1 = [1, 2, 3, 4, 5]
#print(f"La suma de los elementos de la lista es {sumar_enteros(lista_1)}")


# 2) Definir una lista que almacene los nombres de los primeros seis meses del año. Mostrar el primer y último elemento de la lista solamente.

#lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]

def mostrar_elemento(lista: list, indice:int, mensaje:str) -> None:
    print(f"{mensaje}: {lista[indice]}")

#print(mostrar_elemento(lista_meses, 0, "El primer mes es "))
#print(mostrar_elemento(lista_meses, -1))


# 3) Definir una lista que almacene como primer elemento el nombre de un alumno y en las dos siguientes sus
# notas. Imprimir luego el nombre y el promedio de las dos notas.

#lista_alumno = ["Tomás", 10, 4]

def mostrar_promedio(lista:list)-> None:
     print(f"Nombre del alumno: {lista[0]} y su promedio es {(lista[1] + lista[2])/2}")

#mostrar_promedio(lista_alumno)

# 4) Definir una lista con 7 elementos enteros. Contar cuántos de dichos valores almacenan un valor superior a 33.
#lista_enteros = [1, 5, 36, 78, 3, 11, 17]

def contador_mayores(lista:list, minimo:int)-> int:
    contador = 0
    for elemento in lista:
        if elemento > minimo:
            contador += 1
    return contador

#print(contador_mayores(lista_enteros, 15))

#5) Definir una lista con 7 elementos enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores a 5.

def filtrar_lista(lista:list, valor_superior_igual:int)->list:
    
    lista_numeros = []

    for i in range(len(lista)):
        if lista[i] >= valor_superior_igual:
            lista_numeros += [lista[i]]

    return lista_numeros



'''lista_cargada = cargar_lista(7, "Ingrese el numero ")
lista_filtrada = filtrar_lista(lista_cargada, 5)
mostrar_lista_formateada(lista_filtrada)'''

'''
#6) Definir y cargar una lista con 10 números enteros aleatorios (utilizar random), entre 1 y 10. Contar y mostrar por
#pantalla la cantidad de números pares'''

def cargar_lista_aleatoria(numero:int, valor_desde:int , valor_hasta:int)->list:

    lista_random = []
    
    for _ in range(numero):
        lista_random += [random.randint(valor_desde,valor_hasta)]    
    
    return lista_random


def contar_numeros_pares(lista:list)->int:

    contador = 0

    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            contador += 1 

    return contador



'''lista_aleatoria = cargar_lista_aleatoria(10, 1, 10)
cantidad_pares = contar_numeros_pares(lista_aleatoria)

print("la cantidad de numeros pares es: ", cantidad_pares)'''

# 7) Definir una lista que almacene los nombres de 4 personas. Contar cuántos de esos nombres tienen 5 o más
# caracteres.

def cargar_palabras_en_lista(mensaje:str, cantidad:int)->list:
    '''
    La funcion carga strings en una lista
    Recibe un mensaje con lo que se pide y la cantidad de elementos de la lista
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    
    lista = []
    
    for _ in range(cantidad):
        nombre_ingresado = input(mensaje)
        lista += [nombre_ingresado]
        
    return lista

def contar_caracteres(lista:list, cantidad:int)->int:
    contador = 0
    for elemento in lista:
        if len(elemento) >= cantidad:
            contador += 1
            
    return contador

# lista_nombres = cargar_palabras_en_lista("Ingrese un nombre: ", 4)

# cantidad_nombres = contar_caracteres(lista_nombres, 5)

# print(f"La cantidad de nombres con 5 o mas caracteres son: {cantidad_nombres}")
        
        
# 8) Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista
# generada

def cargar_lista_enteros(mensaje:str, cantidad:int)->list:
    '''
    La funcion carga enteros en una lista
    Recibe un mensaje con lo que se pide y la cantidad de elementos de la lista
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    
    lista = []
    
    for _ in range(cantidad):
        entero_ingresado = int(input(mensaje))
        lista += [entero_ingresado]
        
    return lista

def mostrar_lista(lista:list)->None:
    for elem in lista:
        print(elem)
        
'''lista_enteros = cargar_lista_enteros("Ingrese un numero entero: ", 5)

mostrar_lista(lista_enteros)'''

#9) Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al
#ingresar el cero. Mostrar finalmente todos los elementos cargados y el tamaño de la lista.

def cargar_lista_enteros(mensaje:str, valor_break)->list:
    '''
    La funcion carga enteros en una lista
    Recibe un mensaje con lo que se pide y la cantidad de elementos de la lista
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    
    lista = []
    
    while True:
        numero = input(mensaje)
        if numero == valor_break:
            break

        lista += [int(numero)]

    return lista

def mostrar_lista(lista:list)->None:
    for elem in lista:
        print(elem)

'''lista_enteros = cargar_lista_enteros("Ingrese un numero entero: ", 0)

mostrar_lista(lista_enteros)

print(f"La cantidad de numeros de la lista es:{len(lista_enteros)}")'''

#10) Almacenar en una lista los sueldos (valores float) de 7 operarios. Imprimir la lista y el promedio de sueldos.

def cargar_lista(mensaje:str, cantidad:int, tipo:type)->list:
    '''
    La funcion carga datos en una lista con el tipo especificado
    Recibe un mensaje con lo que se pide, la cantidad de elementos de la lista y el tipo de dato
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    
    lista = []

    for _ in range(cantidad):
        valor_ingresado = input(mensaje)

        valor_ingresado = tipo(valor_ingresado)


        lista += [valor_ingresado]
        
    return lista

def mostrar_lista(lista:list)->None:
    '''
    La funcion recibe una lista y la muestra por pantalla
    '''
    for elem in lista:
        print(elem)

def calcular_promedio(lista:list)->float|None:
    '''
    La funcion recibe una lista y calcula el promedio, si está vacia devuelve None
    '''
    if len(lista) == 0:
        promedio = None
    else:
        acumulador = 0

        for element in lista:
            acumulador += element

        promedio = acumulador / len(lista)

    return promedio


'''lista_sueldos = cargar_lista("ingrese numeros: ", 7, float)
promedio_lista =calcular_promedio(lista_sueldos)

mostrar_lista(lista_sueldos)

print(f"El promedio de los sueldos es de: {promedio_lista}")'''

"""11) Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float). Obtener el promedio de las
mismas. Contar cuántas personas son más altas que el promedio.
"""


def cargar_lista(mensaje:str, cantidad:int, tipo:type)->list:
    '''
    La funcion carga datos en una lista con el tipo especificado
    Recibe un mensaje con lo que se pide, la cantidad de elementos de la lista y el tipo de dato
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    
    lista = []

    for _ in range(cantidad):
        valor_ingresado = input(mensaje)

        valor_ingresado = tipo(valor_ingresado)


        lista += [valor_ingresado]
        
    return lista


def calcular_promedio(lista:list)->float|None:
    '''
    La funcion recibe una lista y calcula el promedio, si está vacia devuelve None
    '''
    if len(lista) == 0:
        promedio = None
    else:
        acumulador = 0

        for element in lista:
            acumulador += element

        promedio = acumulador / len(lista)

    return promedio


def contar_superen_promedio (lista:list,promedio:float)->int:
    contador = 0 

    for elemento in lista:
        if elemento > promedio:
            contador +=1
    return contador

def identificar_valor_maximo(lista:list)->int|None:
    """Retorna None cuando se produjo un error o la lista está vacía, caso contrario retorna el valor máximo
      """
    numero_mayor = None 

    for i in range (len(lista)):

        if(numero_mayor == None or lista[i] > numero_mayor):
            numero_mayor = lista[i]

    
    return numero_mayor
 



# lista_sueldos = cargar_lista("ingrese numeros: ", 7, float)
# promedio_lista =calcular_promedio(lista_sueldos)

# mostrar_lista(lista_sueldos)

# print(f"El promedio de los sueldos es de: {promedio_lista}")

# """

"""12) Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.
"""
#lista_numeros_enteros = cargar_lista("Ingrese un número entero: ",5,int)

#valor_maximo = identificar_valor_maximo (lista_numeros_enteros)

#print(f"El número entero máximo es {valor_maximo}")

'''13) Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de
la lista y su posición.'''

def identificar_valor_minimo (lista:list)->int|None:
    """Retorna None cuando se produjo un error o la lista está vacía, caso contrario retorna el valor mínimo
      """
    numero_menor = None 

    for i in range (len(lista)):

        if(numero_menor == None or lista[i] < numero_menor):
            numero_menor = lista[i]

    
    return numero_menor

#lista_numeros_enteros = cargar_lista("Ingrese un número entero: ",5,int)

#valor_minimo = identificar_valor_minimo (lista_numeros_enteros)

#print(f"El número entero mínimo es {valor_minimo} y su indice es {lista_numeros_enteros.index(valor_minimo)}")

'''14) Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de la persona
con el nombre más corto.'''
       

def identificar_valor_minimo(lista: list) -> int | None:
    """
    Retorna None cuando se produjo un error o la lista está vacía, caso contrario retorna el valor minimo
    """
    numero_menor = None 

    for i in range (len(lista)):

        if(numero_menor == None or lista[i] < numero_menor):
            numero_menor = lista[i]

    
    return numero_menor

# def posicion_numero_minimo(lista:list, numero_menor:int)->int:
   
#     for i in range(len(lista)):
#         if lista[i] == numero_menor:
#             indice_menor = i
#             break
#     return indice_menor 

#[2,3,2,5] 
#       
def posicion_numero_minimo(lista:list, numero_menor:int)->list:
    lista_indice = []
    for i in range(len(lista)):
        if lista[i] == numero_menor:
            lista_indice += [i]
    return lista_indice





'''print("LISTA DE ENTEROS")

lista_enteros = cargar_lista(5,".Ingrese un entero: ", int)

numero_mas_chico = identificar_valor_minimo(lista_enteros)
indice_numero_minimo = posicion_numero_minimo(lista_enteros, numero_mas_chico)

print(f"El numero mas chico es: {numero_mas_chico} y su indice es {indice_numero_minimo}")'''

'''15) Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir
si dicho valor se encuentra en 2 o más posiciones en la lista)'''

def determinar_repetidos(lista:list, valor:int)->int:
    contador = 0
    for elemento in lista:
        if elemento == valor:
            contador += 1
    return contador

"""lista_cargada = cargar_lista("Ingrese un numero entero: ", 5, int)
valor_maximo = identificar_valor_maximo(lista_cargada)
cantidad_repetidos = determinar_repetidos(lista_cargada, valor_maximo)
print(f"El valor maximo es: {valor_maximo}")
if cantidad_repetidos >= 2:
    print(f"Se repetio el maximo {cantidad_repetidos} veces")"""

'''16) Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de
realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o
iguales a 18 años). Utilizar listas paralelas.'''

def cargar_listas_paralelas(cantidad:int, mensaje_a:str, mensaje_b:str, lista_a:list, lista_b:list)->list:
    
    """
    Carga una cantidad determinada de nombres y edades en dos listas paralelas.
    
    Args:
        cantidad (int): Cantidad de nombres y edades a cargar.
        mensaje_a (str): Mensaje a mostrar para pedir el nombre.
        mensaje_b (str): Mensaje a mostrar para pedir la edad.
        lista_a (list): Lista de nombres.
        lista_b (list): Lista de edades.
    
    Returns:
        list: Una lista con los nombres y otra con las edades, ambas de igual longitud.
    """
    for _ in range (cantidad):
        valor_a = input(mensaje_a)
        valor_b = input(mensaje_b)
        lista_a += [valor_a]
        lista_b += [valor_b]
    return lista_a, lista_b

def mostrar_mayores(lista_a, lista_b, valor_b)->None:

    for i in range(len(lista_b)):
        if int(lista_b[i]) >= valor_b:
            print(lista_a[i])



#lista_nombres = []
#lista_edades = []

#cargar_listas_paralelas(5, "Ingrese nombre: ", "Ingrese edad: ", lista_nombres, lista_edades)
#mostrar_mayores(lista_nombres, lista_edades, 18)

#print(f"El nombres de las personas mayores de edad son: {lista_nombres} y sus edades son: {lista_edades}")

'''17) Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Mostrar la
cantidad de productos que tienen un precio mayor al primer producto ingresado.'''

def contar_mayor_que_primero(lista:list)->int:
    contador = 0
    for i in range(len(lista)):
        if i == 0:
            primer_valor = lista[i]
        elif lista[i] > primer_valor:
            contador += 1
    return contador

'''lista_nombres = []

lista_precios = []'''

'''cargar_lista_paralelas(5,"Ingrese el nombre del producto: ", "Ingrese el valor del producto: ", lista_nombres, lista_precios)

mayores_a_primer_valor = contar_mayor_que_primero(lista_precios)

print(f"La cantidad de productos que superan el precio del primer producto es de: {mayores_a_primer_valor}")'''


'''Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. Generar una
tercer lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista'''

def sumar_listas (lista_a:list, lista_b: list) -> list:
    lista_c = []
    for i in range(len(lista_a)):
        lista_c += [int(lista_a[i]) + int(lista_b[i])]
    return lista_c



#lista_numeros_a = []
#listas_numeros_b = []

#cargar_listas_paralelas(4, "Ingrese numero:", "Ingrese otro numero:", lista_numeros_a, listas_numeros_b)
#resultado = sumar_listas (lista_numeros_a, listas_numeros_b)
#print("La lista resultante es:")
#mostrar_lista(resultado)

'''18) Realizar un programa que permita la registración de una cantidad determinada de alumnos y sus respectivas
notas de exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar la cantidad total de alumnos. (No se debe poder acceder a las opciones b,c y d si no se ingresó a la
opción “a”)
b) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas).
c) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar
"Promocionado" si la nota es mayor o igual a 6, "Aprobado" si la nota es 4 o 5, y colocar "Reprobado" si la
nota es inferior a 4.
d) Contar e imprimir por consola la cantidad de “Aprobados”, “Promocionados” y “Reprobados”.'''


