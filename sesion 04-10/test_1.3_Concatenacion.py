"""Usando las propiedades de cadena"""

"""Concatenación"""

nombre = "Luke"
apellido = "skywalker"


nombreCompleto = "El nombre completo del primer unuario es: " + nombre + " " + apellido

print("\n" + nombreCompleto)

"""Usando format"""

nombreCompleto2 = "El nombre completo del usuario es: {} {}".format(nombre, apellido)
print(nombreCompleto2)