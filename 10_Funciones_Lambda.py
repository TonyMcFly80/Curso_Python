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

mult = lambda x: (x - 1) * x * (x + 1)

print(mult(5))

##############################################################

# Ejercicio 02
# Crea una función lambda que dados dos números devuelva si el primero es mayor.

comparativa = lambda x, y: (x > y)

print('Introduce 2 números y te diremos si el primero es mayor que el segundo')
num1 = int(input('Primer número: '))
num2 = int(input('Segundo número: '))
print(f'Es {num1} mayor que {num2}?')
print(comparativa(num1, num2))

##############################################################

# Ejercicio 03
# Dada una lista de palabras, quédate con filter() con las que tengan más vocales que consonantes.
# Necesitarás una función que devuelva si una palabra tiene más vocales que consonantes.

def vocal_vs_conso(palabra):
    """
    Devuelve la palabra introducida si esta tiene más vocales que consonantes.
    :param palabra: La palabra introducida.
    :return: Si la palabra tiene más vocales la devuelve, al contrario no devuelve nada.
    """
    count = 0
    for letra in palabra:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            count += 1
        else:
            continue

    final = len(palabra) - count

    if final < (len(palabra) / 2):

        return palabra


lista_palabras = ['america', 'amapola', 'ambrosia', 'algas', 'aleluya', 'enchufe', 'lila']
print(list(filter(vocal_vs_conso, lista_palabras)))

##############################################################

# Ejercicio 04
# Dada una lista de números enteros, quédate con filter() con los que tengan más de 5 divisores. Necesitarás
# una función que devuelva el número de divisores de un número dado.

def divisores(num):
    """
    Busca todos los divisores de un número entero introducido, y si tiene 5 o más la devuelve.
    :param num: Número entero solicitado.
    :return: Devuelve el número si este tiene 5 o más divisores.
    """
    count = 0

    for i in range(1, num + 1):

        if num % i == 0:
            count += 1

        else:
            continue

    if count >= 5:

        return num


lista_numeros = [0, 88, 2345, 343, 22, 98, 50, 1000, 912, 19, 7]
print(list(filter(divisores, lista_numeros)))

##############################################################

# Ejercicio 05
# Dada una lista de palabras, quédate con reduce() con la palabra más larga. Necesitarás una función que
# compare dos palabras y devuelva la que tenga mayor longitud.

from functools import reduce


def more_long(palara1, palabra2):

    if len(palara1) > len(palabra2):
        return palara1
    else:
        return palabra2


lista_palabras = ['america', 'amapola', 'ambrosia', 'algas', 'aleluya', 'enchufe', 'lila', 'gryffindor']
print(reduce(more_long, lista_palabras))

##############################################################

# Ejercicio 06
# Dada una lista de palabras, calcula el número de vocales de cada una con map().

l_p = ['america', 'amapola', 'ambrosia', 'algas', 'aleluya', 'enchufe', 'lila', 'gryffindor']

print(list(map(lambda p: p.count('a') + p.count('e') + p.count('i') + p.count('o') + p.count('u'), l_p)))

##############################################################

# Ejercicio 07
# Dada una lista de palabras, quédate con reduce() y map() con la palabra con más consonantes.
# Necesitarás una función que cuente el número de consonantes de una palabra y otra que dados dos
# números, devuelva el mayor.

from functools import reduce


def count_conso(palabra):
    """
    Cuenta el número de consonantes de una palabra.
    :param palabra: La palabra introducida.
    :return: El número de consonantes de la palabra.
    """
    count = 0
    for letra in palabra:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            continue
        else:
            count += 1

    return count


def num_max(num1, num2):
    """
    Calcula cual es el mayor número entre dos números.
    :param num1: Primer número.
    :param num2: Segundo número.
    :return: El número más alto.
    """
    if num1 > num2:
        return num1

    else:
        return num2


lista_palabras = ['america', 'amapola', 'ambrosia', 'algas', 'aleluya', 'enchufe', 'lila', 'gryffindor']

print(lista_palabras)
conso = list(map(count_conso, lista_palabras))
print(conso)
print(reduce(num_max, conso))

##############################################################
