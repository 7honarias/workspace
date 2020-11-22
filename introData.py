
dato1 = float(input("introduce un numero \n"))
dato2 = float(input("introduce un numero \n"))
result = dato1 + dato2
print(result)

lista = [1, 2, 3, 4, 8, 6, 5]

lista2 = lista.copy()
# pop elimina el ultimo valor de la lista
lista.pop()
# remove elimina un elemento dado
lista.remove(2)
lista.reverse()
print(lista)
lista.sort()
print(lista2)
print(lista)

rango = range(6)
# me regresa un rango de 0 - 6

diccionario = {
    "nombre": "kiara",
    "Raza": "Tres Colores",
    "Edad": 5
}
print(diccionario)
print(diccionario["nombre"])