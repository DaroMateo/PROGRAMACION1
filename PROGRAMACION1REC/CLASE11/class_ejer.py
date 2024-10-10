class Vehiculo:
    motor = True
    def __init__(self, tipo:str, marca:str, modelo_ing:str, color:str, patente:str, cantidad_ruedas:int, cantidad_puertas:int, vuela:bool):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo_ing
        self.color = color
        self.patente = patente
        self.cantidad_ruedas = cantidad_ruedas
        self.cantidad_puertas = cantidad_puertas
        self.vuela = vuela

    def set_motor(self,cambio):
        self.motor = cambio
mi_auto = Vehiculo("Auto", "Ford", "F4000", "Blanco", "ABC123", 4, 2, False)

# print(mi_auto.patente)
# print(mi_auto.motor)
# mi_auto.set_motor(False)
# print(mi_auto.motor)


    