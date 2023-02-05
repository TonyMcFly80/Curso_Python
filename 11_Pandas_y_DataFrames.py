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
