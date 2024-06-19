'''#Lista paralela (repaso)
nombres = ["Pedro", "Ana", "Jose"]
edades = [23, 30, 18]
estados = ["OCUPADO","OCUPADO","OCUPADO"]

def mostrarlista(lista_estado:list, lista_uno:list, lista_dos:list):
    for i in range(len(lista_estado)):
        if lista_estado[i] == 'OCUPADO':
            print(f"{lista_estado[i]} {lista_uno[i]}")

    mostrarlista(estados,nombres, edades)'''

#Lista paralela

nombres = ["Pedro", "Ana", "Jose"]
edades = [23, 30, 18]
estados = ["OCUPADO","OCUPADO","OCUPADO"]
personas = [["OCUPADO", 'Pedro', 23, "M"], ["OCUPADO", 'Ana', 30, "F"], ["OCUPADO", 'Jose', 18, "M"]]

def mostrarlista(lista_estado:list, lista_uno:list, lista_dos:list):
    for i in range(len(lista_estado)):
        if lista_estado[i] == 'OCUPADO':
            print(f"{lista_estado[i]} {lista_uno[i]}")

    #mostrarlista(estados,nombres, edades)

def listar_lista_de_lista(lista:list):
    #recorro la lista
    for i in range(len(lista)):
        #Seteo/Inicializacion de variables
        bandera_mensaje = True
        bandera_ocupado = True
        estado_ocupado = False
        
        #Recorro cada elemento (es una lista) de la lista 
        for j in range(len(lista[i])):
            #Controlo el primer elemento que es OCUPADO/LIBRE para no imprimirlo
            if bandera_ocupado == True: 
                bandera_ocupado = False
                #Controlo que el elemento este ocupado para mostrarlo a partir de la segunda repeticion de j
                if lista[i][j] == "OCUPADO":
                    estado_ocupado = True
            #Controlo que el estado este ocupado en cada elemento (es una lista) de la lista general
            elif estado_ocupado == True:
                #Si no es un dato no es str lo paso/casteo a str
                if type(lista[i][j]) == int:
                    lista[i][j] = str(lista[i][j])
                #Quito el espacio en blanco del primer mensaje
                if bandera_mensaje == True:
                    mensaje = lista[i][j]
                    bandera_mensaje = False
                #Concateno los datos con un espacio en blanco en medio de ellos
                else:
                    mensaje += " " + lista[i][j]
        #Imprimo solamente si esta ocupado
        if estado_ocupado == True:
            print (mensaje)

listar_lista_de_lista(personas)




#ejemplo1
"""for i in range(len(personas)):
    print(personas[i][0], personas[i][1])"""

#ejemplo2
"""for personas in personas:
    print(personas[0], personas[1])"""

#ejemplo3
# 0, 1, 2
"""for i in range(len(personas)):
    mensaje= ""
    bandera =True
    for j in range(len(personas[i])):
        if type(personas[i][j])== int:
            personas[i][j] = str(personas[i][j])
            if bandera:
                mensaje += "," + personas[i][j]
                bandera = False
            else:
                mensaje += "," + personas[i][j]    
    print(mensaje)"""