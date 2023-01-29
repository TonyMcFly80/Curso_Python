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

if B < A or D < C:
    print('Los intervalos no son correctos.')

else:
    for n in range(A, B + 1):
        set1.add(n)

    for n in range(C, D + 1):
        set2.add(n)

    set3 = set1.symmetric_difference(set2)

    print(set3)

# Tarea 04
# Vamos a guardar en un conjunto los números primos comprendidos entre 2 y el número n que nos
# indique el usuario mediante la criba de Eratóstenes.

n = int(input('Escribe un número entero mayor que 2: '))
primos = set(range(2, n + 1))       # Rango completo de números introducidos
numeros = list(range(2, n + 1))     # Lista igual que primos para poder trabajar
multiplos = [True for x in range(len(numeros))]     #Lista Booleana con todo en True

for i in range(len(numeros)):   # Índice de toda la lista
    if multiplos[i] == False:   # Si el número que está trabajando es False, continuamos.
        continue

    for j in range(i + 1, len(numeros)):    # Consideramos el siguiente número True
        if numeros[j] % numeros[i] == 0:    # Comprobamos si j es multiplo de i
            multiplos[j] = False            # Si es multiplo lo tachamos
            primos.discard(numeros[j])      # Y lo eliminamos del conjunto

print(primos)
    
# Tarea 05
# Vamos a crear un programa que nos devuelva el elemento máximo de un conjunto sin utilizar
# la función max().

set1 = {2, 13, -7, 14, 5, 0, -1, 3, 9}
ok = -100

for n in set1:

    if n > ok:
        ok = n

    else:
        continue

print(f'El número mayor de {set1} es {ok}')


# EXAMEN DEL TEMA

# Ejercicio 01
# Dado un número entero introducido por teclado, guarda sus divisores en un conjunto y muéstralo.

print('/// Vamos a calcular todos los divisores de un número ///')

n = int(input('Qué numero vamos a dividir?: '))
set1 = set()

for i in range(1, n + 1):

    if n % i == 0:
        set1.add(i)

    else:
        continue

print('Estos son los divisores:')
print(set1)

# Ejercicio 02
# Crea un programa que dado un conjunto, nos devuelva su mínimo. Debes hacerlo sin recurrir a la función
# min().

set1 = {2, 13, -7, 14, 5, 0, -1, 3, 9}
ok = 100

for n in set1:

    if n < ok:
        ok = n

    else:
        continue

print(f'El número menor de {set1} es {ok}')
