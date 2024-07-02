from os import system
import json


def leer_json(data, key):
    
    with open(data, "r") as archivo:
        data = json.load(archivo)
    
    return(data[key])

leer_json("data.json", "pasajeros")
def obtener_maximo(lista:list, clave:str):
    retorno = False
    flag = True
    
    if len(lista) > 0:
        for personaje in lista:
            if type(personaje[clave]) != type(int()) and type(personaje[clave]) != type(float()):
                break
            
            if flag == True or personaje[clave] > retorno:
                retorno = personaje[clave]
                flag = False

    return retorno


def validar_aerolinea():
    aerolinea = input("LATAM | AA | IBERIA\nIngrese aerolinea: ")
    aerolinea = aerolinea.upper()
    
    while aerolinea != "LATAM" and aerolinea != "AA" and aerolinea != "IBERIA" and aerolinea.isdigit() == True:
        aerolinea = input("LATAM | AA | IBERIA\nReingrese aerolinea: ")
    
    return aerolinea


def validar_nombre():
    apellido_pasajero = input("Ingrese apellido del pasajero: ").capitalize()
    nombre_pasajero = input("Ingrese nombre del pasajero: ").capitalize()
    nombre_completo = apellido_pasajero + " " + nombre_pasajero
    
    while len(nombre_completo) > 30 or nombre_completo.isdigit() == True:
         nombre_pasajero = input("No puede superar los 30 caracteres\nReingrese Apellido y Nombre del pasajero: ")
    
    return nombre_completo


def validar_dni():
    dni = input("Ingrese DNI: ")
    
    while len(dni) < 7 or len(dni) > 8:
        dni = input("Ingrese DNI: ")

    return dni


def validar_precio():
    precio = float(input("Ingrese precio del pasaje: "))
    
    while precio < 500000 or precio > 2000000:
        precio = float(input("El rango de precio es entre 500.000 y 2.000.000\nReingrese precio del pasaje: "))
    
    precio = str(precio)
    
    return precio


def validar_origen():
    origen = input("Buenos Aires | Madrid | París | Miami | Roma | Tokio\nIngrese ciudad de origen: ")
    origen = origen.lower()
    origen = origen.capitalize()
    
    while origen != "Buenos aires" and origen != "Madrid" and origen != "Paris" and origen != "Miami" and origen != "Tokio":
        origen = input("Buenos Aires | Madrid | París | Miami | Roma | Tokio\nReingrese una ciudad de origen valida: ")
    
    if origen == "Buenos aires":
        origen = "Buenos Aires"
    
    if origen == "Paris":
        origen = "París"
    
    return origen


def validar_destino():
    destino = input("Buenos Aires | Madrid | París | Miami | Roma | Tokio\nIngrese ciudad de destino: ")
    destino = destino.lower()
    destino = destino.capitalize()
    
    while destino != "Buenos aires" and destino != "Madrid" and destino != "Paris" and destino != "Miami" and destino != "Tokio":
        destino = input("Buenos Aires | Madrid | París | Miami | Roma | Tokio\nReingrese una ciudad de origen valida: ")
    
    if destino == "Buenos aires":
        destino = "Buenos Aires"
    
    if destino == "Paris":
        destino = "París"
    
    return destino


def validar_clase():
    clase = input("Turista | Ejecutivo\nIngrese clase de vuelo: ")
    clase = clase.lower()
    clase = clase.capitalize()
    
    while clase != "Turista" and clase != "Ejecutivo":
        clase = input("Turista | Ejecutivo\nReingrese clase de vuelo: ")

    return clase


def validar_fecha():
    año = int(input("Ingrese año: "))
    mes = int(input("Ingrese mes (numerico): "))
    dia = int(input("Ingrese dia: "))
    
    while año < 2024:
        año = input("Reingrese año: ")
    
    while mes < 1 or mes > 12:
        mes = input("Reingrese mes (numerico): ")

    while dia < 1 or dia > 31:
        dia = input("Reingrese dia: ")

    año = str(año)
    
    mes = str(mes)
    
    dia = str(dia)
    
    if len(dia) == 1:
        dia = "0" + dia

    if len(mes) == 1:
        mes = "0" + mes
    
    fecha = año + mes + dia

    return fecha


