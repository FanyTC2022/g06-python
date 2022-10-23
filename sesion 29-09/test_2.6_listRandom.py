"""Importando librería Random"""

"""random: manejor de número aleatorios"""

import random
listaNumeros = []

for indice in range(1, 20):  # nunca considera al ultimo valor como el 20
    # te mprime en orden desde el 1 a19
    #listaNumeros.append(indice)
    listaNumeros.append(random.randint(1, 20)) # te imprime de diferentes orden y ramdom

print(listaNumeros)
