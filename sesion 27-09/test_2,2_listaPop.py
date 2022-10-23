"""Estructura de datos"""

"""Listas pop(i): quitar un elemento indicando su índice"""

lista = ["Dia del descubrimiento de América", True, 1000, 20.8]

print("\nEl valor de mi lista: {}".format(lista[0]))
print("El valor de mi lista: {}".format(lista[1]))

lista.append(False)
lista.append(800)

print("\nMi lista actualizada tiene los siguientes datos:\n{}". format(lista))

lista.pop(1)
print("\nMi lista actualizada tiene los siguientes datos:\n{}". format(lista))

lista.pop(0)
print("\nMi lista actualizada tiene los siguientes datos:\n{}". format(lista))