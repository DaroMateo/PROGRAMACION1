# 1) Desarrolle una función que cuente las letras vocales de una cadena de caracteres pasada por
# parámetro.
palabra = ("palabra")
vocales = ["a", "e", "i", "o", "u"]
def contar_vocales(cadena:str, caracter_a_contar:str) -> int:
    """
    Recibe una cadena de caracteres y un caracter a contar, y devuelve cuántas veces aparece ese caracter en la cadena.
    :param cadena: Cadena de caracteres a recorrer
    :param caracter_a_contar: Caracter cuya cantidad se va a contar
    :return: Cantidad de veces que el caracter_a_contar se encuentra en la cadena
    """
    cadena_minuscula = cadena.lower()
    contador = 0
    for letra in caracter_a_contar:
        contador += cadena_minuscula.count(letra)
    return contador
#print(f"La palabra {palabra} tiene {contar_vocales(palabra)} vocales")
# 2) Desarrolle una función que reciba una cadena de caracteres y un separador por parámetro,
# luego limpiara los espacio vacíos que se encuentren al principio y al final de la cadena de
# caracteres y reemplazará los espacios en el medio de la misma utilizando el separador
# recibido
palabra_1 = ("      Hola mundo que tal      ")
separador = ("-")
def limpiar_cadena(cadena:str, separador:str) -> str:
    """
    Recibe una cadena de caracteres y un separador por parámetro, luego 
    - Limpia los espacios vacíos que se encuentren al principio y al final de la cadena de caracteres
    - Reemplaza los espacios en el medio de la cadena utilizando el separador recibido
    :param cadena: Cadena de caracteres a recorrer
    :param separador: Caracter que se va a utilizar como separador
    :return: Cadena de caracteres con los espacios reemplazados
    """
    cadena_limpia = cadena.strip()
    resultado = cadena_limpia.replace(" ", separador)
    return resultado
#print(f"La palabra {palabra_1} limpiada es {limpiar_cadena(palabra_1, separador)}")

# 3) Desarrolle una función que cuente los caracteres de una cadena de caracteres con excepción
#del espacio.
palabra_2 = " la ola de calor que hay del dia de hoy"
def contar_caracteres(cadena:str) -> int:
    """
    Recibe una cadena de caracteres y devuelve la cantidad de caracteres que tiene,
    exceptuando los espacios.
    :param cadena: Cadena de caracteres a recorrer
    :return: Cantidad de caracteres que tiene la cadena, exceptuando los espacios
    """
    contador_caracteres = len(cadena) - cadena.count(" ")
    return contador_caracteres

#print(f"La palabra {palabra_2} tiene {contar_caracteres(palabra_2)} caracteres")

#4) Desarrolle una función que cuente las palabras de una cadena de caracteres.

def contar_palabras(cadena:str) -> int:
    """
    Recibe una cadena de caracteres y devuelve la cantidad de palabras que tiene,
    exceptuando los espacios.
    :param cadena: Cadena de caracteres a recorrer
    :return: Cantidad de palabras que tiene la cadena, exceptuando los espacios
    """
    return len(cadena.split())

# print(f"La palabra {palabra_2} tiene {contar_palabras(palabra_2)} palabras")

# 5) Desarrolle la función “normalizar_texto()”, que recibirá por parámetro una cadena y un
# criterio, la misma deberá limpiar la cadena recibida de cualquier espacio extra que se
# encuentre al principio o al final de la cadena, y dependiendo del criterio recibido la
# transformará a mayúsculas, minúsculas o un título.
def validar_cadena(msj:str, lista_validacion:list) -> str:
    """
    Recibe un mensaje y una lista de opciones, y devuelve la cadena ingresada por el usuario
    :param msj: Mensaje a mostrar al usuario
    :param lista_validacion: Lista de opciones a elegir
    :return: Cadena de caracteres seleccionada por el usuario
    """
    while True:
        cadena = input(msj)
        if cadena in lista_validacion:
            return cadena
def normalizar_texto(cadena:str, criterio:str) -> str:
    """
    Recibe una cadena de caracteres y un criterio, la misma deberá limpiar la cadena recibida de cualquier espacio extra que se encuentre al principio o al final de la cadena,
    y dependiendo del criterio recibido la transformara a mayúsculas, minúsculas o un título.
    :param cadena: Cadena de caracteres a recorrer
    :param criterio: Criterio de transformación de la cadena
    :return: Cadena de caracteres transformada
    """
    cadena_limpia = cadena.strip()
    match criterio:
        case "mayuscula":
            resultado = cadena_limpia.upper()
        case "minuscula":
            resultado = cadena_limpia.lower()
        case "capitalizar":
            resultado = cadena_limpia.capitalize()
        case "title":
            resultado = cadena_limpia.title()
        case _:
            resultado = cadena_limpia    
    return resultado

