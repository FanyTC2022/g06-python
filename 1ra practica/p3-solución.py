"""

3. Teniendo presente el uso y concepto de diccionarios en Python, realizar un
programa con los siguientes requerimientos
Reglas:
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario.

"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
dni = input("Ingrese su DNI: ")

diccionarioPersona = {'nombre': nombre, 'apellido': apellido, 'edad': edad, 'dni': dni}

# Mostrar en pantalla sólo los values del diccionario

valuesDic = diccionarioPersona.values()
print("Los valores de mi diccionario actual son: {}".format(valuesDic))

# Agregando un nuevo key a mi diccionario

diccionarioPersona['profesion'] = input("Ingrese su profesión: ")

# Eliminando el key dni

del diccionarioPersona['dni']

# Mostrando mi diccionario actualizado

print("Mi diccionario actualizado es: {}".format(diccionarioPersona))
