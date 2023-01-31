# EJERCICIOS y EXAMEN FINAL del Tema
# NOTA: No es necesario usar código para comprobar si los datos introducidos por el usuario son correctos.
# Vamos a interpretar que así es por ahora a menos que se especifique lo contrario.

# Tarea 01
# Vamos a pedirle al usuario el número de números enteros que va a introducir por teclado. Para cada
# uno de esos números, vamos a crear una tupla donde la primera entrada sea el número entero, y la segunda,
# la palabra 'positivo', 'negativo' o 'cero' según el signo del número entero.
# Vamos a guardar todas las tuplas en una lista y la vamos a mostrar.

number = int(input('Cuantos números deseas introducir?: '))

tuplas = []

for n in range(1, number + 1):
    num = int(input(f'Nº{n} - Escribe un número entero: '))

    if num > 0:
        t = (num, 'positivo')
        tuplas.append(t)

    elif num < 0:
        t = (num, 'negativo')
        tuplas.append(t)

    else:
        t = (num, 'cero')
        tuplas.append(t)

print(tuplas)

# Tarea 02
# Vamos a pedirle al usuario números enteros del 1 al 10 hasta que introduzca el 0. Para cada uno
# de esos números, vamos a crear una tupla donde la primera entrada sea el número entero y, la
# segunda, la palabra 'suspenso', 'aprobado', 'notable' o 'excelente' según el intervalo al que
# pertenezca el número entero. Vamos a mostrar la tupla recién creada al usuario.

# Las diferentes categorías son:

# suspenso [1,5]
# aprobado [5,7]
# notable [7,9]
# excelente [9,10]

while True:
    numero = int(input('Escribe un número del 1 al 10 (0 para finalizar el programa): '))

    if numero in range(1, 5):
        t = (numero, 'Suspenso')
        print(t)

    elif numero in range(5, 7):
        t = (numero, 'Aprobado')
        print(t)

    elif numero in range(7, 9):
        t = (numero, 'Notable')
        print(t)

    elif numero in range(9, 11):
        t = (numero, 'Excelente')
        print(t)

    elif numero == 0:
        print('FIN del programa')
        break

    else:
        print('Número incorrecto')

# Tarea 03
# Dada una frase introducida por el usuario, vamos a crear una lista con 3 tuplas y 2 entradas.
# La primera tupla tendrá el número de vocales; la segunda, el número de consonantes; y la última,
# el número de espacios en blanco. Para cada tupla, la primera entrada será un string explicativo
# y, la segunda, el valor correspondiente.

frase = str(input('Escribe una frase: '))
frase = frase.lower()
lista = []

vocales = 'aeiou'
consonantes = 'bcdfghijklmnñpqrstvwxyz'
espacio = ' '

count_v = 0
count_c = 0
count_e = 0

for letra in frase:

    if letra in vocales:
        count_v += 1

    elif letra in consonantes:
        count_c += 1

    elif letra in espacio:
        count_e += 1

    else:
        continue

t1 = ('Vocales en la frase', count_v)
lista.append(t1)

t2 = ('Consonantes en la frase', count_c)
lista.append(t2)

t3 = ('Espacios en la frase', count_e)
lista.append(t3)

print(lista)

# Tarea 04
# Vamos a pedirle al usuario una asignatura ('Mates', 'Lengua', 'Historia', 'Informática' o 'Música')
# y la nota en dicha asignatura hasta que introduzca una asignatura diferente a las indicadas.
# El usuario puede repetir una asignatura tantas veces como quiera. La nota tendrá que ser del 1 al 10.
# Guardaremos la información (asignatura, nota) en una tupla. Las tuplas serán guardadas en una lista.
# Finalmente, para cada asignatura, vamos a mostrar la nota media.

lista = []

c_mat = 0
c_len = 0
c_his = 0
c_inf = 0
c_mus = 0

mat = 0
len = 0
his = 0
inf = 0
mus = 0

while True:
    asignatura = int(input('Elige entre 1.Mates, 2.Lengua, 3.Historia, 4.Informatica o 5.Musica (0 para Finalizar): '))

    if asignatura == 1:
        nota = float(input('Escribe la nota de Mates: '))
        mat = mat + nota
        c_mat += 1

    elif asignatura == 2:
        nota = float(input('Escribe la nota de Lengua: '))
        len = len + nota
        c_len += 1

    elif asignatura == 3:
        nota = float(input('Escribe la nota de Historia: '))
        his = his + nota
        c_his += 1

    elif asignatura == 4:
        nota = float(input('Escribe la nota de Informática: '))
        inf = inf + nota
        c_inf += 1

    elif asignatura == 5:
        nota = float(input('Escribe la nota de Música: '))
        mus = mus + nota
        c_mus += 1

    else:
        break

