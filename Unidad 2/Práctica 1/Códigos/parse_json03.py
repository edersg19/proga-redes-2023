# Nombre: Eder Gael Saldaña Galván
# Fecha: 23/Octubre/2023
# Descripción: Invocando API

import urllib.parse
import requests

while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "1AvgD6pPkSTGJb7jYkYtvLAQxajn0rtu"

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 

    json_data = requests.get(url).json()

    print("URL: " + (url))

    json_data = requests.get(url).json()

    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")

    # Codificar para manejar el error distinto a 0
    if json_status != 0:
        print("API Status: " + str(json_status) + " = An error route call.\n")
                               