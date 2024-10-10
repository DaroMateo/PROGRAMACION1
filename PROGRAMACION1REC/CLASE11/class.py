saludo = "hola mundo"
palabra = "   Pepe    "

# print(type(saludo))
# print(type(palabra))

# len(palabra) #funcion
# print(palabra) # funcion

# palabra.strip() # .strip borra los espacios en blanco, metodo de la clase string
# print(palabra)

# Palabra reservada class y nombre de la clase con UpperCamelCase

class TarjetaDeCredito: # class Personas:
    pass
    # Atributo

    # Metodo: Setters y Getters (set() , get()) -> con snake_case

class Persona:
    def __init__(self, nombre:str, edad: int, dni: int, genero_param:str) -> None:
        # Atributo = valor recibido por parametro
        self.nombre = nombre # atributo publico
        self.edad = edad # atributo publico
        self.__dni = dni # atributo privado
        self.genero = genero_param # atributo publico
        self.estado_civil = "soltero"
        
    # Metodo: Setters y Getters (set() , get()) -> con snake_case
    def get_nombre(self):
        return self._nombre
    def get_dni(self):
        return self.__dni
    def set_nombre(self, dato):
        #Validacion
        self.nombre = dato

    def set_dni(self, dato):
        #Validacion
        self.__dni = dato
    
    def presentarse(self):
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} años, mi dni es {self.__dni} y mi genero es {self.genero}") 

#ATRIBUTOS

persona_a= Persona("pepe", 23, 12345678, "masculino") # instancia de clase Persona
persona_b= Persona("juan",45, 20589670, "masculino") # otra instancia de la clase Persona

#print(id(persona_a))
#print(id(persona_b))

#persona_a.nombre = "pedro"

#print(persona_a.nombre)
#print(persona_b.nombre)
#print(id(persona_a))
#print(id(persona_b))

#METODOS

#print(persona_a.get_dni())
#print(persona_b.get_nombre())

#print(persona_b.set_nombre("juan")) 

#persona_a.presentarse()
# persona_b.presentarse()

#Persona.presentarse() #rompe xq es la clase y no el objeto

# len() #Funcion
# mi_lista = [5,2,4,1,3]
# mi_lista.sort() #Metodo 