"""Usando las propiedades de cadena"""

"""metodos de String"""

cadena = "Conexión a base de datos con Python"

cadena2 = cadena.replace(cadena[0:6], "ccc")

print("\nCadena con reemplazo, tiene el siguiente valor: \n> "
      "{}".format(cadena2))

"""Eliminando los espacios en blanco de mi cadena (final)"""

cadena3 = "Conexión a base de datos con Python        "

cadena4 = cadena3.rstrip()

print("\nMi cadena de espacios en blanco eliminados es: \n> "
      "{}".format(cadena4))

"""Eliminando los espacios en blanco de mi cadena (inicio)"""

cadena5 = "              Conexión a base de datos con Python        "

cadena6 = cadena3.lstrip()

print("\nMi cadena de espacios en blanco eliminados es: \n> "
      "{}".format(cadena6))