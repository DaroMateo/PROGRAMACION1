class Personaje_principal:
    tipo = 'Personaje_principal'
    def __init__(self, id, nombre, apellido, edad, cantidad, nacionalidad = 'Argentina') -> None:
        self.id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__candidad = 5
        self.__nacionalidad = nacionalidad
        self._lista= [id, nombre, apellido, edad]
    
    def __getitem__(self,index) -> str:
        return self._lista[index]
    
    def __setitem__(self,index, value):
        self._lista[index] = value
        
    def __contains__(self,item):
        return item in self._lista
    
    def __delitem__(self,index):
        return self._lista.pop(index)

    def __iter__(self):
        for index in range(len(self._lista)):
            yield self._lista[index]
    
    def descripcion(self):
        return '{0}-{1}'.format(self.__nombre,self.__apellido)
    
    def get_nombre(self):
        return 'Mi nombre es: {0}'.format(self.__nombre)
    
    @property
    def nombre(self):
        return 'Mi nombre es: {0}'.format(self.__nombre)
    @nombre.setter
    def nombre(self, nombre):
        if(nombre != 'Claudio'):
            self.__nombre = nombre
        else:
            self.__nombre = 'None'
            
    @property
    def nacionalidad(self):
        return self.__nacionalidad
            
    def __str__(self) -> str:
        return '{0}-{1}'.format(self.__nombre,self.__apellido)
    
    def __len__(self) -> int:
        return self.__candidad

        
        
personajeUno = Personaje_principal(0, 'ricky', 'bartoncello', 23, 4)
personajeTres = Personaje_principal(3, 'juan', 'perez', 25, 4,  'uruguay')
personajeDos = Personaje_principal(1, 'Leonel', 'Messi', 37, 8)

#print(personajeUno.get_nombre())
'''print(len(personajeUno))

personajeUno.nombre = 'Claudo'''

'''print(personajeUno.nacionalidad)
print(personajeDos.nacionalidad)
print(personajeTres.nacionalidad)'''

for i in personajeUno:
    print(i)

personajeUno[3] = 'cambio'

'''for i in range(4):
    print(personajeUno[i])
    
    
print('ricky' in personajeUno)
print('cambio' in personajeUno)
print('messi' in personajeUno)'''

'''del personajeUno[1]

for i in range(3):
    print(personajeUno[i])'''
    
    
class Personaje_tres:
    tipo = 'Personaje_tres'
    def __init__(self) -> None:
        self.id = 0
        self.__nombre = 'Pedro'
        self.__apellido = 'Gonzalez'
        self.__edad = 56
        self.__candidad = 2
        self.__nacionalidad = 'usa'
    
    def descripcion(self):
        return '{0}-{1}'.format(self.__nombre,self.__apellido)
    
    def get_nombre(self):
        return 'Mi nombre es: {0}'.format(self.__nombre)
    
    @property
    def nombre(self):
        return 'Mi nombre es: {0}'.format(self.__nombre)
    @nombre.setter
    def nombre(self, nombre):
        if(nombre != 'Claudio'):
            self.__nombre = nombre
        else:
            self.__nombre = 'None'
            
    @property
    def nacionalidad(self):
        return self.__nacionalidad
            
    def __str__(self) -> str:
        return '{0}-{1}'.format(self.__nombre,self.__apellido)
    
    def __len__(self) -> int:
        return self.__candidad
    
nuevo_personaje = Personaje_tres()
nuevo_personaje_2 = Personaje_tres()

print(nuevo_personaje)
print(nuevo_personaje_2)