# Nombre: Eder Gael Saldaña Galván
# Fecha: 25/Septiembre/2023
# Laboratorio: Operadores y expresiones

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

total_min = mins + dura

min_a_hour= int(total_min / 60)

total_hour = ((min_a_hour + hour) % 24)

ex_mins = ((mins + dura) % 60)

print(total_hour, ex_mins, sep = ":")
