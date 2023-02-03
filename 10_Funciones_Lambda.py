# EJERCICIOS y EXAMEN FINAL del Tema
# NOTA: No es necesario usar código para comprobar si los datos introducidos por el usuario son correctos.
# Vamos a interpretar que así es por ahora a menos que se especifique lo contrario.

##############################################################

# Tarea 01
# Vamos a crear una función Lambda que devuelva una tupla donde en la primera posición esté
# el número introducido por parámaetro; en la segunda, su doble; y, en la tercera, su cuadrado.

operation = lambda x: (x, x*2, x**2)

print(operation(5))

##############################################################

# Tarea 02
# Dada una lista numérica, vamos a filtrarla y quedarnos con los números positivos. El resultado lo
# mostraremos en una lista.

nums = [0, 22, -4, 8, 9, -34, -1, 3, -8, 1]

print(list(filter(lambda x: (x > 0), nums)))

##############################################################

# Tarea 03
# Dada una lista de palabras, vamos a quedarnos con la palabra con más "a".

from functools import reduce


def max_a(x, y):
    if x.count('a') > y.count('a'):
        return x
    return y


lista_palabras = ['salchichas', 'amapola', 'ambrosia', 'algas']

print(reduce(max_a, lista_palabras))

##############################################################

# Tarea 04
# Vamos a convertir una lista de grados Celsius a grados Fahrenheit. El resultado lo mostraremos
# como una lista.

celcius = [0, 16, 32, 40, -5]

print(list(map(lambda x: (x * 9 / 5) + 32, celcius)))

##############################################################

# Tarea 05
# Vamos a ordenar una lista de palabras por el número de apariciones de la letra indicada por
# el usuario. El orden será descendente.

lista_palabras = ['salchichas', 'amapola', 'ambrosia', 'algas', 'yoyo', 'silla', 'pan']

l = str(input('Introduce una letra: '))

print(sorted(lista_palabras, key=lambda x: x.count(l), reverse=True))

##############################################################

# EXAMEN DEL TEMA

##############################################################

# Ejercicio 01
# Crea una función lambda que dado un número entero multiplique por su anterior y su siguiente. Por ejemplo,
# si proporcionamos n = 3, nos tendrá que devolver 2 · 3 · 4 = 24.
