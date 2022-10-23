nombre = input("\nIngrese su nombre: ")
edad = int(input("Ingrese su edad: ")) # edad de tipo entero

print("\nEl tipo de dato del 'nombre' es: {}".format(type(nombre)))
print("El tipo de dato de la 'edad' es: {}".format(type(edad)))

##--------------------------------

nombre1 = input("\nIngrese el nombre del 1er trabajador: ")
edad1 = int(input("Ingrese la edad del 1er trabajador: ")) # edad de tipo entero
nombre2 = input("\nIngrese el nombre del 2do trabajador: ")
edad2 = int(input("Ingrese la edad del 2do trabajador: ")) # edad de tipo entero

trabajador = []

trabajador.append(nombre1)
trabajador.append(edad1)
trabajador.append(nombre2)
trabajador.append(edad2)

print("\nMi lista es: {}".format(trabajador))

suma = trabajador[1] + trabajador[3]

print("La suma de edades de los 2 trabajadores es: {}". format(suma))