# validar = validar_cadena("Criterio: ", ["mayuscula", "minuscula", "capitalizar", "title"])

# print(normalizar_texto(palabra_2, validar))

# 6) Desarrolle la función “personalizar_titulo()”, que recibirá por parámetro una cadena y le dará
# formato de título, con excepción de las siguientes palabras que deben aparecer en letra
# minúscula: ‘y’, ‘el’, ‘la’, ‘de’, 'del.
lista_valida = ["y", "el", "la", "de", "del"]
def personalizar_titulo(cadena:str) -> str:
    """
    Recibe una cadena de caracteres y le da formato de título, con excepción de las siguientes palabras que deben aparecer en letra
    minúscula: 'y', 'el', 'la', 'de', 'del.
    
    :param cadena: Cadena de caracteres a recorrer
    :return: Cadena de caracteres con formato de título
    """
    
    palabras_minusculas = ['y', 'el', 'la', 'de', 'del']
    palabras = (cadena.lower()).split()
    resultado = []
    for palabra in palabras:
        if palabra in palabras_minusculas:
            resultado.append(palabra)
        else:
            resultado.append(palabra.capitalize())
    return ' '.join(resultado)

#print(f"La palabra {palabra_2} personalizada es {personalizar_titulo(palabra_2)}")

# 7) Desarrolle la función “resumir_texto()”, que recibirá por parámetro una cadena de caracteres
# larga y un entero que representa la cantidad máxima de palabras. Si la cadena supera la
# cantidad máxima de palabras deberá retornar la cadena con la cantidad máxima de palabras
# y tres puntos al final “...”, si no lo supera, devolverá la cadena original si modificarla.

def resumir_texto(cadena:str, max_palabras:int) -> str:
    """
    Recibe una cadena de caracteres y un entero que representa la cantidad máxima de palabras. Si la cadena supera la
    cantidad máxima de palabras deberá retornar la cadena con la cantidad máxima de palabras
    y tres puntos al final “...”, si no lo supera, devolverá la cadena original si modificarla.
    :param cadena: Cadena de caracteres a recorrer
    :param max_palabras: Cantidad máxima de palabras
    :return: Cadena de caracteres resumida
    """
    cantidad_palabras = len(cadena.split())
    if cantidad_palabras > max_palabras:
        palabras = cadena.split()[:max_palabras]
        retorno = " ".join(palabras)
        resultado = retorno + "..."
    else:
        resultado = cadena
    return resultado

# print(resumir_texto(palabra_2, 3))

# 8) Desarrolle la función “convertir_a_snake_case()”, que recibirá por parámetro una cadena de
# caracteres y la convertirá a snake case, eliminando todos los espacios innecesarios,
# convirtiendo las letras a minúsculas y reemplazando los espacios entre palabras por guiones
# bajos.
def convertir_a_snake_case(cadena:str) -> str:
    cadena_minus_limpia = cadena.lower().strip()
    lista_palabras = cadena_minus_limpia.split()
    cadena_snake = "_".join(lista_palabras)
    return cadena_snake

cadena = "     HOLA     MUNDO      "
print(convertir_a_snake_case(cadena))

# 9) Desarrolle la función “contar_letras_unicas()”, que recibirá por parámetro una cadena de
# caracteres y se encargará de contar cuantas letras únicas contiene. Las letras mayúsculas y
# minúsculas cuentan como 1.

def contar_letras_unicas(texto):
    texto = texto.lower()  # Convertir todo a minúsculas para ignorar mayúsculas/minúsculas
    letras_vistas = []  # Lista para almacenar letras únicas encontradas
    
    for caracter in texto:
        # Verificar si el carácter es una letra y no está ya en letras_vistas
        if caracter.isalpha() and caracter not in letras_vistas:
            letras_vistas.append(caracter)  # Añadir la letra única encontrada
    
    return len(letras_vistas)

print(contar_letras_unicas(cadena))

#print(contar_letras_unicas(palabra_2))
# 10) Desarrolle la función “resaltar_palabra()”, que recibirá por parámetro una texto y una palabra
# y reemplazará todas las ocurrencias de esa palabra por la versión mayúscula de la misma,
# devolviendo el texto resultante.



