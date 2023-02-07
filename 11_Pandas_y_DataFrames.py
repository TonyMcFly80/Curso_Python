# EJERCICIOS y EXAMEN FINAL del Tema
# NOTA: No es necesario usar código para comprobar si los datos introducidos por el usuario son correctos.
# Vamos a interpretar que así es por ahora a menos que se especifique lo contrario.

##############################################################

# Tarea 01
# Vamos a crear un dataframe de 10 filas y 5 columnas.
# - La primera columna será word y contendrá 10 apalabras.
# - La segunda columna será length y contendrá la longitud de cada palabra.
# - La tercera columna será start y contendrá la primera letra de cada palabra.
# - La cuarta columna será end y contendrá la última letra de cada palabra.
# - La quinta columna será isPalindrome y contendrá valores booleanos indicando si cada palabra es
# palindromo o no.
# A continuación, vamos a transformar la columna word en los nombres de las filas utilizando el método
# .set_index().
# Finalmente. calcularemos las dimensones de nuestro dataframe.

import pandas as pd

words = ['leña', 'fuego', 'campo', 'hierba', 'ala', 'insectos', 'aire', 'animales', 'mesa', 'cuchara']

data = {'word': words,
        'length': map(len, words),
        'start': map(lambda palabra: palabra[0], words),
        'end': map(lambda palabra: palabra[-1], words),
        'isPalindrome': map(lambda palabra: palabra == palabra[::-1], words)
        }

df = pd.DataFrame(data=data)

df_mod = df.set_index('word')

df_mod.index.names = [None]

print(df_mod)
print(df_mod.shape)

##############################################################

# Tarea 02
# Del dataframe df_mod creado en el ejercicio anterior, vamos a mostrar cada columna por separado
# con un bucle for.
# Finalmente, vamos a quedarnos con las 3 últimas columnas, y ese nuevo subdataframe lo guardaremos
# en una variable words2, para no modificar el dataframe original.

import pandas as pd

words = ['leña', 'fuego', 'campo', 'hierba', 'ala', 'insectos', 'aire', 'animales', 'mesa', 'cuchara']

data = {'word': words,
        'length': map(len, words),
        'start': map(lambda palabra: palabra[0], words),
        'end': map(lambda palabra: palabra[-1], words),
        'isPalindrome': map(lambda palabra: palabra == palabra[::-1], words)
        }

df = pd.DataFrame(data=data)

df_mod = df.set_index('word')

df_mod.index.names = [None]

count = 0

# For para mostrar cada columna por separado:

for j in df_mod:
    print(f'\n=== {j.upper()} ===')
    print(df_mod[df_mod.columns[count]])
    count += 1

# Nueva variable que muestra las 3 íltimas columnas:

words2 = df_mod[df_mod.columns[1:]]
print('\n=== NUEVA LISTA ===')
print(words2)

##############################################################

# Tarea 03
# Del dataframe df_mod, vamos a mostrar las 5 primeras filas, las 5 últimas filas y después, vamos
# a guardar una copia en la variable df_mod_copy. Finalmente, vamos a modificar los nombres de las
# columnas de df_mod_copy a 'Longitud', 'Principio', 'Fin' y 'Palíndromo'.

import pandas as pd

words = ['leña', 'fuego', 'campo', 'hierba', 'ala', 'insectos', 'aire', 'animales', 'mesa', 'cuchara']

data = {'word': words,
        'length': map(len, words),
        'start': map(lambda palabra: palabra[0], words),
        'end': map(lambda palabra: palabra[-1], words),
        'isPalindrome': map(lambda palabra: palabra == palabra[::-1], words)
        }

df = pd.DataFrame(data=data)

df_mod = df.set_index('word')

df_mod.index.names = [None]

# Mostramos la 5 primeras filas
print('/// LAS 5 PRIMERAS FILAS DEL DATAFRAME ///\n')
print(df_mod.head(5))

