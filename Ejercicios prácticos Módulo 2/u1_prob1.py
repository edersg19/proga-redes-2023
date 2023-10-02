# Autor: Eder Gael Saldaña Galván
# Fecha: 2/Octubre/2023
# Descripción: Ejercicio práctico 2 - Cuenta de ahorro

deposito = float(input("Introduce tu depósito en la cuenta de ahorros: "))

interes = deposito * 0.04
ahorro1 = deposito + interes
ahorro2 = deposito + (interes*2)
ahorro3 = deposito + (interes*3)

print("El ahorro en un año es de:",ahorro1)
print("El ahorro en dos años es de:",ahorro2)
print("El ahorro en tres años es de:",ahorro3)
