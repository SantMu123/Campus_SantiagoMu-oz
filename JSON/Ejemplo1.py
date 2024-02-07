import json


with open("C://Users//user//Desktop//datos.json") as f:
    datos = json.load(f)

valor_especifico = datos['clave']['subclave']

print("El valor específico es:", valor_especifico)
