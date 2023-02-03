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

