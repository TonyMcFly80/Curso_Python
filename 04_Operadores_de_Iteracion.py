# EJERCICIOS y EXAMEN FINAL del Tema
# NOTA: No es necesario usar código para comprobar si los datos introducidos por el usuario son correctos.
# Vamos a interpretar que así es por ahora a menos que se especifique lo contrario.

# Tarea 01
# Con un bucle while, dado un string vamos a recorrer una frase y contar el número total de vocales.

frase = str(input('Escribe una frase y te diré cuantas vocales tiene: '))
f = frase.lower()
n = 0
long = int(len(frase))
total = 0

while n <= (long - 1):
    if f[n] == 'a' or f[n] == 'e' or f[n] == 'i' or f[n] == 'o' or f[n] == 'u':
        n += 1
        total += 1
    else:
        n += 1

print(f'La frase introducida tiene {total} vocales.')

# Tarea 02
# Con un bucle while, dados dos números enteros proporcionados por el usuario, vamos a encontrar el
# primer número divisible entre 2, 3 y 5, siempre que sea posible, que se encuentre dentro del intervalo
# formado por los dos números dados por el usuario (ambos extremos también incluidos).

num1 = int(input('Escribe un número entero: '))
num2 = int(input('Escribe otro número entero: '))

if num1 > num2:

    while num2 <= num1:
        if num2 % 2 == 0 and num2 % 3 == 0 and num2 % 5 == 0:
            print(f'{num2} se puede dividir entre 2, 3 y 5')
            num2 += 1
            break

elif num1 < num2:

    while num1 <= num2:
        if num1 % 2 == 0 and num1 % 3 == 0 and num1 % 5 == 0:
            print(f'{num1} se puede dividir entre 2, 3 y 5')
            num1 += 1
        else:
            num1 += 1
else:
    print('Error ambos números no pueden ser iguales')

# Tarea 03
# Vamos a hacer que el usuario introduzca números por teclado e ir sumándolos. Cuando el usuario
# introduzca 0 saldremos del bucle while. Al salir del bucle, con un else mostraremos la suma.

n = float(input('Introduce un número y lo iremos sumando hasta que escribas 0: '))
suma = float(0)

while n != 0:
    suma += n
    n = float(input('Introduce un número y lo iremos sumando hasta que escribas 0: '))

else:
    print(f'La suma total es {suma}')

# Tarea 04
# Imaginemos las letras del abecedario ordenadas y dispuestas en círculo. Es decir, a la derecha
# de la A está la B, luego la C, y así sucesivamente hasta la Z. A la derecha de la Z, se encuentra de
# nuevo la letra A.

# Vamos a hacer que el usuario introduzca un valor entero n, que se corresponderá con la rotación que
# llevará a una determinada letra n posiciones a su derecha. Por ejemplo, si la rotación es 4, entonces la A
# pasará a la E, la B a la F, ..., la Y a la C y la Z a la D.

# Con un bucle while, vamos a construir el programa que desplazará las letras n posiciones a la derecha.

# PISTA: Investiga las funciones chr() y ord() para pasar del valor ASCII de un caracter y viceversa.

print('Vamos a girar la rueda del Abecedario!')
abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
print(f'Esta es la posición actual: {abecedario}')
n = int(input('Cuantas pociciones quieres mover?: '))
inicio = 65

while inicio <= 90:
    if inicio + n <= 90:
        print(chr(inicio + n))
    else:
        print(chr((inicio - 26) + n))
    inicio += 1

# Tarea 05
# Vamos a recorrer un string dado un bucle for y lo vamos a devolver del revés.

frase = str(input('Escribe una frase: '))
frase_invertida = str('')

for letra in frase:
    frase_invertida = letra + frase_invertida

print(frase_invertida)

# Tarea 06
# Con un bucle for, dada una progresión aritmética de números enteros indicada por el usuario
# (nos dará el primer término, la diferencía y la cota), vamos a calcular la suma de los
# elementos incluyendo la cota.

