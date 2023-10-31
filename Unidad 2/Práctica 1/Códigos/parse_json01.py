# Nombre: Eder Gael Saldaña Galván
# Fecha: 23/Octubre/2023
# Descripción: Invocando API

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Hidalgo"
dest = "Puerto Vallarta"
key = "1AvgD6pPkSTGJb7jYkYtvLAQxajn0rtu"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 

json_data = requests.get(url).json()

print(json_data['route']['sessionId'])

# Extrae la distancia y el tiempo
print("Distancia: " + str(json_data['route']['distance']))
print("Tiempo: " + str(json_data['route']['time']))

# Extrae el primer elemento llamado "formattedTime"
print("Tiempo total: " + str(json_data['route']['formattedTime']))