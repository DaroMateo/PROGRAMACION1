import random
from os import system
'''1) Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.'''

def sumar_elementos_lista(lista: list)->int:
    """
    Calcula la suma de todos los elementos de una lista determinada.
    Parameters:
    lista (lista): La lista de números a sumar.
    Returns:
    int: la suma de todos los elementos de la lista.
    """
    acumulador = 0
    for i in range(len(lista)):
        acumulador += lista[i]
    return acumulador

'''2)Definir una lista que almacene los nombres de los primeros seis meses del año. Mostrar el primer y último
elemento de la lista solamente.'''

def imprimir_primer_ultimo_y_ultimo_elemento(meses:list)->str:
    """
    Imprime el primer elemento de una lista y el último elemento de la lista.
    Parameters:
    meses (lista): La lista de meses.
    """
    print(meses[0], meses[-1])

#print(imprimir_primer_ultimo_y_ultimo_elemento(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']))

'''3)Definir una lista que almacene como primer elemento el nombre de un alumno y en las dos siguientes sus
notas. Imprimir luego el nombre y el promedio de las dos notas.'''
lista = ["dario", 10,6]
def calcular_y_mostrar_promedio (lista:list)->float:
    """
    Calcula y muestra el promedio de una lista de dos elementos.
    Parameters:
    lista (lista): una lista de dos elementos.
    """
    print(f"El nombre es: {lista[0]} y el promedio es: ", {(lista[1] + lista[2]) / 2})

#print(calcular_promedio([1,2,3,4,5]))

'''4)Definir una lista con 7 elementos enteros. Contar cuántos de dichos valores almacenan un valor superior a 33.'''
def contar_superior_a_33(lista:list)->int:
    """
    Conta cuantos de los elementos de una lista son superiores a 33.
    Parameters:
    lista (lista): una lista de números.
    Returns:
    int: la cantidad de elementos de la lista que son superiores a 33.
    """
    contador = 0
    for i in range(len(lista)):
        if lista[i] > 33:
            contador += 1
    return contador

#print(contar_superior_a_33([1,2,3,55,5,6,7]))

''' 5)Definir una lista con 7 elementos enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores
a 5'''

def crear_lista_de_7_elementos(lista:list)->list:
    """
    Crea una lista con 7 elementos enteros.
    Parameters:
    lista (lista): una lista vacía.
    """
    for i in range(7):
        num = int(input('INGRESE UN NUMERO: '))
        lista.append(num)
    return lista

def mostrar_superiores_a_5 (lista:list)->list:
    """
    Imprime los elementos de una lista que son superiores a 5.
    Parameters:
    lista (lista): una lista de números.
    """
    for i in range(len(lista)):
        if lista[i] >= 5:
            mensaje = lista[i]
        return mensaje

#print(mostrar_superiores_a_5([1,2,3,55,5,6,7]))

'''6)Definir y cargar una lista con 10 números enteros aleatorios (utilizar random), entre 1 y 10. Contar y mostrar por
pantalla la cantidad de números pares.'''

def crear_lista_numeros_random(tope, valor_desde: int, valor_hasta: int):
    """
    Genera una lista de números aleatorios dentro del rango [0, 99] de la longitud especificada.

    Parameters:
        tope (int): La longitud de la lista que se generará.
    Returns:
        list: Una lista de números aleatorios dentro del rango [0, 99] de la longitud especificada.
    """
    numeros = []
    for i in range (tope):
        numeros+= [random.randint(valor_desde, valor_hasta)]

    return numeros
def contar_pares (lista:list)->int:
    """
    Conta cuantos de los elementos de una lista son pares.
    Parameters:
    lista (lista): una lista de números.
    Returns:
    int: la cantidad de elementos de la lista que son pares.
    """
    contador = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            contador += 1
    return contador

#print(contar_pares([1,2,3,4,5,6,7,8,9,10]))

'''7)Definir una lista que almacene los nombres de 4 personas. Contar cuántos de esos nombres tienen 5 o más
caracteres'''

