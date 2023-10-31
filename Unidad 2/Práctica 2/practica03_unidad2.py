# Descripción de la API: Generador de imágenes de zorros
# Autor: Eder Gael Saldaña Galván
# Fecha de creación: 30/Octubre/2023

import urllib.parse
import requests

while True:
    image = input("Fox here: ")
    if image == "quit" or image == "q":
        print("Que un zorro te acompañe siempre")
        break
    
    main_api = "https://randomfox.ca/floof/?ref=apilist.fun"

    url = main_api + urllib.parse.urlencode({}) 

    json_data = requests.get(url).json()

    print("URL: " + (url))

    json_data = requests.get(url).json()

    print(json_data['image'])