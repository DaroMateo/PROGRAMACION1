import json

data = {}
data['clientes'] = []
data['clientes'].append({ 'nombre': 'Juan', 'edad': 27})
data['clientes'].append({ 'nombre': 'Ana', 'edad': 26})

with open('data.json', 'w') as file:json.dump(data, file, indent=4, ensure_ascii=False )

#metodo load
with open('data.json', 'r') as file: data = json.load(file)
print(data)