from os import system
#CADA ELEMENTO DE UN ARRAY QUEDA AL FINAL DE LA LISTA, PERO SI LA LISTA ESTA VACIA ENTRA COMO PRIMER ELEMENTO ASI SUCESIBAMENTE, ASI SE INGRESA DATOS DE MANERA SECUENCIAL
palabra = input('INGRESE UN PALABRA: ')
#RECORRER LETRA POR LETRA
for i in range(len(palabra)):
    print(palabra[i])

for letra in palabra:
    print(letra)

# CARGA SECUENCIAL

nombres = ['A' , 'A', 'A', 'A', 'A']

for i in range(len(nombres)):
    nombre = input('INGRESE UN NOMBRE: ')
    nombres[i] = nombre

nombres[2] =  'Burns'

for i in range(len(nombres)):    
    print(nombres[i])

#CARGA ALEATORIA

nombres = ['A' , 'A', 'A', 'A', 'A']

for i in range(len(nombres)):
    nombre = input('INGRESE UN NOMBRE: ')
    indice = int(input('INGRESE EL INDICE: '))
    while indice < 0 or indice > len(nombres) or nombres[indice] != "A":
        indice = int(input('ERROR INDICE OCUPADO, INGRESE EL INDICE: '))
    
    nombres[indice] = nombre
   
#nombres[2] =  'Burns'

for i in range(len(nombres)):    
    print(nombres[i])

# CARGA MIXTA

def listar(lista:list):
    if contador > 0:
        for i in range(len(lista)):
            if lista[i] != 'A':
                print(lista[i])


nombres = ['A' , 'A', 'A', 'A', 'A']
continuar = True
contador = 0
encontrado = False

while continuar == True:
    print('Menu ')
    print('1- alta ')
    print('2- listar')
    print('3- modificar')
    print('4- baja')
    print('5- salir')
    opcion = int(input('INGRESE LA OPCION: '))
    system('cls') #antes de entrar el menu limpia la pantalla

    match opcion:
        case 1:
            if contador < len(nombres):
                for i in range(len(nombres)):
                    if nombre[i] == 'A':
                            nombre = input('INGRESE UN NOMBRE: ')
                            nombre[i] = nombre
                            contador += 1
                            break
            else:
                print('NO SE ENCONTRO ESPACIOS DISPONIBLES')

        case 2:
            if contador > 0:
                listar(nombres)
                '''for i in range(len(nombres)):
                    if nombre[i] != 'A':
                        print(nombres[i])'''
            else:
                print('NO HAY DATOS PARA LISTAR')

        case 3:
           if contador > 0:
                encontrado = False
                nombre_buscar = input('INGRESE NOMBRE A BUSCAR: ')
                for i in range(len(nombre)):
                    if nombre_buscar == nombre[i]:
                        nombres[i] == 'A'
                        contador -= 1
                        encontrado = True
                        break
                    
                if encontrado == False:
                    print('EL DATO BUSCADO NO SE ENCUENTRA EN LA LISTA')
           else:
                print('NO HAY DATOS PARA ELIMINAR')
        
        case 4:
            if contador > 0:
                encontrado = False
                nombre_buscar = input('INGRESE NOMBRE A BUSCAR: ')
                for i in range(len(nombre)):
                    if nombre_buscar == nombre[i]:
                        nombres[i] == input('INGRESE UN NUEVO NOMBRE')
                        encontrado = True
                        break
                    
                if encontrado == False:
                    print('EL DATO BUSCADO NO SE ENCUENTRA EN LA LISTA')
            else:
                print('NO HAY DATOS PARA ELIMINAR')
        case 5:
            continuar = False

        case _:
            print('LA OPCION INGRESADA ES INCORRECTA')

#informar cuando no hay espacio, cuand el for termina su ciclo