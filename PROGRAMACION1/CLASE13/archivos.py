# r abre un archivo para lectura
# rb abre un archivo para lectura binaria
#r+ abre un archivo para lectura y escritura
#w abre un archivo para escritura
#a abre un archivo para escritura
#wb abre un archivo para escritura binaria
#w+ abre un archivo para lectura y escritura

# archivo objeto
#nombre_archivo string que contiene el nombre del archivo
#modo string que contiene el modo de apertura

nombre_archivo = input("Archivo: ")
modo = input("Modo: ")
archivo = open(nombre_archivo, modo)

# file permite no sólo operar con él sino también obtener mucha información relacionada con ese archivo
# archivo.closed verdadero o falso
#archivo.mode string que contiene el modo de apertura
#archivo.name string que contiene el nombre del archivo

#archivo.read string que contiene el contenido del archivo
# Abrimos el archivo en modo lectura y escritura
archivo = open('archivo.txt', 'r+')
texto = archivo.read(10)
print('El contenido del archivo es: ' + texto)
# Cerramos el archivo
archivo.close()

#archivo.readlines lista de string que contiene el contenido del archivo
archivo = open('archivo.txt', 'r+')
print(archivo.tell()) #Indica en que byte esta el puntero 0
linea = archivo.readline()
print(linea,end="") # Hola mundo
print(archivo.tell()) #Indica en que byte esta el puntero 11
# Cerramos el archivo
archivo.close()

#archivo.write string que contiene el contenido del archivo
archivo = open('archivo.txt', 'w')
archivo.write('Primer linea de texto\n')
archivo.write('segunda linea\n')
archivo.write('tercera linea\n')
archivo.close()

#archivo.writelines lista de string que contiene el contenido del archivo
archivo = open('archivo.txt', 'w')
lineas_texto = ['Primer linea de texto\n','segunda linea\n','tercera linea\n']
archivo.writelines(lineas_texto)
archivo.close()

#archivo.seek(byte) mueve el puntero al byte indicado
archivo = open('archivo.txt', 'r+')
archivo.seek(11)
print(archivo.tell()) #Esta en el byte 11
linea = archivo.readline()
print(linea,end="") # Hola mundo
archivo.close()

#with abre un archivo para lectura y escritura
with open('archivo.txt', 'r+') as archivo:
    for linea in archivo:
        print(linea, end="")



nombre_archivo = input("Archivo: ")
archivo_datos = open(nombre_archivo, 'r')
#lista_lineas = archivo_datos.readlines()

for linea in archivo_datos:
    print(linea, end="")

print("\n")
#archivo.close() para cerrar el archivo
archivo_datos.close()