import json

file =  open("object.json") 
users = json.load(file)

for user in users:
    print("Nombre del usuario:", user["name"], ", edad:", user["age"])
file.close()
dicctionary = [
    { 
        "table": 12,
        "chair": 14,
        "id": 567
        },{
        "table": 44,
        "chair": 10,
        "id": 56
    }
]

#Pasamos el diccionario a objeto tipo json
things = json.dumps(dicctionary)

#usamos open para abrir el archivo o para generarlo si no existe y abrirlo
file =  open("things.json", "w") 

#Escribimos sobre todo el archivo
file.write(things)

#Cerramos el archivo
file.close()
import json

dicctionary = [
    { 
        "table": 12,
        "chair": 14,
        "id": 567
        },{
        "table": 44,
        "chair": 10,
        "id": 56,
        "valor": True,
        5: "Hola"
    }
]
with open("personas.json", "w") as file:
    things = json.dumps(dicctionary)
    file.write(things)