def ingresar_nombres(mensaje:str, limite:int)->list:
    nombres = []
    for i in range(limite):
        nombre_insgresado = input(mensaje)
        nombres += [nombre_insgresado]
    return nombres

def contar_caracteres (lista:list)->int:
    """
    Conta cuantos de los elementos de una lista tienen 5 o más caracteres.
    Parameters:
    lista (lista): una lista de nombres.
    Returns:
    int: la cantidad de elementos de la lista que tienen 5 o más caracteres.
    """
    contador = 0
    for i in range(len(lista)):
        if len(lista[i]) >= 5:
            contador += 1
    return contador

#print(contar_caracteres((f"{ingresar_nombres('INGRESE UN NOMBRE: ', 4)}")))

'''8)Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista
generada'''

def cargar_enteros():
    lista_enteros = []
    
    for i in range(5):
        numero = int(input(f'Ingresa el entero {i+1}: '))
        lista_enteros += [numero]
        mensaje = f'La lista generada es: {lista_enteros}'
    return mensaje

#print(cargar_enteros())


"""9)Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al
ingresar el cero. Mostrar finalmente todos los elementos cargados y el tamaño de la lista"""

def cargar_lista_enteros(mensaje:str, valor_break)->list:
    
    """
    Carga una lista con valores enteros ingresados por teclado.
    Finaliza la carga de enteros al ingresar el valor_break.
    Retorna la lista conformada con los datos ingresados por el usuario.
    
    Parameters:
    mensaje (str): el mensaje a mostrar al usuario para solicitar el ingreso de enteros.
    valor_break (int): el valor que hace que finalice la carga de enteros.
    
    Returns:
    list: la lista con los enteros ingresados (sin incluir el valor_break).
    """
    lista = []

    while True:
        num = int(input(mensaje))
        if num == valor_break:
            break
        
        lista += [int(num)]
    
    return lista

def mostrar_enteros (lista:list)->list:
    """
    Imprime los elementos de una lista.
    Parameters:
    lista (list): una lista de enteros.
    """
    for i in range(len(lista)):
        print(lista[i])
    return lista

#mostrar_enteros(cargar_lista_enteros("Ingrese un numero: ", 0))

'''10) Almacenar en una lista los sueldos (valores float) de 7 operarios. Imprimir la lista y el promedio de sueldos.'''
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


'''11) Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float). Obtener el promedio de las
mismas. Contar cuántas personas son más altas que el promedio.'''

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
'''12) Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.'''
def buscar_num_max(lista):
    """
    Encuentra el número maximo en una lista determinada.
    Parameters:
    - lista (list): La lista de números para buscar.
    Returns:
    - int: el número maximo en la lista.
    """
    numero_max = lista[0]
    for elemento in range(len(lista)):
        if lista[elemento] > numero_max:
            numero_max = lista[elemento]
    return numero_max

#print (f"El mayor valor de la lista es: {buscar_num_max(cargar_lista("ingrese un numero: ", 5, int))}")
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
def mostrar_nombres (lista:list)->None:
    """Retorna None cuando se produjo un error o la lista está vacía, caso contrario retorna el valor mínimo
      """
    indice_minimo = 0
    for i in range (len(lista)):
        if len (lista[indice_minimo]) > len (lista[i]):
            indice_minimo = i

    print (f"El nombre mas corto es {lista[indice_minimo]}")

#lista_nombres = cargar_lista("Ingrese un nombre: ",5,str)  

#mostrar_nombres (lista_nombres)

#print(mostrar_nombres (lista_nombres))
'''15) Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir
si dicho valor se encuentra en 2 o más posiciones en la lista)'''

def contar_repeticiones (lista:list,valor:int)->int:
    """Retorna None cuando se produjo un error o la lista está vacía, caso contrario retorna el valor mínimo
      """
    contador = 0
    for i in range (len (lista)):
        if lista[i] == valor:
            contador += 1
    return contador

