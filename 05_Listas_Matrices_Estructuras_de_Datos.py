# EJERCICIOS y EXAMEN FINAL del Tema
# NOTA: No es necesario usar código para comprobar si los datos introducidos por el usuario son correctos.
# Vamos a interpretar que así es por ahora a menos que se especifique lo contrario.

##############################################################

# Tarea 01
# Vamos a pedirle al usuario la longitud de una lista y haremos que introduzca por teclado
# tantos números enteros como haya indicado, que se guardarán en una lista. Al acabar, imprimiremos
# la lista.

print('Vamos a crear una lista!!!')
n = int(input('Cuantos números enteros va a tener la lista?: '))
contador = 0
lista = []

while n > contador:
    lista.append(int(input('Escribe un número entero: ')))
    contador += 1

print(lista)

##############################################################

# Tarea 02
# Dada una lista de caracteres, le pediremos al usuario qué elemento quiere eliminar
# y lo eliminaremos de la lista.

print('Vamos a crear una lista de caracteres!!!')
n = int(input('Cuantos caracteres va a tener la lista?: '))
contador = 0
lista = []

while n > contador:
    lista.append(str(input('Escribe una letra: ')))
    contador += 1

print('La lista es la siguiente:')
print(lista)

borrar = str(input('Qué letra quieres borrar?: '))

for letra in lista:
    if letra == borrar:
        lista.remove(borrar)

print('Esta es la nueva lista:')
print(lista)

##############################################################

# Tarea 03
# Vamos a pedir al usuario que ingrese 10 números, los guardaremos en una lista y mostraremos la
# lista ordenada, siendo el usuario quien indique el orden: Ascencente o Descendente.

print('Vamos a crear una lista de 10 números!!!')
n = 10
contador = 0
lista = []

while n > contador:
    lista.append(float(input('Escribe un número: ')))
    contador += 1

orden = int(input('En que orden deseas ver la lista? Ascendente marca 1, Descendente marca 0: '))

if orden == 1:
    lista.sort()
    print(lista)
elif orden == 0:
    lista.sort()
    lista.reverse()
    print(lista)
else:
    print('Datos Incorrectos')

##############################################################    
    
# Tarea 04
# Vamos a convertir los números impares del 0 al 30 a una lista y mostrar los elementos
# en formato "El valor {} ocupa el indice {}".

lista = []

for n in range(1, 31, 2):
    lista.append(n)
    print(f'El valor {n} ocupa el indice {lista.index(n)}')

##############################################################    
    
# Tarea 05
# Vamos a crear manualmente una matriz de tamaño 4 x 4 y guardarla en una lista.

print('/// Vamos a crear manualmente una matriz de tamaño 4 x 4 ///')

A = []

for i in range(4):
    A.append([])
    for j in range(4):
        A[i].append(int(input(f'Introduce el elemento ({i},{j}): ')))

for i in range(4):
    for j in range(4):
        print(A[i][j], end='  ' if A[i][j] >= 0 else ' ')
    print('')

##############################################################    
    
# Tarea 06
# Vamos a sumar dos matrices con listas. Ambas matrices serán porporcionadas por el usuario,
# así como la dimensión de las matrices:

print('/// Vamos a crear manualmente dos matrices que vamos a sumar ///')
m = int(input('Escribe que tamano de filas: '))
n = int(input('Escribe que tamano de columnas: '))

A = []
B = []

print('/// Vamos con la matriz A ///')
for i in range(m):
    A.append([])
    for j in range(n):
        A[i].append(int(input(f'Introduce el elemento ({i},{j}): ')))


print('/// Vamos con la matriz B ///')
for i in range(m):
    B.append([])
    for j in range(n):
        B[i].append(int(input(f'Introduce el elemento ({i},{j}): ')))


if len(A) == len(B) and len(A[0]) == len(B[0]):
    C = []

    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(A[i][j] + B[i][j])

    for i in range(m):
        for j in range(n):
            print(A[i][j], end='  ' if A[i][j] >= 0 else ' ')
        print('')

else:
    print('No se puede realizar la suma')

##############################################################    
    
# Tarea 07
# Vamos a calcular el producto de dos matrices con listas. Ambas matrices serán dadas por el
# usuario así como las dimensiones de ambas.

print('/// Vamos a crear manualmente dos matrices que vamos a multiplicar ///')
n = int(input('Escribe que tamano de filas tendrá A: '))
m = int(input('Escribe que tamano de columnas que tendrá A (y filas B): '))
p = int(input('Escribe que tamano de columnas que tendrá B: '))

A = []

print('/// Vamos con la Matriz A ///')
for i in range(n):
    A.append([])
    for j in range(m):
        A[i].append(float(input(f'Introduce el elemento ({i},{j}): ')))

B = []

