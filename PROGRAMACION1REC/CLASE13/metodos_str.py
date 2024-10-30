# saludo = ".hOLa MuNdO. 23"

# # Upper (Mayusculas)
# resultado = saludo.upper()
# print("Resultado upper:", resultado, "Original:", saludo)

# print("=============================================")
# # Lower (minusculas)
# resultado = saludo.lower()
# print("Resultado lower:", resultado, "Original:", saludo)

# print("=============================================")
# # Capitalize (primera letra en mayusculas y el resto en minusculas)
# resultado = saludo.capitalize()
# print("Resultado capitalize:", resultado, "Original:", saludo)

# print("=============================================")
# # Title (primera letra de cada palabra en mayusculas y el resto en minusculas)
# resultado = saludo.title()
# print("Resultado title:", resultado, "Original:", saludo)


# saludo = " ,|| ,|aaaaaaaaaaaa| ,hola  ,  mundo, , ,| , || ,,aaaaaaa| , "
# # Strip (limpia la cadena al principio y al final de algun caracter innecesario)             
# resultado = saludo.strip(" ,|a")
# # resultado = resultado.strip(",") # "hola     mundo"
# print(resultado, "***")

# saludo = "Hola...mundo...ooooooooooooooo!"
# # Replace (reemplaza caracteres o una secuen de caracteres)
# resultado = saludo.replace("o", "x")
# print(resultado)

# Split (retorna una lista con las palabras del string)
# saludo = "Hola    mundo  pepe      juan"
# lista_resultante = saludo.split()
# saludo = "Hola, mundo, pepe, juan" # CSV 
# lista_resultante = saludo.split(", ", 2)
# print(lista_resultante)


# Join (une los elementos de un objeto iterable utilizando un separador)
# separador = "-"
# #lista_palabras = ["Hola", "Mundo", "Juan", "Pepe"]
# #resultado = separador.join(lista_palabras)    # Hola-Mundo-Juan-Pepe
# saludo = "Hola mundo!"
# resultado = separador.join(saludo) 
# print(resultado)


# ZFill (completa una cadena de caracteres con 0s a la izquierda)
# numero_factura = "AAAAAA"
# resultado = numero_factura.zfill(8) # 00AAAAAA
# print(resultado)


# isAlgo  (Sirven para validaciones, devuleven booleanos)
# saludo = "AAaB15"
# #resultado = saludo.isalpha() # Alfabeticos
# #resultado = saludo.isdecimal() # Numerica (decimal, numeric y digit)
# resultado = saludo.isalnum() # Alfanumericos
# print(resultado)


# Count (cuenta las ocurrencias de algun valor)
# saludo = "Hola mundo 1112223444 ....."
# print(saludo.count(" ", 6, 30))


# Find (busca un valor dentro del string, si no lo encuentra retorna -1)
# saludo = "Hola mundo"
# print(saludo.find("mundo"))


# Index (hace lo mismo que Find, pero al no encontrar el valor, arroja una excepcion)
# saludo = "Hola mundo"
# print(saludo.index("Hola"))


# Center (agrega espacios a la derecha y izquierda del string para "centrarlo")
# saludo = "Hola mundo"
# resultado = saludo.center(110)
# print(resultado)


# Swapcase (invierte minusculas y mayusculas)
# saludo = "Hola mundo"
# print(saludo.swapcase()) # "hOLA MUNDO"
