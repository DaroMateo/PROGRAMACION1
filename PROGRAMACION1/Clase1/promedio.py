contador = 0
acumulador = 0
for i in range(3):
    numero = int(input("ingrese un numero"))
    acumulador += numero
    #acumulador = acumulador + numero
    contador += 1
    # contador = contador + 1
promedio = acumulador/ contador
print(promedio)