print('/// Vamos con la Matriz B ///')
for i in range(m):
    B.append([])
    for j in range(p):
        B[i].append(float(input(f'Introduce el elemento ({i},{j}): ')))

C = []

for i in range(n):  # Para cada fila de A
    C.append([])    # Creamos en C una fila vacia (es decir una lista vacía)
    for j in range(p):  # Para cada columna de B
        elemento = 0    # Definimos el elemento de la suma igual a cero
        for k in range(m):  # Para cada fila de A o columna de B (que son iguales)
            elemento = elemento + A[i][k] * B[k][j]  # Cada elemento es igual al elemento + la fórmula
        C[i].append(elemento)   # Se añade a C la posición i el elemento/resultado en cada caso

print('/// Resultado Matriz A x B ///')
for i in range(n):
    for j in range(p):
        print(C[i][j], end='  ')
    print('')

##############################################################    
    
# Tarea 08
# Vamos a introducir manualmente una matriz con numpy donde las dimensiones son proporcionadas
# por el usuario.

import numpy as np

print('/// Vamos ha crear una matriz ///')
n = int(input('Cuantas filas tendrá la matriz?: '))
m = int(input('Cuantas columnas tendrá la matriz?: '))

A = np.empty((n, m))

for i in range(n):
    for j in range(m):
        A[i, j] = float(input(f'Introduce el elemento ({i},{j}): '))

print(A)

##############################################################

# Tarea 09
# Vamos a sumar dos matrices con numpy. Ambas matrices las proporcionará el usuario,
# así como sus dimensiones.

import numpy as np

print('/// Vamos ha crear los parámetros de las matrices a sumar A + B ///')
n = int(input('Cuantas filas?: '))
m = int(input('Cuantas columnas?: '))

print('/// Matriz A ///')
A = np.empty((n, m))

for i in range(n):
    for j in range(m):
        A[i, j] = float(input(f'Introduce el elemento ({i},{j}): '))

print('/// Matriz B ///')
B = np.empty((n, m))

for i in range(n):
    for j in range(m):
        B[i, j] = float(input(f'Introduce el elemento ({i},{j}): '))

matrixSum = A + B

print('/// Resultado A + B ///')
print(matrixSum)

##############################################################

# Tarea 10
# Vamos a multiplicar dos matrices con numpy. Ambas matrices serán proporcionadas por el usuario,
# así como la dimensión de ambas.

import numpy as np

print('/// Vamos ha crear los parámetros de las matrices a multi A x B ///')
n = int(input('Filas de A: '))
m = int(input('Columnas de A (y filas de B): '))
p = int(input('Columnas de B: '))

print('/// Matriz A ///')
A = np.empty((n, m))

for i in range(n):
    for j in range(m):
        A[i, j] = float(input(f'Introduce el elemento ({i},{j}): '))

print('/// Matriz B ///')
B = np.empty((m, p))

for i in range(m):
    for j in range(p):
        B[i, j] = float(input(f'Introduce el elemento ({i},{j}): '))

print('/// Resultado de A x B ///')
matrixProd = A.dot(B)

print(matrixProd)

##############################################################

# EXAMEN FINAL del Tema

##############################################################

# Ejercicio 1
# Crea un programa que lea una secuencia de caracteres, guarde cada caracter en una posición de una lista y
# finalmente muestre la secuencia invertida.

secuencia = str(input('Escribe una secuencia de caracteres: '))
lista = list(secuencia)
lista.reverse()
print(lista)

##############################################################

# Ejercicio 2
# Crea un programa que lea dos strings de la misma longitud, los guarde intercalados en una lista. Por último,
# mostrar el contenido de la lista.
# Por ejemplo, si introducimos hola caracola y adios marieta, debería mostrarse haodleao sc
# amraarcioeltaa.

string01 = str(input('Escribe una palabra: '))
string02 = str(input('Escribe otra palabra: '))

list(string01)
list(string02)

lista = []
contador1 = 0
contador2 = -1

for letra1 in string01:
    lista.insert(contador1, letra1)
    contador1 += 1

for letra2 in string02:
    contador2 += 2
    lista.insert(contador2, letra2)

cadena_mezclada = ''.join(lista)
print(cadena_mezclada)

##############################################################

# Ejercicio 3
# Crea un programa que lea un string y guarde en una lista todas las consonantes.

palabra = str(input('Escribe una palabra: '))
palabra_final = palabra.lower()

lista = []

for letra in palabra_final:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        continue
    lista.append(letra)

print(lista)

##############################################################

# Ejercicio 4
# Crea un programa que lea una palabra, la guarde en una lista y compruebe si se trata de un palíndromo.

palabra = str(input('Escribe una palabra o frase: ').replace(' ', ''))
lista = list(palabra.lower())

invertida = []

for letra in lista:
    invertida.append(letra)

invertida.reverse()

if lista == invertida:
    print('Es Palíndromo')

else:
    print('NO es Palíndromo')

