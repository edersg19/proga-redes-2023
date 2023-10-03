# Nombre: Eder Gael Saldaña Galván
# Fecha: 2/Octubre/2023
# Laboratorio: Fundamentos del bucle while

blocks = int(input("Ingresa el número de bloques: "))

height = 0
step = 1

while blocks > height:
    height += 1
    blocks -= height
    
print("La altura de la pirámide:", height)