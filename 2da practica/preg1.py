"""
Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad y de nacionalidad peruana (use el manejo de errores para el tipo de
dato)

"""
from datetime import datetime, date

class Persona:

    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

#Un método cumpleaños donde cada vez que invoque aumentará en un año la
#edad de la persona

    def cumpleaños(self):
        self.edad = self.edad + 1

#Crear la instancia de la clase Persona y usar su método cumpleaños para
#incrementar su edad (mínimo 2 vez, mostrar por pantalla dicha edad
#actualizada)

nombre = input("\nIngrese su nombre: ")
edad = int(input("Digite su edad: "))

persona1 = Persona(nombre, edad, "peruana")

print("\nLa edad de {} es: {}".format(persona1.nombre, persona1.edad))

persona1.cumpleaños()
persona1.cumpleaños()

print("La edad actual de {} es: {}".format(persona1.nombre, persona1.edad))


# Crear una función que retorne solamente la fecha, hora y minuto que se ha
# registrado esta persona

def tiempo():
    fecha = date.today()
    hora = datetime.now().hour
    minuto = datetime.now().minute

print("\nRegistrado el {} a las {} horas y {} minutos".format(f)



