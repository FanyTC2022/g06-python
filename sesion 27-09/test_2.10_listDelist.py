"""Estructura de datos"""

"""Listas del(i): Elimina un item de la lista enviando una posición existente"""

lista = []

lista.append(2022)
lista.append("Septiembre")
lista.append("Modulo 1")
lista.append(40)

print(lista)

del lista[2]

print("\nMi lista actualizada es: {}". format(lista))

""" """
del lista[6] #fuera del rango
print("\nMi lista actualizada es: {}". format(lista))