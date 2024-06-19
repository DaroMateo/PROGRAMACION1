# str: es un tipo inmutable, que no puede cambiar, permite almacenar secuencia de carcateres
taberna = "Moe's"
print(taberna)

# secuencia de escape
taberna = 'Moe\'s'
print(taberna)

# lo baja a una linea nueva
saludo = 'Hola\nChau'
print(saludo)

#tabula\ encolumna
saludo = 'Hola\tChau'
print(saludo)

#La """ """ sirve para que pueda imprimir como esta escrito y no todo seguido

#%d tenes q decirle q es un numero decimal se concatena ej %(numero,pi)
numero =3
pi =3.14

mensaje = "el numero es %d\nEl valor de pi es %f %s" %(numero, pi,saludo)

#saber si puedo buscar una cadena dentro de una cadena

print("cierto" in "rascacielo")

# not in ( no esta en) suele aparecer en muchos tipos de codigos

# print(texto.count('corto')) metodo de conteo 
# print(len(texto)) cuenta la cantidad de caracteres que hay en un texto o lo que este en el str

# slay imprime el rango de 0 a 2 que seria ab
x = 'abcd'

print(x[0:2]) #ab

print(x[2:]) #cde imprime del rango 2 hasta donde termine

#subcadenas

print(x[0:5:2]) #ace
print(x[0::2]) #ace

#eliminar una cadena

texto = "este es un ejemplo"
print("cadena: " + texto)
del texto 