def alta_pasajero(lista:list):
    id = obtener_maximo(lista, "Id") + 1
    aerolinea = validar_aerolinea()
    nombre = validar_nombre()
    dni = validar_dni()
    precio = validar_precio()
    origen = validar_origen()
    destino = validar_destino()
    
    while destino == origen:
        print("Las ciudades de origen y destino no pueden coincidir.\n")
        destino = validar_destino()

    clase = validar_clase()
    fecha = validar_fecha()

    lista.append({
            "Id": id,
            "Aerolinea": aerolinea,
            "Apellido_Nombre_Pasajero": nombre,
            "DNI_Pasajero": dni,
            "Precio": precio,
            "Origen": origen,
            "Destino": destino,
            "Clase": clase,
            "Fecha": fecha
        },)


def modificar_pasajero(lista:list):
    for pasajero in lista:
        if len(pasajero) == 1:
            print(f"Id: {pasajero["Id"]} | Pendiente de asignacion.\n") 
        else:             
            print(f"Id: {pasajero["Id"]} | Nombre completo: {pasajero["Apellido_Nombre_Pasajero"]}.\n")

    a_modificar = int(input("\nIngrese el Id del pasajero que desea modificar: "))
    continuar = True

    for pasajero in lista:       
        if pasajero["Id"] == a_modificar and len(pasajero) != 1:
            while continuar:
                print("\nMenu de modificacion:\n\n1.-Modificar DNI.\n2.-Modificar nombre.\n3.-Modificar fecha.\n4.-Salir.")
                opcion = int(input("\nIngrese la opcion deseada: "))
                
                match opcion:
                    case 1:
                        pasajero["DNI_Pasajero"] = validar_dni()
                        print("El DNI del pasajero ha sido modificado exitosamente.\n")
                    case 2:
                        pasajero["Apellido_Nombre_Pasajero"] = validar_nombre()
                        print("El nombre del pasajero ha sido modificado exitosamente.\n")
                    case 3:
                        pasajero["Fecha"] = validar_fecha()
                        ("La fecha del pasaje ha sido modificado exitosamente.\n\n")
                    case 4:
                        continuar = False
                    case _:
                        print("\nLa opcion ingresada no es valida.\n")


def borrar_pasajero(lista:list):
    for pasajero in lista:
        print(f"Id: {pasajero["Id"]} | Nombre completo: {pasajero["Apellido_Nombre_Pasajero"]}.\n")

    a_modificar = int(input("Ingrese el Id del pasajero que desea borrar: "))

    for pasajero in lista:
        if pasajero["Id"] == a_modificar:
            auxiliar =  pasajero["Id"]
            pasajero.clear()
            pasajero.update({"Id" :auxiliar})


def listar_pasajeros(lista:list):
    nueva_lista = lista
    for pasajero in nueva_lista:
        if len(pasajero) == 9:
            print(f"Fecha: {pasajero["Fecha"]} | Aerolínea: {pasajero["Aerolinea"]} | Clase: {pasajero["Clase"]} | Origen: {pasajero["Origen"]} | Destino: {pasajero["Destino"]} | Precio: {pasajero["Precio"]} | DNI: {pasajero["DNI_Pasajero"]} | Apellido y nombre: {pasajero["Apellido_Nombre_Pasajero"]}\n------------------------------------------------------------------------------------------------------------------------------------------")
        
        
"""
F – Hacer un submenú que realice lo siguiente:
1-Listar por pantalla los pasajes de menor y mayor precio.
2-Calcular y mostrar la cantidad de pasajes de un destino determinado, el mismo será ingresado por el usuario por consola.
3-Listar los pasajes ordenados por Fecha. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’). Este ítem debe ser realizado por el algoritmo de ordenamiento bubble sort (burbujeo).
4-Exportar a JSON la lista de pasajes, de acuerdo a la opción F 3.
5-Exportar a CSV la lista de pasajes, de acuerdo a la opción F 1.
"""

#1-Listar por pantalla los pasajes de menor y mayor precio.
    
def castear_precios(lista):
    for pasajero in lista:
        precio_casteado = pasajero["Precio"]
        precio_casteado = float(precio_casteado)
        pasajero["Precio"] = precio_casteado