##############################################################    
    
# Ejercicio 5
# Crea un programa que lea una matriz 3 x 3 y devuelva el máximo de cada fila

import numpy as np

n = 3
m = 3

matriz = np.empty((n, m))

for i in range(n):
    for j in range(m):
        matriz[i, j] = float(input(f'Introduce el elemento {i}, {j}: '))

# Fila 1
if matriz[0, 0] > matriz[0, 1] and matriz[0, 0] > matriz[0, 2]:
    print('La máxima de la fila 1 es', matriz[0, 0])

elif matriz[0, 1] > matriz[0, 0] and matriz[0, 1] > matriz[0, 2]:
    print('La máxima de la fila 1 es', matriz[0, 1])

else:
    print('La máxima de la fila 1 es', matriz[0, 2])

# Fila 2
if matriz[1, 0] > matriz[1, 1] and matriz[1, 0] > matriz[1, 2]:
    print('La máxima de la fila 2 es', matriz[1, 0])

elif matriz[1, 1] > matriz[1, 0] and matriz[1, 1] > matriz[1, 2]:
    print('La máxima de la fila 2 es', matriz[1, 1])

else:
    print('La máxima de la fila 2 es', matriz[1, 2])

# Fila 3
if matriz[2, 0] > matriz[2, 1] and matriz[2, 0] > matriz[2, 2]:
    print('La máxima de la fila 3 es', matriz[2, 0])

elif matriz[2, 1] > matriz[2, 0] and matriz[2, 1] > matriz[2, 2]:
    print('La máxima de la fila 3 es', matriz[2, 1])

else:
    print('La máxima de la fila 3 es', matriz[2, 2])

##############################################################    
    
# Ejercicio 6
# Crea un programa que lea un entero, n, de teclado y construya una matriz de tamaño n × n. Cada posición
# debe contener su orden en la matriz (desde 0 hasta n al cuadrado − 1. Por ejemplo, si n es 3, deberá crearse la matriz:
# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]

import numpy as np

n = int(input('Escribe un número entero: '))
contador = 0

matriz = []

for i in range(n):
    matriz.append([])

    for j in range(n):
        matriz[i].append(contador)
        contador += 1

print(np.matrix(matriz))

##############################################################

# Ejercicio 7
# Crea una matriz de n × m y asigna los valores manualmente. El programa debe indicar si la suma de cada
# columna es el mismo valor.

import numpy as np

n = int(input('Número de filas: '))
m = int(input('Número de columnas: '))

matriz = np.empty((n, m))

for i in range(n):

    for j in range(m):
        matriz[i, j] = float(input(f'Introduce el elemento {i}, {j}: '))

print('\n /// Matriz ///')
print(matriz)

suma = []

for j in range(m):
    operador = 0

    for i in range(n):
        operador += matriz[i][j]
    suma.append(operador)

suma_final = True

for i in range(m - 1):
    if suma[i] != suma[i + 1]:
        suma_final = False

if suma_final is True:
    print('La suma de las columnas es igual')

else:
    print('La suma de las columnas NO es igual')
    
##############################################################    
    
# Ejercicio 8
# Crear un programa determina si la matriz introducida manualmente (tanto sus dimensiones como los elementos)
# se trata de la matriz identidad. Recuerda que la matriz identidad debe ser una matriz cuadrada.

import numpy as np

n = int(input('Número de filas: '))
m = int(input('Número de columnas: '))

matriz = np.empty((n, m))

for i in range(n):

    for j in range(m):
        matriz[i, j] = float(input(f'Introduce el elemento {i}, {j}: '))

print('\n /// Matriz ///')
print(matriz)

matriz_identidad = True

if n == m:
    
    for i in range(n):
        
        for j in range(n):
            
            if i == j and matriz[i][j] != 1:
                matriz_identidad = False
            
            elif i != j and matriz[i][j] != 0:
                matriz_identidad = False

else:
    matriz_identidad = False

if matriz_identidad is True:
    print('SI es la Matriz Identidad')

else:
    print('NO es la Matriz Identidad')

##############################################################    
    
# Ejercicio 9
# Realiza un programa que calcule la matriz transpuesta.

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matriz_trans = []

for i in range(len(matriz[0])):
    matriz_trans.append([])

    for j in range(len(matriz)):
        matriz_trans[i].append(matriz[j][i])

for i in range(len(matriz_trans)):

    for j in range(len(matriz_trans[0])):
        print(matriz_trans[i][j], end=' ')
    print('')

##############################################################    
    
# Ejercicio 10
# Crea un programa que pida al usuario la dimensión y cree la matriz identidad de orden
# correspondiente con numpy.

import numpy as np

n = int(input('Escribe la dimensión de la matriz: '))

matriz = np.zeros((n, n))

for i in range(n):
    matriz[i, i] = 1

print(matriz)

##############################################################
