""""
El código debe desarrollarse dentro un módulo llamado “Boligrafo” en una
clase llamada Bolígrafo.
● Los atributos serán los siguientes:
- capacidad_tinta_maxima
- grosor_punta
- color
- cantidad_tinta
● Al crearse una nueva instancia de la clase Bolígrafo, la misma siempre se creará con
una capacidad de tinta máxima de 100 (El constructor no recibirá este parámetro)
"""
"""
Al crearse una nueva instancia de la clase Bolígrafo la cantidad de tinta siempre
comenzará siendo de 80 (El constructor no recibirá este parámetro)
● Al crearse una nueva instancia de la clase Bolígrafo se podrá elegir el color del
mismo (El constructor recibirá un string indicando el color y lo guardará en el
atributo)
● Al crearse una nueva instancia de la clase Bolígrafo se podrá elegir el grosor de la
punta del mismo (El constructor recibirá un string indicando el grosor y lo guardará
en el atributo)


Los métodos de instancia serán los siguientes:
● escribir(texto)
- Deberá validar si el bolígrafo cuenta con la tinta suficiente para escribir el
texto: La tinta a ser gastada corresponde a la cantidad de caracteres (Ej: el
texto “hola” gasta 4 de tinta)
- En caso de contar con la tinta suficiente, deberá restarse la cantidad del
atributo cantidad_tinta y devolver una cadena con el texto recibido por
parámetro.

- En caso de no contar con la tinta suficiente deberá retornar la cadena
“No
alcanza la tinta”.

recargar(cantidad)
-Deberá sumarse la cantidad de tinta recibida por parámetro al atributo
cantidad_tinta.
-Deberá validarse que la tinta recargada no supere el valor establecido por el
atributo cantidad_tinta_maxima. (Ej: Si el bolígrafo tiene 50 de tinta y el
parámetro cantidad es 60 debe establecerse cantidad_tinta en 100, no en
110, pues ese es el valor establecido como máximo en el atributo
cantidad_tinta_maxima.

-Si la cantidad recargada no excede el máximo deberá retornarse la cadena
“Lapicera recargada”.
- Si la cantidad recargada excede el máximo deberá retornarse la cadena “Se
recargó la lapicera y sobró __ cantidad de tinta. (Rellenar el espacio con el
valor que se haya excedido)

"""

class Boligrafo:
    def __init__(self,grosor_punta,color):
        self.__grosor_punta = grosor_punta
        self.__color = color
        self.__capacidad_tinta_maxima = 100
        self.__cantidad_tinta = 80
    
    @property
    def grosor_punta(self):
        return self.__grosor_punta
    
    @property
    def color(self):
        return self.__color
    
    @property
    def capacidad_tinta_maxima(self):
        return self.__capacidad_tinta_maxima
    
    @property
    def cantidad_tinta(self):
        return self.__cantidad_tinta
    
    def descripcion (self):
        return "{0}-{1}-{2}-{3}".format(self.__grosor_punta,self.__color,self.__cantidad_tinta,self.__capacidad_tinta_maxima)
    
    def escribir(self,texto):
        if self.__cantidad_tinta >= len(texto):
            self.__cantidad_tinta = self.__cantidad_tinta - len(texto)
            mensaje = texto
        else:
            mensaje = "No alcanza la tinta"

        return mensaje

    def recargar (self,cantidad):

        auxiliar = cantidad + self.__cantidad_tinta

        if auxiliar > self.__capacidad_tinta_maxima:
            self.__cantidad_tinta = 100
            mensaje = f'Se recargó la lapicera y sobró {auxiliar - self.__capacidad_tinta_maxima} cantidad de tinta'
        else:
            self.__cantidad_tinta = auxiliar
            mensaje = f'Lapicera recargado {self.__cantidad_tinta}'

        return mensaje

 
boligrafo_azul = Boligrafo("Grueso","Azul")

print(boligrafo_azul.descripcion())

print(boligrafo_azul.escribir('hola'),boligrafo_azul.cantidad_tinta)

print(boligrafo_azul.recargar(20))
print(boligrafo_azul.recargar(30))





