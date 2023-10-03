# Nombre: Eder Gael Saldaña Galván
# Fecha: 2/Octubre/2023
# Descripción: Ejercicio práctico 2 - Servidores

asignaturas = []
notas = {}
for asignatura in asignaturas:
    nota = float(input(f"Ingresa la nota de la {asignatura}: "))
    notas[asignatura] = nota
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")
