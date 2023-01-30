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
