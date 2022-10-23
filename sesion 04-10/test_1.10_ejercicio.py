"""cadena de caracteres"""

"""
    - crear una cadena con nombres y apellidos de un usuario
    - mostrar los apellidos en mayúscula
"""
cadena = "fany Taquila Calderon"
print("\nMi cadena  de caracteres transformado a mayuscula es: \n> "
      "{}{}".format(cadena[0:5], cadena[5:].upper()))
"""
    - pedir uuna cadena y un caracter por teclado
    - mostrar cuantas veces aparece el caracter enn la cadena
"""

cadena = input("\nIngrese una cadena: ")
caracter = input("Ingrese el caracter de interes: ")

print("El caracter '{}' se repite {} veces ".format(caracter, cadena.count(caracter)))

"""ejericio"""

email = input("\nIngrese su correo electronico: ")

if email.index('@'):    # if '@' in email:
      print("\n el correo es correcto")
else:
      print("El correo es incorrecto")