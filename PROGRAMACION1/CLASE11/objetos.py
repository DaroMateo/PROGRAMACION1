# POO(objetos)

# DICCIONARIO( es un tipo de dato que gurada informacion por clave + valor) pueden tener listas de lo que sea el dato es random {diccionario} (tupla) [lista]
"""
d_personajes = {
    'nombres' : 'Dario' ,
    'apellido' : 'Mateo' ,
    'edad' : '27' ,
    'genero' : 'M'
}

print(d_personajes['nombres'])
"""

# Pisarlos

"""
d_personajes['nombres'] = 'Leonel'

d_personajes.update9{'apellido' : 'Messi'}
d_personajes.pop('apellido') #remueve el dato de apellido
"""
"""
for carcaracteristica in d_personajes:
    print(d_personajes[carcaracteristica])

for carcaracteristica in d_personajes.values():
    print(carcaracteristica)

for carcaracteristica in d_personajes.items():
    print(carcaracteristica)
"""

#CLASE (class) primer letra siempre con mayuscula ej: class Personaje; si repetis el id no haces diferencia en la clase
#personajeuno = Personaje_principal(0,'dario','mateo',27)
#  objeto            clase

#caracteristicas o atributos
class Personaje_principal: 
    tipo = 'Personaje Principal'
    def __init__(self,id,nombre,apellido,cantidad,edad,nacionalidad) -> None:
        self.id = id
        self._nombre = nombre # "_" proteje el atributo o dato y solamente lo ven sus herederos
        self.__apellido = apellido # "__" privado el atributo o dato y solamente lo ven sus herederos
        self.edad = edad
        self.__cantidad = 5
        self.__nacionalidad =  'Argentina'
        self.__lista =[self,id,nombre,apellido]

#METODOS SON FUNCIONES UN METODO DE DESCRIPCION
    def descripcion(self):
        return '{0}-{1}' .format(self._nombre, self.__apellido)
    def get_nombre(self):
        return 'Mi nombre es: {0}' .format(self._nombre) 
    
    @property # se comporta como un atributo pero es una funcion
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self):
        if (self._nombre.lower() != "dario"):
            return self._nombre

    
personajeUno = Personaje_principal(0,'dario','mateo',27,45,'argentina')
personajeDos = Personaje_principal(1,'pedro','perez',25,45,'chileno')
personajeTres = Personaje_principal(2,'juan','perez',25,25,'chileno')

"""
print(personajeUno.nombre,personajeUno.apellido,personajeUno.edad)
print(personajeDos.tipo)
print(personajeTres.nombre)
"""

print(personajeUno.get_nombre())
print(personajeDos.nombre)
print(personajeTres.descripcion())

#propertys
@property # se comporta como un atributo pero es una funcion
def nombre(self):
    return self._nombre

#getters
#setters setear o modificar 
@nombre.setter
def nombre(self):
    if (self._nombre.lower() != "dario"):
        return self._nombre
#Metodos Dunder ej: __init__, __str__ siemrpe tiene que retornar algo
def __str__(self) -> str:
    return '{0}-{1}' .format(self._nombre, self.__apellido)
print(personajeUno)



def __len__(self):
    return len(self.__cantidad)
print(len(personajeUno))

#getitem inicializa la lista
index= 0 # innecesario solo para el ejemplo
def __getitem__(self):
    return self.lista[index]
for i in range(4):
    print(personajeUno[i])

#setitem setear
def __setitem__(self, index, value):
    self.lista[index] = value

for i in range(4):
    print(personajeUno[i])


#__contains__ retorna True o False

def __contains__(self, item):
    return item in self.__lista
print('dario' in personajeUno)

#__delitem__ borrar el item

def __delitem__(self, index):    
    self.__lista.pop(index)

for i in range(3):
    print(personajeUno[i])

#__iter__  retorna un iterador

def __iter__(self):
    for index in range(len(self.__lista)):
        yield self.__lista[index]

for i in personajeUno:
    print(i)

