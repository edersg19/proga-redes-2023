# Nombre: Eder Gael Saldaña Galván
# Fecha: 23/Octubre/2023
# Descripción: Invocando API

import urllib.parse
import requests

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        print("Hasta luego querido viajero")
        break
    dest = input("Destination: ")
    # Agregar condición a dest
    if dest == "quit" or dest == "q":
        # Agregar mensaje de despedida
        print("Hasta luego querido viajero")
        break
    
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "1AvgD6pPkSTGJb7jYkYtvLAQxajn0rtu"

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 

    json_data = requests.get(url).json()

    print("URL: " + (url))

    json_data = requests.get(url).json()

    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Miles:           " + str(json_data["route"]["distance"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================")
        
        # Imprimir RouteType, latutude y longitud
        print(json_data['route']['options']['routeType'])
        print(json_data['route']['boundingBox']['ul']['lat'])
        print(json_data['route']['boundingBox']['ul']['lng'])
        
    # Codificar para manejar el error distinto a 0
    elif json_status == 402:
        print("API Status: " + str(json_status) + " = An error route call.\n")
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
