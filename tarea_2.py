# Crear líneas de código en Python que calcule el promedio de los valores contenidos en una lista.

mis_valores = [5, 6, 10, 13, 3, 4,5,10,45782]

respuesta = 0

for valor in mis_valores:
    respuesta = valor + respuesta

respuesta = respuesta/len(mis_valores)

print(respuesta)

# Considere si se tiene una lista que contiene las alturas de grupos de personas

todos = [

[177,145,167,190,140,150,180,130], # grupo 1

[165,176,145,189,170,189,159,190], # grupo 2

[145,136,178,200,123,145,145,134], # grupo 3

[201,110,187,175,156,165,156,135] # grupo 4

]
# Escriba un código en python que determine cual grupo de
# personas contiene la mayor de todas las alturas de todas las personas
mayor = 0

for fila in todos:
    for columna in fila:
        mayor = mayor if mayor > columna else columna


print(mayor)
















