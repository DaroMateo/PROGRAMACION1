import random

#MINI JUEGO DE ADIVINAR EL NUMERO
numero_secreto = random.randint(1, 100)
contador_intentos = 0

while True:
    intento = int(input("Introduce un numero secreto entre 1 y 100: "))
    contador_intentos += 1
    if intento == numero_secreto:
        print(f"Enhorabuena, has acertado el numero en {contador_intentos} intentos")
        break
    elif intento > numero_secreto:
        print("El numero es menor")
    else:
        print("El numero es mayor")