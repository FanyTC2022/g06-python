"""Usando las propiedades de cadena"""

"""Usando rango y el tercer valor opcional step"""

cadena = "Bienvenido al modulo I de Python"

cadena1 = cadena[0:10] # no toma el ultimo valor, solo hasta el indice 9

"""Usando el tercer valor: step para ir sumando el primer indice"""

cadena2 = cadena[0:24:2]

print("\nLa primera rebanada de nuestra cadena es: {}".format(cadena1))
print("La segunda rebanada de nuestra cadena es: {}".format(cadena2))
