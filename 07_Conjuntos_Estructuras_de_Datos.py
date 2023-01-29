# EJERCICIOS y EXAMEN FINAL del Tema
# NOTA: No es necesario usar código para comprobar si los datos introducidos por el usuario son correctos.
# Vamos a interpretar que así es por ahora a menos que se especifique lo contrario.

# Tarea 01
# Vamos a pedirle al usuario una frase y vamos a guardar en un conjunto las letras que aparecen
# en dicha frase.

frase = str(input('Escribe una frase: '))
f = frase.lower()
set1 = set()

for l in f:

    if l.isalnum() is True:
        set1.add(l)

    else:
        continue

print(set1)

# Tarea 02
# Vamos a pedirle al usuario dos palabras y vamos a calcular la intersección de las letras de cada
# palabra. Para ello habrá que crear dos conjuntos que contendrán, respectivamente, las letras que
# forman cada palabra.

palabra1 = str(input('Escribe una palabra: '))
palabra2 = str(input('Escribe otra palabra: '))
p1 = palabra1.lower()
p2 = palabra2.lower()

set1 = set()
set2 = set()

for l in p1:    # Creamos conjunto de la primera palabra.

    if l.isalnum() is True:
        set1.add(l)

    else:
        continue

for l in p2:    # Creamos conjunto de la segunda palabra.

    if l.isalnum() is True:
        set2.add(l)

    else:
        continue

set3 = set1.intersection(set2)

print(set3)

# Tarea 03
# Vamos a pedirle 4 números enteros al usuario. Se corresponderán con los extremos de los intervalos
# [a,b] y [c,d]. Vamos a generar dos conjuntos que guarden, respectivamente, los enteros contenidos en
# cada uno de los intervalos (incluyendo los extremos) y, finalmente, calcularemos la diferencia
# simétrica.

print('Vamos a pedirte 4 numeros que crearán 2 intervalos de números... de A a B, y de C a D...')

A = int(input('Escribe número para A: '))
B = int(input('Escribe número para B: '))
C = int(input('Escribe número para C: '))
D = int(input('Escribe número para D: '))

set1 = set()
set2 = set()

for n in range(A, B + 1):
    set1.add(n)

for n in range(C, D + 1):
    set2.add(n)

set3 = set1.symmetric_difference(set2)

print(set3)
