import json
def leer_json(nombre_archivo, key):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        data = json.load(archivo)

    return(data[key])

#------------------------------------------------------------------------------

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("File not found. Creating a new one.")
        with open(filename, 'w') as file:
            json.dump([], file)
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return []

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print("Data saved successfully.")

def generate_id(data):
    return max([item['Id'] for item in data], default=0) + 1

def get_input(prompt, validation_func, error_message):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print(error_message)

def alta(data):
    # Generar ID único
    id = generate_id(data)
    
    # Validar Aerolínea
    def validate_airline(airline):
        return airline in ["AA", "LATAM", "IBERIA"]
    airline = get_input("Enter airline (AA, LATAM, IBERIA): ", validate_airline, "Invalid input. Please enter one of the following: AA, LATAM, IBERIA.")

    # Validar Nombre
    def validate_name(name):
        return len(name) <= 30 and name.replace(' ', '').isalpha()
    name = get_input("Enter passenger's name (up to 30 characters): ", validate_name, "Invalid input. Name must be up to 30 characters and contain only letters.")
    
    # Validar DNI
    def validate_dni(dni):
        return dni.isdigit()
    dni = get_input("Enter passenger's DNI: ", validate_dni, "Invalid DNI. Please enter a numeric value.")
    
    # Validar Precio
    def validate_price(price):
        return price.isdigit() and 500000 <= int(price) <= 2000000
    price = int(get_input("Enter price (500000 - 2000000): ", validate_price, "Invalid price. Please enter a value between 500000 and 2000000."))
    
    # Validar Origen y Destino
    def validate_city(city):
        return city in ["Buenos Aires", "Madrid", "París", "Miami", "Roma", "Tokio"]
    origin = get_input("Enter origin (Buenos Aires, Madrid, París, Miami, Roma, Tokio): ", validate_city, "Invalid city. Please enter one of the following: Buenos Aires, Madrid, París, Miami, Roma, Tokio.")
    destination = get_input("Enter destination (Buenos Aires, Madrid, París, Miami, Roma, Tokio): ", validate_city, "Invalid city. Please enter one of the following: Buenos Aires, Madrid, París, Miami, Roma, Tokio.")
    while origin == destination:
        print("Destination must be different from origin.")
        destination = get_input("Enter destination (Buenos Aires, Madrid, París, Miami, Roma, Tokio): ", validate_city, "Invalid city. Please enter one of the following: Buenos Aires, Madrid, París, Miami, Roma, Tokio.")
    
    # Validar Clase
    def validate_class(class_type):
        return class_type in ["Turista", "Ejecutivo"]
    class_type = get_input("Enter class (Turista, Ejecutivo): ", validate_class, "Invalid class. Please enter either 'Turista' or 'Ejecutivo'.")
    
    # Validar Fecha
    def validate_date(date):
        return len(date) == 8 and date.isdigit()
    date = get_input("Enter date (AAAAMMDD): ", validate_date, "Invalid date. Please enter a date in the format AAAAMMDD.")

    # Crear el nuevo registro
    record = {
        "Id": id,
        "Aerolínea": airline,
        "Apellido_Nombre_Pasajero": name,
        "DNI_Pasajero": dni,
        "Precio": price,
        "Origen": origin,
        "Destino": destination,
        "Clase": class_type,
        "Fecha": date
    }
    
    # Agregar el registro a los datos
    data.append(record)
    print("Record added successfully.")
    return data
def modify_record(data):
    for clave in data:
        print(f"Id: {clave['Id']}, Name: {clave['Apellido_Nombre_Pasajero']}")
    id = int(input("Enter id of the clave to modify: "))
    clave = next((item for item in data if item["Id"] == id), None)
    if clave:
        print("1. Modify DNI")
        print("2. Modify Name")
        print("3. Modify Date")
        choice = int(input("Choose an option: "))
        match choice:
            case 1:
                clave['DNI_Pasajero'] = input("Enter new DNI: ")
            case 2:
                clave['Apellido_Nombre_Pasajero'] = input("Enter new name: ")
            case 3:
                clave['Fecha'] = input("Enter new date (AAAAMMDD): ")
            case _:
                print("Invalid choice.")
    else:
        print("clave not found.")
    return data

def delete_record(data):
    for clave in data:
        print(f"Id: {clave['Id']}, Name: {clave['Apellido_Nombre_Pasajero']}")
    id = int(input("Enter id of the record to delete: "))
    data = [record for record in data if record["Id"] != id]
    print("Record deleted successfully.")
    return data

def list_records(data):
    if not data:
        print("No records to display.")
        return
    
    header = "Fecha | Aerolínea | Clase | Origen | Destino | Precio | DNI | Apellido y nombre"
    print(header)
    print("-" * len(header))
    
    for record in data:
        formatted_record = (
            f"{record['Fecha']} | "
            f"{record['Aerolínea']} | "
            f"{record['Clase']} | "
            f"{record['Origen']} | "
            f"{record['Destino']} | "
            f"{record['Precio']} | "
            f"{record['DNI_Pasajero']} | "
            f"{record['Apellido_Nombre_Pasajero']}"
        )
        print(formatted_record)


def main():
    filename = 'data.json'
    data = load_data(filename)
    
    while True:
        print("\nMenu:")
        print("A – Load data")
        print("B – Add data")
        print("C – Modify data")
        print("D – Delete data")
        print("E – List data")
        print("F – Exit")
        choice = input("Choose an option: ").upper()

        match choice:
            case 'A':
                data = load_data(filename)
            case 'B':
                data = alta(data)
                save_data(data, filename)
            case 'C':
                if data:
                    data = modify_record(data)
                    save_data(data, filename)
                else:
                    print("Load data first.")
            case 'D':
                if data:
                    data = delete_record(data)
                    save_data(data, filename)
                else:
                    print("Load data first.")
            case 'E':
                if data:
                    list_records(data)
                else:
                    print("Load data first.")
            case 'F':
                break
            case _:
                print("Invalid choice.")

print(main())