t1 = ('Mates', mat / c_mat)
lista.append(t1)

t2 = ('Lengua', len / c_len)
lista.append(t2)

t3 = ('Historia', his / c_his)
lista.append(t3)

t4 = ('Informática', inf / c_inf)
lista.append(t4)

t5 = ('Música', mus / c_mus)
lista.append(t5)

print('\nLas notas medias de las asignaturas son:\n')
print(lista)

# Tarea 05
# Vamos a pedirle al usuario el número de puntos de un plano que quiere introducir. Para cada punto,
# vamos a solicitarle las coordenadas x e y. Guardaremos las coordenadas (x, y) en tuplas de tamaño 3,
# donde la última entrada se corresponde con el cuadrante al que pertenece dicho punto. Todas las tuplas
# de tamaño 3 serán guardadas en una lista. Finalmente, mostraremos todas las tuplas de tamaño 3 creadas,
# con el formato "El punto ({x}, {y}) pertenece al cuadrante {cuadrante}"

n = int(input("¿Cuántos puntos vas a introducir? "))
puntos = []

for i in range(n):
    x = float(input("Indica la coordenada x = "))
    y = float(input("Indica la coordenada y = "))

    if x >= 0 and y >= 0:
        cuadrante = "I"

    elif x <= 0 and y >= 0:
        cuadrante = "II"

    elif x <= 0 and y <= 0:
        cuadrante = "III"

    elif x >= 0 and y <= 0:
        cuadrante = "IV"

    elif x == 0 and y == 0:
        cuadrante = "center"

    puntos.append((x, y, cuadrante))

for punto in puntos:
    x, y, cuadrante = punto
    print(f"El punto ({x}, {y}) pertenece al cuadrante {cuadrante}")
    
# Tarea 06
# Dada una lista de palabras, vamos a crear otra lista del mismo tamaño que guarde la primera
# letra de cada palabra en la posición correspondiente. Por último, con la función zip() crearemos
# una tupla de tuplas con la palabra en la primera entrada y la letra con la que empieza, en la segunda.

palabras = ['frodo', 'sam', 'pippin', 'merry']
iniciales = []

for xp in palabras:
    iniciales.append(xp[0])

anillo = zip(palabras, iniciales)

tupla = tuple(anillo)

print(tupla)


# EXAMEN

# Ejercicio 01
# Pide al usuario el número de números enteros que va a introducir por teclado. Para cada uno de esos
# números, crea una tupla donde la primera entrada sea el número entero y, la segunda, la palabra “par” o
# “impar” según la paridad del número entero. Muestra la tupla recién creada al usuario.

number = int(input('Cuantos números deseas introducir?: '))

for n in range(1, number + 1):
    num = int(input(f'Nº{n} - Escribe un número entero: '))

    if num % 2 == 0:
        print((num, 'par'))

    else:
        print((num, 'impar'))

print('FIN DEL PROGRAMA')

# Ejercicio 02
# Dado un año proporcionado por el usuario, crea una tupla de dos elementos cuya primera entrada sea el año
# y, la segunda entrada, el horóscopo chino correspondiente.

year = int(input('Introduce un año: '))

formula = year % 12

dicc = {0: 'Mono', 1: 'Gallo', 2: 'Perro', 3: 'Cerdo', 4: 'Rata', 5: 'Buey', 6: 'Tigre', 7: 'Conejo',
        8: 'Dragón', 9: 'Serpiente', 10: 'Caballo', 11: 'Cabra'}

for key, value in dicc.items():

    if key == formula:
        t = year, value
        print(t)

    else:
        continue

# Ejercicio 03
# Dada una frase proporcionada por el usuario, crea una lista de tuplas indicando palabra, longitud de cada
# palabra, letra inicial y posición que ocupan dentro de la frase.

frase = str(input('Escribe una frase: '))
frase = frase.lower()

final = frase.split(' ')

lista = []

indice = 1

for palabra in final:
    t = palabra, len(palabra), palabra[0], indice
    indice += 1
    lista.append(t)

print(lista)

# Ejercicio 04
# Haz que el usuario introduzca palabras hasta que introduzca una palabra vacía. Guarda todas las palabras
# en una tupla y muestra la primera y la última introducidas haciendo uso del método unpacking.
# PISTA: Para guardar los elementos de uno en uno vas a tener que utilizar un tipo de dato que no es tupla
# y luego transformarlo a tupla.

lista = []

while True:

    palabra = str(input('Escribe una palabra (Enter para finalizar): '))

    if palabra != '':
        lista.append(palabra.lower())

    else:
        break

tupla = tuple(lista)
(palabra1, *resto, palabra2) = tupla

print((palabra1, palabra2))