def precio_min(lista:list):
    castear_precios(lista)
    bandera = True
    minimo = None
    
    for pasajero in lista:
        if bandera == True:
            minimo = pasajero["Precio"]
            bandera = False

        if pasajero["Precio"] < minimo:
            minimo = pasajero["Precio"]


    return minimo


#pasajeros = leer_json("Simulacro\data.json", "pasajeros")


def precio_max(lista:list):
    castear_precios(lista)
    bandera = True
    maximo = None
    
    for pasajero in lista:
        if bandera == True:
            maximo = pasajero["Precio"]
            bandera = False

        if pasajero["Precio"] > maximo:
            maximo = pasajero["Precio"]

    return maximo

def retornar_max_min(lista):
    maximo = precio_max(lista)
    minimo = precio_min(lista)
    castear_precios(lista)

    for pasajero in lista:
        if pasajero["Precio"] == maximo:
            pasaje_max = f"Pasaje mas caro:\n\nFecha: {pasajero["Fecha"]} | Aerolínea: {pasajero["Aerolinea"]} | Clase: {pasajero["Clase"]} | Origen: {pasajero["Origen"]} | Destino: {pasajero["Destino"]} | Precio: {str(pasajero["Precio"])} | DNI: {pasajero["DNI_Pasajero"]} | Apellido y nombre: {pasajero["Apellido_Nombre_Pasajero"]}\n"

    for pasajero in lista:
        if pasajero["Precio"] == minimo:
            pasaje_min = f"Pasaje mas barato:\n\nFecha: {pasajero["Fecha"]} | Aerolínea: {pasajero["Aerolinea"]} | Clase: {pasajero["Clase"]} | Origen: {pasajero["Origen"]} | Destino: {pasajero["Destino"]} | Precio: {str(pasajero["Precio"])} | DNI: {pasajero["DNI_Pasajero"]} | Apellido y nombre: {pasajero["Apellido_Nombre_Pasajero"]}"

    mensaje = pasaje_max + "\n" + pasaje_min
    
    print(mensaje)


#2-Calcular y mostrar la cantidad de pasajes de un destino determinado, el mismo será ingresado por el usuario por consola.

def cantidad_pasajes(lista):
    destino = input("Buenos Aires | Madrid | París | Miami | Roma | Tokio\n\nIngrese el destino a calcular: ")
    destino = destino.lower()
    destino = destino.capitalize()
    
    if destino == "Buenos aires":
        destino = "Buenos Aires"
    
    if destino == "Paris":
        destino = "París"
    
    contador_destino = 0

    for pasajero in lista:
        if pasajero["Destino"] == destino:
            contador_destino += 1
    
    print(f"\nLa cantidad de pasajes encontrados hacia {destino} es: {contador_destino} pasajes.\n")


#3-Listar los pasajes ordenados por Fecha. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’). Este ítem debe ser realizado por el algoritmo de ordenamiento bubble sort (burbujeo).

def castear_fechas(lista):
    for pasajero in lista:
        fecha_casteado = pasajero["Fecha"]
        fecha_casteado = int(fecha_casteado)
        pasajero["Fecha"] = fecha_casteado


def ordenar_lista_ascendente(lista):
    nueva_lista = lista
    for i in range(len(nueva_lista) -1):
        for j in range(i + 1, len(nueva_lista)):
            if nueva_lista[i]["Fecha"] > nueva_lista[j]["Fecha"]:
                auxiliar = nueva_lista[i]
                nueva_lista[i] = nueva_lista[j]
                nueva_lista[j] = auxiliar
    
    return nueva_lista

def ordenar_lista_descendente(lista):
    nueva_lista = lista

    for i in range(len(nueva_lista) -1):
        for j in range(i + 1, len(nueva_lista)):
            if nueva_lista[i]["Fecha"] < nueva_lista[j]["Fecha"]:
                auxiliar = nueva_lista[i]
                nueva_lista[i] = nueva_lista[j]
                nueva_lista[j] = auxiliar

    return nueva_lista

