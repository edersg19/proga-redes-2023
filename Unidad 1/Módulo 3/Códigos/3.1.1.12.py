# Nombre: Eder Gael Saldaña Galván
# Fecha: 2/Octubre/2023
# Laboratorio: Fundamentos de la sentencia if-elif-else

year = int(input("Introduce un año: "))

if year < 1582:
    print("No está dentro del período del calendario Gregoriano")
if year % 4 != 0:
    print("Año común")
elif year % 100 != 0:
    print("Año bisiesto")
elif year % 400 != 0:
    print("Año común")
else:
    print("Año bisiesto")