#lista_numeros_enteros = cargar_lista("Ingrese un número entero: ",5,int)

#valor_maximo = identificar_valor_maximo (lista_numeros_enteros)

#print(f"El valor maximo es {valor_maximo} y se repite {contar_repeticiones (lista_numeros_enteros,valor_maximo)} veces")

'''16) Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de
realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o
iguales a 18 años). Utilizar listas paralelas.'''

def validar_nombres_edades (lista_nombres:list,lista_edades:list)->list:
    """Retorna una lista con los nombres de las personas que son mayores de edad o iguales a 18 años.
    
    Args:
        lista_nombres (list): Lista de nombres de personas
        lista_edades (list): Lista de edades de las personas
    
    Returns:
        list: Lista con los nombres de las personas que son mayores de edad o iguales a 18 años
    """
    nombres_mayores = []
    for i in range (len (lista_nombres)):
        if lista_edades[i] >= 18:
            nombres_mayores += [lista_nombres[i]]
    return nombres_mayores

#lista_nombres_cargados = cargar_lista("Ingrese un nombre: ",5,str)
#lista_edades_cargadas = cargar_lista("Ingrese una edad: ",5,int)
#print(f"Nombres mayores de edad: {validar_nombres_edades (lista_nombres_cargados,lista_edades_cargadas)}")

'''17) Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Mostrar la
cantidad de productos que tienen un precio mayor al primer producto ingresado.'''

def validar_precios (lista_productos:list,lista_precios:list,valor:int)->list:

    """
    Retorna una lista con los nombres de los productos que tienen un precio mayor al valor ingresado
    
    Args:
        lista_productos (list): Lista de nombres de productos
        lista_precios (list): Lista de precios de los productos
        valor (int): Valor a comparar
    
    Returns:
        list: Lista con los nombres de los productos que tienen un precio mayor al valor ingresado
    """
    productos_mayores = []
    for i in range (len (lista_productos)):
        if lista_precios[i] > valor:
            productos_mayores += [lista_productos[i]]
    return productos_mayores

#lista_productos_cargados = cargar_lista("Ingrese producto: ",5,str)
#lista_precios_cargadas = cargar_lista("Ingrese precio: ",5,int)
#print(f"Los productos con un precio mayor a {lista_precios_cargadas[0]} son: {validar_precios (lista_productos_cargados,lista_precios_cargadas,lista_precios_cargadas[0])}")

'''19) Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. Generar una
tercer lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista.'''
def sumar_listas (lista1:list,lista2:list)->list:
    """Retorna una lista con la suma de los elementos de las listas pasadas por parâmetro
    
    Args:
        lista1 (list): Lista de enteros
        lista2 (list): Lista de enteros
    Returns:
        list: Lista con la suma de los elementos de las listas pasadas por parâmetro
    """
    lista3 = []
    for i in range (len (lista1)):
        lista3 += [lista1[i] + lista2[i]]
    return lista3

#lista1 = cargar_lista("Ingrese un número: ",4,int)
#lista2 = cargar_lista("Ingrese un número: ",4,int)
#print(f"La lista resultante es: {sumar_listas (lista1,lista2)}")

'''18) Realizar un programa que permita la registración de una cantidad determinada de alumnos y sus respectivas
notas de exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar la cantidad total de alumnos. (No se debe poder acceder a las opciones b,c y d si no se ingresó a la
opción “a”)
b) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas).
c) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar
"Promocionado" si la nota es mayor o igual a 6, "Aprobado" si la nota es 4 o 5, y colocar "Reprobado" si la
nota es inferior a 4.
d) Contar e imprimir por consola la cantidad de “Aprobados”, “Promocionados” y “Reprobados”.'''

def registrar_alumnos():
    alumnos = []
    notas = []
    return alumnos, notas

