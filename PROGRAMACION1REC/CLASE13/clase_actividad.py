# 1) Desarrolle una función que cuente las letras vocales de una cadena de caracteres pasada por parámetro.

cadena = "hopawkloweeeiioop"
vocales = "aeiou"
def contar_caracteres(cadena:str, caracter_a_contar:str)->int:
    cadena_minuscula = cadena.lower()
    ocurrencias = 0
    for letra in caracter_a_contar:
        ocurrencias += cadena_minuscula.count(letra)
    return ocurrencias

# resultado = contar_caracteres(cadena, vocales)
# print(f"la cantidad de vocales es: {resultado}")

#2) Desarrolle una función que reciba una cadena de caracteres y un separador por parámetro, 
# luego limpiara los espacio vacíos que se encuentren al principio y al final de la cadena de caracteres 
# y reemplazará los espacios en el medio de la misma utilizando el separador recibido.


def limpiar_y_reemplazar(cadena:str, separador:str)->str:
    cadena_limpia = cadena.strip()
    resultado = cadena_limpia.replace(" ", separador)
    return resultado

# cadena = "    hola      que tal     "
# separador = "-"
# prueba = limpiar_y_reemplazar(cadena,separador)
# print(prueba)

#3) Desarrolle una función que cuente los caracteres de una cadena de caracteres con excepción
#del espacio.

def contar_caracteres(cadena:str)->int:
#    contador_caracteres = len(cadena.replace(" ", ""))
    contador_caracteres = len(cadena) - cadena.count(" ")
    return contador_caracteres

# cadena = "    hola mundo     "

# prueba = contar_caracteres(cadena)
# print(prueba)   


#4) Desarrolle una función que cuente las palabras de una cadena de caracteres

def contar_palabras (cadena:str)->int:
    return len(cadena.split())

# cadena = "    hola mundo hola     "
# prueba = contar_palabras(cadena)
# print (prueba)

#5) Desarrolle la función “normalizar_texto()”, que recibirá por parámetro una cadena y un
#criterio, la misma deberá limpiar la cadena recibida de cualquier espacio extra que se
#encuentre al principio o al final de la cadena, y dependiendo del criterio recibido la
#transformará a mayúsculas, minúsculas o un título.


def validar_cadena(msj:str, lista_validacion:list)->str:
    cadena=input(msj)
   # if cadena in lista_validacion:
    #    print ("Existe")
   # else:
     #   print("No existe")

    #while cadena not in lista_validacion:
       # cadena=input(msj)
    while lista_validacion.count(cadena)== 0:
        cadena=input(msj)
    return cadena
    


def normalizar_texto(cadena:str, criterio:str)->str:
    cadena_limpia=cadena.strip()
    match criterio:
        case "mayus":
            retorno=cadena_limpia.upper()
        case "minus":
            retorno=cadena_limpia.lower()
        case "capit":
            retorno=cadena_limpia.capitalize()
        case "title":
            retorno=cadena_limpia.title()
        case _:
            retorno=cadena_limpia
    return retorno

#criterio_ingresado=validar_cadena("Ingrese dato: ",["mayus","minus","capit","title"])
#resultado=normalizar_texto("  Hola  Mundo   ",criterio_ingresado)
#print(resultado)


#6)Desarrolle la función “personalizar_titulo()”, que recibirá por parámetro una cadena y le dará
#formato de título, con excepción de las siguientes palabras que deben aparecer en letra
#minúscula: ‘y’, ‘el’, ‘la’, ‘de’ , 'del'.
lista_valida=["y","el","la","de","del"]
def personalizar_titulo(cadena:str,lista:list)->str:
    cadena_lower=cadena.lower()
    lista_de_palabras=cadena_lower.split()
    for i in range(len(lista_de_palabras)):
        if lista.count(lista_de_palabras[i])==0:
            lista_de_palabras[i]=lista_de_palabras[i].title()
    resultado=" ".join(lista_de_palabras)
    return resultado

# resultado=personalizar_titulo("HOLA COMO ESTAS Del EsTomAgO.", lista_valida)
# print(resultado)

#  7) Desarrolle la función “resumir_texto()”, que recibirá por parámetro una cadena de caracteres
#  larga y un entero que representa la cantidad máxima de palabras. Si la cadena supera la
#  cantidad máxima de palabras deberá retornar la cadena con la cantidad máxima de palabras
#  y tres puntos al final “...”, si no lo supera, devolverá la cadena original si modificarla.

def resumir_texto(cadena:str, max:int)->str:
    cantidad_palabras = len(cadena.split())
    
    if cantidad_palabras > max:
        lista_palabras = cadena.split()
        lista_palabras = lista_palabras[0:max]
        
        retorno = " ".join(lista_palabras)
        retorno += "..."
    
    else:
        retorno = cadena
    
    return retorno

# texto_resumido = resumir_texto("pepe pepitp pepe pepe pepe pepe pepe pepe pepe pepe pepe", 20)
# print(texto_resumido)


# 8) Desarrolle la función “convertir_a_snake_case()”, que recibirá por parámetro una cadena de
#  caracteres y la convertirá a snake case, eliminando todos los espacios innecesarios,
#  convirtiendo las letras a minúsculas y reemplazando los espacios entre palabras por guiones
#  bajos.

def convertir_a_snake_case(cadena:str)->str:
    
    cadena_minus_limpia = cadena.lower().strip()
    
    # cadena_snake_case = cadena_minus_limpia.replace(" ", "_")
    
    lista_palabras = cadena_minus_limpia.split()
    
    cadena_snake_case = "_".join(lista_palabras)
  
    return cadena_snake_case

# cadena = convertir_a_snake_case("          HOLA       MUNDO     pepe JUAN        JOSE          FEDE ")
# print(cadena)