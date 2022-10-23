"""Control de excepciones"""
"""
TypeError.
ZeroDivisionError
OverflowError
IndexError: no encuentra un indice q nosotros queremos acceder
KeyError: cuando no encuentra un key en el diccionario
FileNotFoundError: en caso no encuentre un archivo
ImportError: 
"""

"""Estructura y uso"""

"""
    try:
        #bloque de código 1
    except exepción:
        #bloque de código 2
    else:
        #bloque de código 3
"""


def division(a, b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("¡No se puede dividir por cero!")
    else:
        print(resultado)


division(20, 0)

division(100, 40)
