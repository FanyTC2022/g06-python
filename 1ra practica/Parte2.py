lista = [7, 5, 2, 3, 8, 10, 13, 9, 20, 4]

lista1 = []
lista2 = []

# llenamos la lista1 con los cubos de los elementos de lista
i = 0
for i in range(len(lista)):
    lista1.append(pow(lista[i],3))

print("\nLista1: {}".format(lista1))

# llenamos la lista2 con los cuadrados de los elementos de lista

i = 0
for i in range(len(lista)):
    lista2.append(pow(lista[i],2))

print("\nLista1: {}".format(lista2))

suma = lista1 + lista2

print("\nSuma de lista1 y lista2: \n\n{}".format(suma))
suma.reverse()
print("\nSuma inversa: \n\n{}".format(suma))