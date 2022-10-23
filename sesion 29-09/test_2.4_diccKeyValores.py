"""Diccionarios en Python"""

varDiccionario = {"nombre": "Mysql", "tipo": "BD relacional"}

"""Convirtiendo diccionario a lista"""

list(varDiccionario)

print("\nMi diccionario convertido es el siguiente: {}\n".format(list(varDiccionario)))

"""valores de mi diccionario"""

valores = list(varDiccionario.values())
print(valores)

"""valores de mi keys"""

keys = list(varDiccionario.keys())
print("\n", keys)

"""para mostrar mis keys y valores de diccionario en tuplas"""

lista_convertida = varDiccionario.items()
print("\n", lista_convertida)

