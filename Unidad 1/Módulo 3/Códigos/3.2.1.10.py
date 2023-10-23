# Nombre: Eder Gael Saldaña Galván
# Fecha: 2/Octubre/2023
# Laboratorio: La sentencia continue - El Feo Devorador de Vocales

palSinVocal = ""

userWord = input("Ingresa tu palabra: ")
userWord = userWord.upper()

for letra in userWord:
    if letra == "A":
        continue
    elif letra== "E":
        continue
    elif letra== "I":
        continue
    elif letra== "O":
        continue
    elif letra== "U":
        continue
    else:
        print(letra)
