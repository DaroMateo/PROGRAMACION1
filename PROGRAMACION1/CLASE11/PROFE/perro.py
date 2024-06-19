from PROGRAMACION1.CLASE11.PROFE.mascota import Mascota
class Perro (Mascota):
    def __init__(self, raza, peso, nombre, color, ladrido):
        super().__init__(raza, peso, nombre, color)
        self.ladrido = ladrido