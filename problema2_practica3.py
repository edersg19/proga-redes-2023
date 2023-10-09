# Nombre: Eder Gael Saldaña Galván
# Fecha: 9/Octubre/2023
# Ejercicio: Ejercicio práctico 4

lstnombres = []

for i in range (5):
    nombre = input("Introduce el nombre de tu mejor amigo: ")
    lstnombres.append(nombre)
    
lstedades = []

for i in range (5):
    edad = int(input("Introduce las edad de {}: ".format(lstnombres[i])))
    lstedades.append(edad)
    
print(lstnombres,lstedades)

dicDatos = dict(zip(lstnombres, lstedades))

def mostrarDic(dic):
    for clave, valor in dic.items():
        print(f"{clave} -> {valor}")

mostrarDic(dicDatos)

print("Longitud de nombres: ",len(lstnombres))
print("Longitud de edades: ",len(lstedades))
print("Longitud del diccionario: ",len(dicDatos))

cveOrden = sorted(dicDatos.keys())
print("Claves ordenadas: ",cveOrden)

def buscarVal(clave,diccionario):
    return diccionario.get(clave)

claveBuscar = input("Introduce un valor para buscar: ")
valorEncontrado = buscarVal(claveBuscar, dicDatos)

if valorEncontrado is not None:
    print("Valor encontrado: ",valorEncontrado)
else:
    print("La clave no se encuentra en el diccionario")