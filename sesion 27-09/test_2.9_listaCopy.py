"""Estructura de datos"""

"""Listas copy(): Devuelve la ciopia de una lista"""

var1 = ["SQLserver", "RDS", "Mysql", "postgresql"]

var2 = var1.copy()
var2.append("sqlite3")

print("\nMi primera lista es: {}". format(var1))

print("La copia de mi lista 1 es: {}". format(var2))