# Un ejemplo de progresión aritmética es: 0, 2, 4, 6, 8,... donde el primer término es 0 y la
# diferencia entre sus términos es 2.

print('Vamos a sumar una progresión aritmética!!! Para ello necesito unos datos...')

ini = int(input('Con qué número quieres comenzar?: '))
fin = int(input('Con qué número quieres finalizar?: '))
salto = int(input('Cada cuanto quieres contar?... ejemplo (de 1 en 1, 2 en 2, etc): '))
suma = 0

for n in range(ini, fin + 1, salto):
    print(n)
    suma += n

print(f'La suma total es de {suma}')

# Tarea 07
# Con un bucle for, vamos a recorrer un string dado y vamos a imprimir todas las letras salvo por
# la letra indicada por el usuario.

frase = str(input('Escribe una frase: '))
frase = frase.lower()
letra_x = str(input('Qué letra quieres hacer desaparecer de la frase?: '))
letra_x = letra_x.lower()
final = ''

for letra in frase:
    if letra == letra_x:
        continue
    else:
        final += letra

print(final)

# Tarea 08
# Dado un string, con un bucle for vamos a imprimirlo sin vocales y vamos a salir del bucle
# si la letra que indique el usuario aparece más de n veces, número que támbien nos proporcionará
# el usuario.

frase = str(input('Escribe una frase: '))
frase = frase.lower()
letra_x = str(input('Cual es la letra maldita? (no puede ser vocal): '))
letra_x = letra_x.lower()
repe = int(input('Cuantas veces tiene que salir la letra maldita?: '))
f_final = ''
contador = 0

for letra in frase:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        continue
    elif letra == letra_x:
        contador += 1
        f_final += letra
        if contador == repe:
            break
    else:
        f_final += letra

print(f_final)

# EXAMEN FINAL del Tema

# Ejercicio 1
# Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, muestra
# si el número introducido es par o impar.

numero = int(input('Introduce un número entero: '))

while numero > 0:

    if numero % 2 == 0:
        print(f'El número {numero} es par')

    elif numero % 2 != 0:
        print(f'El número {numero} es impar')

    elif numero <= 0:
        break
    numero = int(input('Introduce un número entero: '))

# Ejercicio 2
# Haz que el usuario introduzca una palabra y una letra por teclado. Comprueba si la palabra contiene la
# letra o no e indícaselo al usuario por pantalla.

palabra = input('Introduce una palabra: ').lower()
letra = input('Introduce una letra: ').lower()
contador = 0

for x in palabra:

    if x == letra:
        print(f'La letra {letra} se encuentra en la palabra {palabra}')
        break

    elif x != letra:
        contador += 1
        if contador == len(palabra):
            print(f'La letra {letra} NO se encuentra en la palabra {palabra}')
            break
    else:
        continue
       
# Ejercicio 3
# Haz que el usuario introduzca precios por teclado (si introduce 0, entonces es que ha finalizado). Si el usuario
# pasa de 200€, entonces ya no debe poder introducir más precios pues se ha pasado de presupuesto. Sea cual
# sea el resultado (o bien el precio final o bien que no tiene más presupuesto), indícaselo por pantalla al usuario.

ahorros = 200
print(f'Tienes {ahorros} euros en tu cuenta.')

while ahorros > 0:
    retirada = float(input('Cuanto dinero quieres sacar?: '))
    
    if retirada == 0:
        print('Fin del programa')
        break
 
    elif retirada <= ahorros:
        ahorros -= retirada
        
        if ahorros > 0:
            print(f'Aún tienes {ahorros} euros')
            continue
 
        elif ahorros == 0:
            print('Ya no te queda dinero')
            break
 
        elif ahorros < 0:
            print(f'No tienes tanto dinero para retirar. Tienes disponible {ahorros} euros')
            continue
 
    else:
        print(f'No tienes tanto dinero para retirar. Tienes disponible {ahorros} euros')
        continue
 
