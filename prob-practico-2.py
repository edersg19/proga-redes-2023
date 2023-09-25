# Nombre: Eder Gael Saldaña Galván
# Fecha: 25/Septiembre/2023
# Descripción: Problema 2

print("Introduce tu número: ")  # Guarda el número del usuario
n = int(input()) 
i = int(1)

while i <= n:                   # Crea una secuencia de números
    print(i)
    i= i+1 

suma = (n*(n+1))/2              # Realiza una suma de todos los números y la divide entre 2
print("Suma de los números: ",suma)     # Imprime los resultados en la pantalla