def ingresar_alumnos(cantidad: int, alumnos: list, notas: list):
    """
    Ingresar nombre y nota de cada alumno y almacenar los datos en dos listas paralelas.
    
    Args:
        cantidad (int): Cantidad de alumnos a registrar
        alumnos (list): Lista de nombres de los alumnos
        notas (list): Lista de notas de los alumnos
    
    Returns:
        list: Lista de nombres de los alumno
        list: Lista de notas de los alumno
    """
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        while True:
            nota = float(input(f"Ingrese la nota de {nombre} (0 a 10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        alumnos += [nombre]
        notas += [nota]
    return alumnos,notas

def listar_alumnos(alumnos: list, notas: list):
    """
    Realizar un listado que muestre los nombres, notas y condición del alumno.
    
    Args:
        alumnos (list): Lista de nombres de los alumnos
        notas (list): Lista de notas de los alumnos
    
    Returns:
        list: Lista de nombres de los alumno
    """
    print("\nListado de alumnos:")
    for i in range(len(alumnos)):
        nombre = alumnos[i]
        nota = notas[i]
        if nota >= 6:
            condicion = "Promocionado"
        elif 4 <= nota <= 5:
            condicion = "Aprobado"
        else:
            condicion = "Reprobado"
        print(f"Nombre: {nombre}, Nota: {nota}, Condición: {condicion}")
    return alumnos


def contar_condiciones(notas: list):
    """
    Contar la cantidad de aprobados, promocionados y reprobados en una lista de notas.
    
    Args:
        notas (list): Lista de notas de los alumnos
    
    Returns:
        None
    """
    aprobados = 0
    promocionados = 0
    reprobados = 0
    for nota in notas:
        if nota >= 6:
            promocionados += 1
        elif 4 <= nota <= 5:
            aprobados += 1
        else:
            reprobados += 1
    print(f"\nCantidad de Promocionados: {promocionados}")
    print(f"Cantidad de Aprobados: {aprobados}")
    print(f"Cantidad de Reprobados: {reprobados}")
    

def menu_carga_alumnos():
    """
    Menú para interactuar con la carga de una lista de alumnos y sus respectivas notas.
    
    El menú permite:
        a) Ingresar la cantidad total de alumnos.
        b) Ingresar nombre y nota de cada alumno.
        c) Mostrar listado de alumnos con su condición.
        d) Mostrar cantidad de Aprobados, Promocionados y Reprobados.
        e) Salir.
    
    Se debe ingresar la cantidad total de alumnos antes de poder acceder a las demás opciones.
    """
    
    cantidad_alumnos = 0
    alumnos_registrados = False
    alumnos = []
    notas = []

    while True:
        print("\n--- Menú ---")
        print("a) Ingresar cantidad total de alumnos.")
        print("b) Ingresar nombre y nota de cada alumno.")
        print("c) Mostrar listado de alumnos con su condición.")
        print("d) Mostrar cantidad de Aprobados, Promocionados y Reprobados.")
        print("e) Salir.")
        
        opcion = input("Seleccione una opción: ")
        

        if opcion == 'a':
            
            while True:
                cantidad_alumnos = int(input("Ingrese la cantidad total de alumnos: "))
                if cantidad_alumnos > 0:
                    alumnos_registrados = True
                    alumnos, notas = registrar_alumnos()
                    print(f"Cantidad de alumnos a registrar: {cantidad_alumnos}")
                    break
                else:
                    print("Debe ingresar una cantidad positiva.")

        elif opcion == 'b':
            if alumnos_registrados:
                ingresar_alumnos(cantidad_alumnos, alumnos, notas)
            else:
                print("Primero debe ingresar la cantidad total de alumnos (opción 'a').")

        elif opcion == 'c':
            if alumnos_registrados and alumnos:
                listar_alumnos(alumnos, notas)
            else:
                print("Primero debe registrar los alumnos y sus notas (opción 'b').")

        elif opcion == 'd':
            if alumnos_registrados and alumnos:
                contar_condiciones(notas)
            else:
                print("Primero debe registrar los alumnos y sus notas (opción 'b').")

        elif opcion == 'e':
            #print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


#menu_carga_alumnos()