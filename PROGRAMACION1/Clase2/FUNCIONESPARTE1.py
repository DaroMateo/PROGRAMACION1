"""Funciones Parte I

1. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

2. Crear una función que verifique si un número dado por argumento es par o impar. 
   La función debe imprimir un mensaje indicando si el número es par o impar.
   
3. Define una función que encuentre el máximo de tres números. 
   La función debe aceptar tres argumentos y devolver el número más grande.
   
4. Diseña una función que calcule la potencia de un número. 
   La función debe recibir la base y el exponente como argumentos y devolver el resultado.

5. Realizar el mismo ejercicio del item 2, pero sin utilizar el operador % """

"""1"""

def ingresar_numero():
    while True:
        numero = int(input("Por favor, ingrese un número entero: "))

        return numero
    
numero_ingresado = ingresar_numero()
print("El número ingresado es:", numero_ingresado)

'''Valida que el numero sea entero. 
No recibe argumento. 
Retorna un entero.

def validar_entero():
    numero = input("Por favor, ingrese un número entero: ")
    
    while not numero.isdigit():
        numero + input("REINGRESE UN NUMERO ENTERO: ")

    numero = int(numero)

    return numero
'''
'''Valida un valor determinado si es un numero entero o no
retorna true si es un numero entero o false si  no lo es 
retorna una cadena de caracteres
is.digit es un metodo para verificar si es digito'''
'''def validar_entero(cadena:str)->bool:
    prueba = '12'
    for carcater in prueba:
        if carcater >= '0' and carcater <= '9':
            print('anda') '''
'''retorno = True

    for carcater in prueba:
        if carcater < '0' or carcater > '9':
            retorno = False
            break

        return retorno
    
    control = validar_entero("123")
    print (control)
''' 
    
'''retorno = False

    if cadena.isdigit():
        retorno = True

    return retorno

dato = input("ingrese un dato")
control = validar_entero(dato)

while control == False:
    dato = input("ingrese un dato")
    control = validar_entero(dato)

dato = int(dato)'''
    
"""2"""

def verificar_par_impar(numero):
    if(numero % 2 == 0):
        print("EL numero {0} es par".format(numero))
    else:
         print("EL numero {0} es impar".format(numero))

verificar_par_impar(numero=numero_ingresado) 
"""prueba"""

"""3"""
'''def encontrar_maximo(ingresar_numero):
    return max(ingresar_numero)

numero_maximo = encontrar_maximo(ingresar_entero = numero_ingresado)
print("El número máximo es:", numero_maximo)'''

"""4"""

def calcular_potencia(base, exponente):
    return base ** exponente

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = calcular_potencia(base, exponente)
print("El resultado de elevar", base, "a la potencia", exponente, "es:", resultado)

"""5"""

def verificar_par_impar(numero):
    if numero / 2 == int(numero / 2):
        print(numero, "es un número par.")
    else:
        print(numero, "es un número impar.")
numero = int(input("Ingrese un número: "))
verificar_par_impar(numero)