# Mostramos las 5 últimas filas
print('\n/// LAS 5 ÚLTIMAS FILAS DEL DATAFRAME ///\n')
print(df_mod.tail(5))

# Hacemos una copia
df_mod_copy = df_mod.copy()

# Modificamos los nombres de las columnas
df_mod_copy.rename(columns={'length': 'Longitud',
                            'start': 'Principio',
                            'end': 'Fin',
                            'isPalindrome': 'Palíndromo'}, inplace=True)

print('\n/// COPIA DE DATAFRAME CON COLUMNAS MODIFICADAS ///\n')
print(df_mod_copy)

##############################################################

# Tarea 04
# Vamos a mostrar las filas del dataframe df_mod con el siguiente formato:
# "La palabra {identificadorFila} {si/no} es un palíndromo de {longitud} letras".

import pandas as pd

words = ['leña', 'fuego', 'ama', 'hierba', 'ala', 'insectos', 'aire', 'animales', 'tenet', 'cuchara']

data = {'word': words,
        'length': map(len, words),
        'start': map(lambda palabra: palabra[0], words),
        'end': map(lambda palabra: palabra[-1], words),
        'isPalindrome': map(lambda palabra: palabra == palabra[::-1], words)
        }

df = pd.DataFrame(data=data)

df_mod = df.set_index('word')

df_mod.index.names = [None]

for i in df_mod.itertuples():
    if i[4] is True:
        print(f'La palabra \"{i[0]}\", es un palíndromo de \"{i[1]}\" letras.')
    else:
        print(f'La palabra \"{i[0]}\", no es un palíndromo de \"{i[1]}\" letras.')

##############################################################

# Tarea 05
# Del dataframe df_mod vamos a transformar la columna start a dataframe para iterar sobre sus
# filas. A continuación vamos a transformar la columna length en lista para eliminar una de sus entradas
# con el método .remove().

import pandas as pd

words = ['leña', 'fuego', 'ama', 'hierba', 'ala', 'insectos', 'aire', 'animales', 'tenet', 'cuchara']

data = {'word': words,
        'length': map(len, words),
        'start': map(lambda palabra: palabra[0], words),
        'end': map(lambda palabra: palabra[-1], words),
        'isPalindrome': map(lambda palabra: palabra == palabra[::-1], words)
        }

df = pd.DataFrame(data=data)

df_mod = df.set_index('word')

df_mod.index.names = [None]

# Transformamos la columna star en dataframe e iteramos

df_start = df_mod.copy()
df_start = df_start['start'].to_frame()

for i in df_start.itertuples():
    print(f'La palabra {i[0]} comienza por {i[1]}')

# Transformamos la columna length en lista para eliminar una de sus entradas con el método .remove()

df_length = df_mod.copy()
df_length = df_length['length'].tolist()
df_length.remove(6)
print(df_length)

##############################################################

# EXAMEN DEL TEMA

##############################################################

# Ejercicio 01
# Crea un dataframe con 15 filas y 2 columnas. La primera columna se llamará x, la segunda y.
# Cada entrada será un número real a tu elección. Guarda el dataframe en una variable llamada points.

import pandas as pd

data = {'x': [2, -4, 6, -8, 10, 12, 14, -16, 18, -20, 22, 24, 26, 28, -30],
        'y': [1, 3, -5, 7, 9, -11, 13, 15, -17, 19, 21, -23, 25, 27, 29]}

points = pd.DataFrame(data=data)

print(points)

##############################################################

# Ejercicio 02
# Del dataset points, muestra las filas cuyo valor en la columna x sea positivo.

import pandas as pd

data = {'x': [2, -4, 6, -8, 10, 12, 14, -16, 18, -20, 22, 24, 26, 28, -30],
        'y': [1, 3, -5, 7, 9, -11, 13, 15, -17, 19, 21, -23, 25, 27, 29]}

points = pd.DataFrame(data=data)

print(points[points['x'] > 0])

##############################################################

