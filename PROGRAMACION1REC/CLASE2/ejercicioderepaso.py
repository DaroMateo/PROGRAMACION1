'''La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
contagio, de cada una debe obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
1000 unidades)
4. La marca y el Fabricante.
Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.
Ejemplo de mensaje de consola:'''

# Inicialización de listas para almacenar los datos de los productos
tipos = []
precios = []
cantidades = []
marcas = []
fabricantes = []

for i in range(5):
    tipo = input("Ingrese el tipo de producto (barbijo, jabón, alcohol): ")
    while tipo != "barbijo" and tipo != "jabón" and tipo != "alcohol":
        print("Tipo no válido. Intente nuevamente.")
        tipo = input("Ingrese el tipo de producto (barbijo, jabón, alcohol): ")

    precio = int(input("Ingrese el precio (entre 100 y 300): "))
    while precio < 100 or precio > 300:
        print("El precio debe estar entre 100 y 300.")
        precio = int(input("Ingrese el precio (entre 100 y 300): "))
    
    cantidad = int(input("Ingrese la cantidad de unidades (entre 1 y 1000): "))
    while cantidad <= 0 or cantidad > 1000:
        print("La cantidad debe estar entre 1 y 1000.")
        cantidad = int(input("Ingrese la cantidad de unidades (entre 1 y 1000): "))
    
    marca = input("Ingrese la marca del producto: ")
    fabricante = input("Ingrese el fabricante del producto: ")

    # Agregar los valores a las listas correspondientes
    tipos.append(tipo)
    precios.append(precio)
    cantidades.append(cantidad)
    marcas.append(marca)
    fabricantes.append(fabricante)

# Inicialización de variables para el análisis
max_precio_barbijo = 0
cantidad_barbijo = 0
fabricante_barbijo_caro = ""

max_cantidad = 0
fabricante_mas_unidades = ""

total_jabones = 0

# Análisis de los productos
for i in range(5):
    if tipos[i] == "barbijo" and precios[i] > max_precio_barbijo:
        max_precio_barbijo = precios[i]
        cantidad_barbijo = cantidades[i]
        fabricante_barbijo_caro = fabricantes[i]
    
    if cantidades[i] > max_cantidad:
        max_cantidad = cantidades[i]
        fabricante_mas_unidades = fabricantes[i]
    
    if tipos[i] == "jabón":
        total_jabones += cantidades[i]

# Resultados
if max_precio_barbijo > 0:
    print(f"El barbijo más caro tiene {cantidad_barbijo} unidades y fue fabricado por {fabricante_barbijo_caro}.")
else:
    print("No se ingresaron barbijos.")

print(f"El producto con más unidades es fabricado por {fabricante_mas_unidades}.")
print(f"Hay un total de {total_jabones} unidades de jabón.")