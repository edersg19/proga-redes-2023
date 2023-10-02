# Nombre: Eder Gael Saldaña Galván
# Fecha: 2/Octubre/2023
# Descripción: Ejercicio práctico 2 - Servidores

asignaturas = ["Probabilidad y Estadística", "Electrónica para IDC", "Conexión de redes WAN", "Administración de servidores I", "Programación de Redes", "Inglés IV"]
notas = {}
for asignatura in asignaturas:
    nota = float(input(f"Ingresa la nota de la unidad I de {asignatura}: "))
    notas[asignatura] = nota
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")