# Ejercicio 03
# Del dataset points, muestra las filas cuyo valor en la columna y sea negativo. Usa el método .query().

import pandas as pd

data = {'x': [2, -4, 6, -8, 10, 12, 14, -16, 18, -20, 22, 24, 26, 28, -30],
        'y': [1, 3, -5, 7, 9, -11, 13, 15, -17, 19, 21, -23, 25, 27, 29]}

points = pd.DataFrame(data=data)

print(points.query('y < 0'))

##############################################################

# Ejercicio 04
# Del dataset points, muestra las observaciones cuyos puntos (x, y) pertenezcan al primer cuadrante.
# Usa el método .query().

import pandas as pd

data = {'x': [2, -4, 6, -8, 10, 12, 14, -16, 18, -20, 22, 24, 26, 28, -30],
        'y': [1, 3, -5, 7, 9, -11, 13, 15, -17, 19, 21, -23, 25, 27, 29]}

points = pd.DataFrame(data=data)

print(points.query('x > 0 and y > 0'))

##############################################################

# Ejercicio 05
# Del dataset points, muestra las observaciones de la forma:
# “El punto ({x}, {y}) {no/sí} pertenece al primer cuadrante”.

import pandas as pd

data = {'x': [2, -4, 6, -8, 10, 12, 14, -16, 18, -20, 22, 24, 26, 28, -30],
        'y': [1, 3, -5, 7, 9, -11, 13, 15, -17, 19, 21, -23, 25, 27, 29]}

points = pd.DataFrame(data=data)

for i in points.itertuples():
    if i[0] >= 0 and i[1] >= 0:
        c = 'si'
        print(f'El punto ({i[0]}, {i[1]}) {c} pertecene al primer cuadrante')
    else:
        c = 'no'
        print(f'El punto ({i[0]}, {i[1]}) {c} pertecene al primer cuadrante')
        
##############################################################

# Ejercicio 06
# Crea un dataframe con 10 filas y 4 columnas. La primera columna se llamará word; la segunda,
# length; la tercera, vowels; y la última, consonants. La columna words contendrá las siguientes
# 10 palabras: “euro”, “diez” “algas”, “broma”, “cicuta”, “fatiga”, “nachos”, “jadeos”, “hazañas”,
# “boutique”. Las columnas length, vowels y consonants contendrán, respectivamente, la longitud,
# el total de vocales y el total de consonantes. Guarda el dataframe en la variable words.

import pandas as pd


def vocal(palabra):
        """
        Cuenta las vocales de una palabra.
        :param palabra: La palabra a contar.
        :return: Número entero de vocales.
        """
        vocales = 'aeiou'
        c_vocales = 0
        for letra in palabra:
                if letra.lower() in vocales:
                        c_vocales += 1
                else:
                        continue
        return c_vocales


def conso(palabra):
        """
        Cuenta las consonantes de una palabra.
        :param palabra: La palabra a contar.
        :return: Número entero de consonantes.
        """
        consonantes = 'bcdfghjklmnñpqrstvwxyz'
        c_conso = 0
        for letra in palabra:
                if letra.lower() in consonantes:
                        c_conso += 1
                else:
                        continue
        return c_conso


palabras = ['euro', 'diez', 'algas', 'broma', 'cicuta', 'fatiga', 'nachos', 'jadeos', 'hazañas', 'boutique']

data = {'word': palabras,
        'length': map(len, palabras),
        'vowels': map(lambda palabra: vocal(palabra), palabras),
        'consonants': map(lambda palabra: conso(palabra), palabras)}

words = pd.DataFrame(data=data)

print(words)

##############################################################

# Ejercicio 07
# Muestra las 10 observaciones de words con el formato “La palabra {word} tiene {length} letras,
# de las cuales {vowels} son vocales y {consonants} consonantes”.

import pandas as pd


