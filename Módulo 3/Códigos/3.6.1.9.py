# Nombre: Eder Gael Saldaña Galván
# Fecha: 2/Octubre/2023
# Laboratorio: Operando con listas - conceptos básicos

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

newList = my_list

for i in my_list:
    if i in newList:
        del my_list[1]

print("La lista con elementos únicos:")
print(my_list)