'''Crear la función generar_json() que va a recibir el nombre y extensión
de donde se ubica el archivo a guardar (Ruta absoluta o relativa) , la
lista de los superhéroes y el nombre de la lista.
Si la lista no está vacía debería guardar en un diccionario de una sóla
clave la lista de superhéroes,el nombre de clave debería ser la del
tercer parámetro que sería el nombre de la lista.'''

import json
from PROGRAMACION1.MARVEL.funcionesmarvel import *

def generar_json(ruta:str, lista:list, nombre:str):
    data = {nombre: lista}#lista / valor 
    #otra forma:
    #data = {}
    #data [clave] = lista

    with open(data, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False )
    
generar_json('Daro.json', lista_personajes, 'personajes')