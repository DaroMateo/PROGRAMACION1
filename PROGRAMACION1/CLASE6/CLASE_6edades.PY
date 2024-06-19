edades = []
acumulador = 0
bandera = False

for i in range(5):
    edad = int(input('Ingrese una edad: '))
    edades.append(edad)
    acumulador += edad

promedio_edad = acumulador / len(edades)

edad_minima = edades[0]

'''for i in range(len(edades)):
    # if bandera == False or edades[i] > edad_maxima:
    if i == 0 or edades[i] > edad_maxima:
        edad_maxima = edades[i]
        # bandera = True
    if edades[i] < edad_minima:
        edad_minima = edades[i]'''

for edad in edades:
    if bandera == False or edad > edad_maxima:
        edad_maxima = edad
        bandera = True
    if edad < edad_minima:
        edad_minima = edad
        
for i in range(len(edades)):
    print(edades[i])

print(edades)
print(promedio_edad)
print(edad_maxima)
print(edad_minima)