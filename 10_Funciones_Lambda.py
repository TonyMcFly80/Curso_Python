# EJERCICIOS y EXAMEN FINAL del Tema
# NOTA: No es necesario usar código para comprobar si los datos introducidos por el usuario son correctos.
# Vamos a interpretar que así es por ahora a menos que se especifique lo contrario.


# Tarea 01
# Vamos a crear una función Lambda que devuelva una tupla donde en la primera posición esté
# el número introducido por parámaetro; en la segunda, su doble; y, en la tercera, su cuadrado.

operation = lambda x: (x, x*2, x**2)

print(operation(5))

