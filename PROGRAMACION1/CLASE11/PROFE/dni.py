class Dni:
    def __init__(self, numero):
        self.__numero = numero
        
    @property
    def numero(self):
        return self.__numero
    
    def __str__(self) -> str:
        return str(self.__numero)