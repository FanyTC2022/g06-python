
import json

class Empleado():

    def __init__(self, nombre):
        self.nombre = nombre

empleado = Empleado("Juan")

empleado1 = {"nombre": empleado.nombre}  # creamos un diccionario

print("nombre: {}".format(empleado1))

empleadoToJson = json.dumps(empleado1)  # conviertiendo a Json doble comilla

print("El dato de nuestra nueva variables es: {}".format(empleadoToJson))
