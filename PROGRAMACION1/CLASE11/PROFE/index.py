from PROGRAMACION1.CLASE11.PROFE.gato import Gato
from PROGRAMACION1.CLASE11.PROFE.perro import Perro

gato_uno = Gato('siames', 5, 'mia', 'negro', 'miau', 100)
gato_dos = Gato('angora', 10, 'pipo', 'naranja', 'miau', 123)

perro_uno = Perro('dalmata', 10, 'manchas', 'blanco y negro', 'guah')
perro_dos = Perro('cocker', 15, 'janson', 'naranja', 'guah')

gatos = [gato_dos, gato_uno]

gato_uno.mover()
gato_dos.mover()

perro_uno.mover()
perro_dos.mover()

print(gato_uno.dni)