def vocal(palabra):
        """
        Cuenta las vocales de una palabra.
        :param palabra: La palabra a contar.
        :return: Número entero de vocales.
        """
        vocales = 'aeiou'
        c_vocales = 0
        for letra in palabra:
                if letra.lower() in vocales:
                        c_vocales += 1
                else:
                        continue
        return c_vocales


def conso(palabra):
        """
        Cuenta las consonantes de una palabra.
        :param palabra: La palabra a contar.
        :return: Número entero de consonantes.
        """
        consonantes = 'bcdfghjklmnñpqrstvwxyz'
        c_conso = 0
        for letra in palabra:
                if letra.lower() in consonantes:
                        c_conso += 1
                else:
                        continue
        return c_conso


palabras = ['euro', 'diez', 'algas', 'broma', 'cicuta', 'fatiga', 'nachos', 'jadeos', 'hazañas', 'boutique']

data = {'word': palabras,
        'length': map(len, palabras),
        'vowels': map(lambda palabra: vocal(palabra), palabras),
        'consonants': map(lambda palabra: conso(palabra), palabras)}

words = pd.DataFrame(data=data)

for i in words.itertuples():
        print(f'La palabra {i[1]} tiene {i[2]} letras, de las cuales {i[3]} son vocales y {i[4]} son consonantes')

##############################################################

# Ejercicio 08
# Muestra aquellas observaciones de words que tienen el mismo número de vocales y consonantes.
# Usa el método .query().

import pandas as pd


def vocal(palabra):
        """
        Cuenta las vocales de una palabra.
        :param palabra: La palabra a contar.
        :return: Número entero de vocales.
        """
        vocales = 'aeiou'
        c_vocales = 0
        for letra in palabra:
                if letra.lower() in vocales:
                        c_vocales += 1
                else:
                        continue
        return c_vocales


def conso(palabra):
        """
        Cuenta las consonantes de una palabra.
        :param palabra: La palabra a contar.
        :return: Número entero de consonantes.
        """
        consonantes = 'bcdfghjklmnñpqrstvwxyz'
        c_conso = 0
        for letra in palabra:
                if letra.lower() in consonantes:
                        c_conso += 1
                else:
                        continue
        return c_conso


palabras = ['euro', 'diez', 'algas', 'broma', 'cicuta', 'fatiga', 'nachos', 'jadeos', 'hazañas', 'boutique']

data = {'word': palabras,
        'length': map(len, palabras),
        'vowels': map(lambda palabra: vocal(palabra), palabras),
        'consonants': map(lambda palabra: conso(palabra), palabras)}

words = pd.DataFrame(data=data)

print(words.query('vowels == consonants'))

##############################################################

# Ejercicio 09
# Investiga el método .sort_values() para ordenar las observaciones según la longitud de las
# palabras en orden descendente.

import pandas as pd


def vocal(palabra):
        """
        Cuenta las vocales de una palabra.
        :param palabra: La palabra a contar.
        :return: Número entero de vocales.
        """
        vocales = 'aeiou'
        c_vocales = 0
        for letra in palabra:
                if letra.lower() in vocales:
                        c_vocales += 1
                else:
                        continue
        return c_vocales


def conso(palabra):
        """
        Cuenta las consonantes de una palabra.
        :param palabra: La palabra a contar.
        :return: Número entero de consonantes.
        """
        consonantes = 'bcdfghjklmnñpqrstvwxyz'
        c_conso = 0
        for letra in palabra:
                if letra.lower() in consonantes:
                        c_conso += 1
                else:
                        continue
        return c_conso


palabras = ['euro', 'diez', 'algas', 'broma', 'cicuta', 'fatiga', 'nachos', 'jadeos', 'hazañas', 'boutique']

data = {'word': palabras,
        'length': map(len, palabras),
        'vowels': map(lambda palabra: vocal(palabra), palabras),
        'consonants': map(lambda palabra: conso(palabra), palabras)}

words = pd.DataFrame(data=data)

print(words.sort_values(by=['length'], ascending=False))

##############################################################

