# Descripción de la API: Validador de Emails
# Autor: Eder Gael Saldaña Galván
# Fecha de creación: 30/Octubre/2023

import urllib.parse
import requests

while True:
    email = input("Email: ")
    if email == "quit" or email == "q":
        print("Gracias por usar el validador de Emails")
        break
    
    main_api = "https://validemail.io/v1/validate?api_key=e6VVXsxthNgYH3tUKfjfSNTOUqskz6rp&"
    key = "e6VVXsxthNgYH3tUKfjfSNTOUqskz6rp"

    url = main_api + urllib.parse.urlencode({"email":email}) 

    json_data = requests.get(url).json()

    print("URL: " + (url))

    json_data = requests.get(url).json()

    print(json_data['is_valid'])