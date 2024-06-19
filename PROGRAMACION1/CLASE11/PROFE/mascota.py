class Mascota:
    def __init__(self, raza, peso, nombre, color):
        self.__nombre = nombre
        self.__peso = peso
        self.__raza = raza
        self.__color = color
        
    @property
    def raza(self):
        return self.__raza
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def color(self):
        return self.__color
    
    def mover(self):
        print(f'La mascota {self.nombre} se mueve')
        
    def comer(self):
        print(f'La mascota {self.nombre} come')