def asc_desc_fecha(lista):
    nueva_lista = lista
    criterio = input("\nASC = Ascendente\nDESC = Descendente\nIngrese el criterio del ordenamiento: ").upper()
    
    while criterio != "ASC" and criterio != "DESC":
        criterio = input("\nASC = Ascendente\nDESC = Descendente\nReingrese el criterio del ordenamiento:")
    
    castear_fechas(nueva_lista)
    
    if criterio == "ASC":
        ordenar_lista_ascendente(nueva_lista)

    if criterio == "DESC":
        ordenar_lista_descendente(nueva_lista)

    listar_pasajeros(nueva_lista)

#4-Exportar a JSON la lista de pasajes, de acuerdo a la opción F 3.


def generar_json(nombre:str, lista:list, clave:str):
    data = {clave: lista}
    
    with open(nombre, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False )


def generar_json_fecha(lista):
    nueva_lista = []
    criterio = input("\nASC = Ascendente\nDESC = Descendente\nIngrese el criterio del ordenamiento: ").upper()
    
    while criterio != "ASC" and criterio != "DESC":
        criterio = input("\nASC = Ascendente\nDESC = Descendente\nReingrese el criterio del ordenamiento:")
    
    castear_fechas(lista)

    if criterio == "ASC":
        ascendente = ordenar_lista_ascendente(lista)
        nueva_lista.append(ascendente)

    if criterio == "DESC":
        descendente = ordenar_lista_descendente(lista)
        nueva_lista.append(descendente)

    generar_json("json.json", nueva_lista, "pasajeros")
        


#5-Exportar a CSV la lista de pasajes, de acuerdo a la opción F 1.

def guardar_archivo(archivo_nombre:str, contenido_archivo:str):
    if len(contenido_archivo) == 0:
        retorno = False
    else:
        with open(archivo_nombre, 'w+') as archivo:
            archivo.write(contenido_archivo)
        
        retorno = f"Se creó el archivo: {archivo_nombre}"

    return retorno


def listar_por_precio(lista):
    maximo = precio_max(lista)
    minimo = precio_min(lista)
    castear_precios(lista)
    texto_csv = ""

    for pasajero in lista:
        if pasajero["Precio"] == maximo:
            maximo = f"Fecha: {pasajero["Fecha"]} | Aerolínea: {pasajero["Aerolinea"]} | Clase: {pasajero["Clase"]} | Origen: {pasajero["Origen"]} | Destino: {pasajero["Destino"]} | Precio: {pasajero["Precio"]} | DNI: {pasajero["DNI_Pasajero"]} | Apellido y nombre: {pasajero["Apellido_Nombre_Pasajero"]}"
    
    
        if pasajero["Precio"] == minimo:
            minimo = f"Fecha: {pasajero["Fecha"]} | Aerolínea: {pasajero["Aerolinea"]} | Clase: {pasajero["Clase"]} | Origen: {pasajero["Origen"]} | Destino: {pasajero["Destino"]} | Precio: {pasajero["Precio"]} | DNI: {pasajero["DNI_Pasajero"]} | Apellido y nombre: {pasajero["Apellido_Nombre_Pasajero"]}"

    maximo = str(maximo)
    minimo = str(minimo)

    maximo = maximo.replace("|", ",")
    minimo = minimo.replace("|", ",")

    texto_csv = maximo + "\n" + minimo
    
    guardar_archivo("csv.csv", texto_csv)


def submenu(lista):

    continuar = True

    while continuar:

        print("\nSubmenu:\n\n1-Listar por pantalla los pasajes de menor y mayor precio.\n2-Calcular y mostrar la cantidad de pasajes de un destino determinado.\n3-Listar los pasajes ordenados por Fecha.\n4-Exportar a JSON la lista de pasajes (Ordenados por fecha ASC o DESC).\n5-Exportar a CSV la lista de pasajes.(Precio Max y Min)\n6-Salir.\n")

        opcion = int(input("Ingrese la opcion deseada: "))
        match opcion:
            case 1:
                system('cls')
                print(retornar_max_min(lista))

            case 2:
                system('cls')
                cantidad_pasajes(lista)

            case 3:
                system('cls')
                asc_desc_fecha(lista)

            case 4:
                system('cls')
                generar_json_fecha(lista)

            case 5:
                system('cls')
                listar_por_precio(lista)

            case 6:
                system('cls')
                continuar = False

            case _:
                print("La opcion ingresada no es valida.")