# Ejercicio 4
# Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, calcula
# cuántos números positivos y cuántos negativos ha introducido y muéstraselo al final.

print('/// Escribe un número entero positivo o negativo (0 para finalizar el programa) ///')

contador_positivios = 0
contador_negativos = 0

while True:
    numero = int(input('Número: '))

    if numero > 0:
        contador_positivios += 1
        continue

    elif numero < 0:
        contador_negativos += 1
        continue

    else:
        print(f'Has introducido {contador_positivios} números positivos y {contador_negativos} números negativos')
        print('Fin del programa...')
        break

# Ejercicio 5
# Haz que el usuario introduzca números por teclado. Mientras el usuario no introduzca el 0, pídele otro
# número. Cuando el usuario introduzca el 0, muéstrale la media aritmética de los números que ha introducido.

print('/// Escribe un número (0 para finalizar el programa) ///')
suma = 0

while True:
    numero = float(input('Número: '))

    if numero != 0:
        suma = suma + numero
        continue

    else:
        print(f'La media aritmética es {suma/2}')
        break

# Ejercicio 6
# Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
# intervalo y, el segundo, el extremo derecho. Imprime todos los números que se encuentren entre los dos
# números introducidos por el usuario (los extremos incluidos).

print('/// Escribe dos números enteros, el primero debe ser menor al segundo ///')

numero1 = int(input('Escribe un 1er número entero: '))
numero2 = int(input('Escribe un 2do número entero: '))

for numero in range(numero1, numero2+1):
    print(numero)

# Ejercicio 7
# Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
# intervalo y, el segundo, el extremo derecho. Imprime la suma de todos los múltiplos de 3 que se encuentren
# entre los dos números introducidos por el usuario (los extremos incluidos). Finalmente, muestra por pantalla
# el resultado de la suma.

print('/// Escribe dos números enteros, el primero debe ser menor al segundo ///')

numero1 = int(input('Escribe un 1er número entero: '))
numero2 = int(input('Escribe un 2do número entero: '))
suma_mult_3 = 0

for numero in range(numero1, numero2+1):

    if numero % 3 == 0:
        suma_mult_3 = numero + suma_mult_3
        continue

    else:
        continue

print(f'La suma de los múltiplos de 3 es {suma_mult_3}')

# Ejercicio 8
# Pídele al usuario cuántos números va a introducir. Con un bucle for, solicítale esa cantidad de números y
# calcula su producto.

print('/// Escribe los numeros que deseas multiplicar ///')

total = int(input('Cuantos números vas a introducir?: '))
producto = 1

for n in range(0, total):
    numero = int(input('Escribe un número: '))
    producto = (producto * numero)
    continue

print(f'El producto es {producto}')

# Ejercicio 9
# Haz que el usuario introduzca su edad y el año actual. Imprime todos los años que han pasado desde su año
# de nacimiento hasta el año actual (ambos incluidos).

edad = int(input('Escribe tu edad: '))
year_actual = int(input('En qué año estamos?: '))

year_nacimiento = year_actual - edad

for years in range(year_nacimiento, year_actual+1):
    print(years)
  
# Ejercicio 10
# Haz que el usuario introduzca un número entero entre 3 y 10. Muestra un cuadrado y luego un triángulo rectángulo de
# lado y altura, respectivamente, el número entero introducido. Por ejemplo, si el usuario introduce como
# número 5, se deberá mostrar:
# *          * * * * *
# * *        * * * * *
# * * *      * * * * *
# * * * *    * * * * *
# * * * * *  * * * * *

print('Vamos a dibujar un triángulo y un cuadrado!')

numero = int(input('Escribe un número entero entre 3 y 10: '))

for i in range(numero):
    print('* ' * (i + 1) + ' ' * (20 - (2 * i + 2) + 1) + '* ' * numero)
