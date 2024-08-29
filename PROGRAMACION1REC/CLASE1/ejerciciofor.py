#1 - Mostrar los números ascendentes desde el 1 al 10:

'''for i in range(1, 11):
    print(i)'''

#2 - Mostrar los números descendentes desde el 10 al 1:

'''for i in range(10, 0, -1):
    print(i)'''

#3 - Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

'''numero = int(input("ingrese un numero: "))

for i in range(0, numero + 1):
    print(i)'''

# 4- Ingresar un número y mostrar la tabla de multiplicar de ese número:

'''numero = int(input("ingrese un numero: "))

for i in range(11):
    print(f"{numero} x {i} = {numero * i}")
'''
#5- Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

'''suma = 0
contador = 0
for _ in range(10):
    numero = int(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    contador += 1
    
if contador > 0:
    promedio = suma / contador
    print(f"Suma: {suma}, Promedio: {promedio}")
else:
    print("No se ingresaron números.")'''

#6- Imprimir los números múltiplos de 3 entre el 1 y el 10:

'''for num in range(1, 11):
    if num % 3 == 0:
        print(num)'''

"""for i in range(3,10,3):
    print(i)"""

#7- Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
'''for i in range(1,51):
    if i % 2 == 0:
        print(i)'''

# 8- Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:
"""num = int(input("Ingresa un número: "))
mi_texto = ""
for i in range(1, num + 1):
    mi_texto += str(i)
    print(mi_texto)"""

#9-Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.
'''numero = int(input("Ingresa un número: "))
divisores = []
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)
print(f"Divisores de {numero}: {divisores}") 
print(f"Cantidad de divisores: {len(divisores)}")
'''

#10-Ingresar un número. Determinar si el número es primo o no.

'''numero = int(input("Ingresa un número: "))
es_primo = True
if numero <= 1:
    es_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")'''

#11- Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

n = int(input("Ingresa un número: "))
cantidad_primos = 0

for i in range(2, n + 1):
    es_primo = True
    
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            es_primo = False
            break
    
    if es_primo:
        print(i, end=" ")
        cantidad_primos += 1

print(f"\nCantidad de números primos entre 1 y {n}: {cantidad_primos}")

"""
#Echo en clase guia visual

#Ingreso el numero para el rango de 1 a el numero ingresado por usuario
num_user = int(input("Ingrese un numero: "))

#Inicializo contador de numeros primos
contador_primo = 0
contador_divisores = 0

#Recorro todos los numeros desde el 2 hasta el numero ingresado inclusive
for i in range(2, num_user + 1):

    #controlo que cada numero del rango ingresado por el usuario sea par
    if i % 2 == 0:
        #Controlo que el numero par sea igual a 2
        if i == 2:
            print(i)
            contador_primo += 1
    else:    #controlo que cada numero del rango ingresado por el usuario sea impar
        #Inicializo contador de divisores
        #contador_divisores = 0
        #Recorrer todos los numeros desde 3(tres) hasta el numero que estoy analizando menos 1(uno)
        for j in range(3, i):
            if i % j == 0:
                contador_divisores += 1
                break
        if contador_divisores == 0:
            contador_primo += 1
            print(i)

print(f"La cantidad de numeros primos es: {contador_primo}.")
"""

"""
numeros = "12345"
letras = "abcde"

for i in numeros:
    for j in letras:
        print(i, j)
"""