def listar(lista1:list, lista2:list, lista3:list): #se debe pasar 3 listas
    for i in range(len(lista1)):
        if lista1[i] != "LIBRE":
            mostrar(lista2, lista3, i)
            """print(lista[i])"""  

def mostrar(lista:list, lista1:list, indice:int): #2 listas + indice
    print(f"{lista[indice]}, {lista1[indice]}")  

def buscar(lista:list,dato:str)-> int:
    """
    Busca un dato en una lista.
    Si lo encuentra retorna el indice.
    Si no lo encuentra retorna -1
    """
    retorno = -1
    for i in range(len(lista)):
        if dato == lista[i]:
            retorno = i
            print("Dato encontrado")
            break

    if retorno == -1:
        print ("El nombre buscado no se encuentra en la lista")
    return retorno

def validar_respuesta(rta:str)-> bool:
    retorno = False
    if rta == "S" or rta == "s" or rta=="N" or rta == "n":
        retorno = True
    return retorno

def alta(mensaje:str):
    dato = input(mensaje)
    return dato

def buscar_libre(lista:list,libre:str)->int:
    retorno=-1
    for i in range(len(lista)):
        if lista[i] == libre:
            retorno=i
            break
    
    if retorno == -1:
        print ("No se encontraron espacios disponibles")
    return retorno

def lista_vacia(lista:list,libre:str,formato:str)->bool:
    retorno=True
    for i in range(len(lista)):
        if lista[i]!=libre:
            retorno=False
            break
    if retorno:
        print(f"No hay datos para {formato}")

    return retorno

def confirmar_si_o_no (formato:str) ->bool:
    '''Esta funcion le pregunta al usuario si desea confirmar una operacion, validando su respuesta. 
    Recibe por parametro un string para darle formato a la pregunta. EJ: Desea "borrar"?
    Devuelve False si la respuesta es negativa y True si la respuesta es verdadera'''
    retorno = False
    confirmar = input(f"Desea {formato}? [S | N]?: ")
    while validar_respuesta(confirmar)== False:
        confirmar = input(f"Desea {formato}? [S | N]?: ")
    if confirmar == "S" or confirmar =="s":    
        retorno = True
    
    return retorno

def ingresar_opcion(rango1=1,rango2=1)->int:
    '''Esta funcion le pide al usuario que ingrese una opcion, la valida y retorna la opcion elegida dentro del rango valido.
    Recibe por parametro el rango de opciones, el primero como inicio, el segundo como final. Ambos tienen valor 1 por defecto.
    Retorna un entero con la opcion elegida.
    '''
    opcion = input("Ingrese una opción: ")
    while opcion.isdigit() == False or int(opcion) < rango1 or int(opcion) > rango2:
        opcion = input(f"Ingrese una opción valida ({rango1}-{rango2}): ")
    opcion = int(opcion)
    
    return opcion

def imprimir_estado_dato(formato:str, bandera:bool):
    '''
    Esta funcion imprime si un dato fue eliminado/modificado
    Recibe el formato y la bandera por parametros
    No retorna ningun valor'''
    if bandera:
        print(f"El dato se ha {formato}")  
    else:
        print(f"El dato no se ha {formato}")  

def ingresar_dato_buscar(lista:list,formato:str)->int:
    '''Esta funcion pregunta el dato a buscar y devuelve el indice
    Recibe una lista y formato de la pregunta por parametros
    Devuelve un entero'''
    dato_buscar = input (f"Ingrese el {formato} a buscar: ")
    indice = buscar(lista,dato_buscar)

    return indice

