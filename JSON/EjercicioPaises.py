import json

paises = [
    { 
        "pais": "Colombia",
        "continente": "Sur America",
        "Poblacion": 55
    },{
        "pais": "Japon",
        "continente": "Asia",
        "Poblacion": 45
    },{
        "pais": "Australia",
        "continente": "Oceania",
        "Poblacion": 30
    }
]

cosas = json.dumps(paises)
file =  open("Paises.json", "w") 

#Escribimos sobre todo el archivo
file.write(cosas)

#Cerramos el archivo
file.close()

