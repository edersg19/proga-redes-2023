# Descripción de la API: Generador de imágenes de gatos
# Autor: Eder Gael Saldaña Galván
# Fecha de creación: 30/Octubre/2023

import urllib.parse
import requests

while True:
    limit = input("Cat here: ")
    if limit == "quit" or limit == "q":
        print("Gracias por amar a los gatitos")
        break
    
    main_api = "https://api.thecatapi.com/v1/images/0XYvRd7oD"
    key = "live_w2IyX9SXq6rVxs6lRkbhDgLTDsYmvLchi6AnjRNLIilR1X5WZZhFQagvwvWnunBi"

    url = main_api + urllib.parse.urlencode([]) 

    json_data = requests.get(url).json()

    print("URL: " + (url))

    json_data = requests.get(url).json()

    print(json_data['url'])