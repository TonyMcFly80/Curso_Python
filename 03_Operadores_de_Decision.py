# EJERCICIOS y EXAMEN FINAL del Tema
# NOTA: No es necesario usar código para comprobar si los datos introducidos por el usuario son correctos.
# Vamos a interpretar que así es por ahora a menos que se especifique lo contrario.

# Tarea 01
# Dado un str, vamos a comprobar si contiene espacios en blamco y, en caso de ser cierto,
# contaremos cuantos tiene.

s = 'He visto rayos-C brillar en la oscuridad cerca de la Puerta de Tannhäuser'
caracter = ' '
contador = s.count(caracter)

if caracter in s:
    print(f'El string tiene {contador} espacios.')
else:
    print('No tiene espacios')

# Tarea 02
# Vamos a hacer un programa que resuelva ecuaciones de primer grado de la forma Ax + B = 0
# proporcionadas por el usuario, donde A será distinta de 0.

print('Vamos a ejecutar una ecuación! Ax + B = 0')
A = float(input('Dime que valor tendrá A (No puede ser 0): '))
B = float(input('Dime que valor tendrá B: '))

if A != 0:
    solucion = -B / A
    print(f'La solución es x = {solucion}')

else:
    print('Los datos no son correctos')

# Tarea 03
# Vamos a comprobar si un número es par o impar usando el operador ternario.

numero = int(input('Escribe un número entero: '))
texto_par = f'El número {numero} es par.'
texto_impar = f'El número {numero} es impar.'

print(texto_par) if numero % 2 == 0 else print(texto_impar)

# Tarea 04
# Vamos a comprobar si un año es bisiesto o no.
# Un año es bisiesto si es divisible entre 4, pero no es multiplo de cien, a no ser que lo sea de 400.

year = int(input('Introduce un año y comprobaremos si es bisiesto: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'El año {year} SI es bisiesto')
        else:
            print(f'El año {year} NO es bisiesto')
    else:
        print(f'El año {year} SI es bisiesto')
else:
    print(f'El año {year} NO es bisiesto')

    
# EXAMEN FINAL del Tema

# Ejercicio 1
# Haz que un usuario introduzca un número real y evalúa si dicho número es positivo, negativo o
# cero. Devuelve por pantalla el resultado en cada caso.

numero = float(input('Introduce un número: '))

if numero < 0:
    print('El número introducido es negativo')
elif numero > 0:
    print('El número introducido es positivo')
else:
    print('El número introducido es cero')

# Ejercicio 2
# Haz que un usuario introduzca su nombre y evalúa con operadores if y else si dicho nombre tiene una
# longitud mayor a 10 caracteres o no. Devuelve por pantalla el resultado en cada caso.

nombre = input('Escribe tu nombre: ')
if len(nombre) >= 10:
    print(f'Tu nombre {nombre} tiene al menos 10 caracteres')
else:
    print(f'Tu nombre {nombre} es inferior a 10 caracteres')
    
# Ejercicio 3
# Realiza el ejercicio anterior con el uso del operador ternario.

nombre = input('Escribe tu nombre: ')
print(f'Tu nombre {nombre} tiene al menos 10 caracteres') if len(nombre) > 10 else print(f'Tu nombre {nombre} es inferior a 10 caracteres')

# Ejercicio 4
# Haz que un usuario introduzca dos números enteros positivos. Comprueba si el primer número introducido
# por el usuario es mayor o igual que el segundo número introducido por el usuario. Devuelve por pantalla el
# resultado en cada caso.

num1 = int(input('Introduce un número entero positivo: '))
num2 = int(input('Introduce un segundo número entero positivo: '))

if num1 > num2:
    print(f'El número {num1} es mayor a {num2}.')
elif num1 == num2:
    print(f'Ambos números: {num1} y {num2} son iguales.')
else:
    print(f'El número {num1} es menor a {num2}.')

# Ejercicio 5
# Haz que un usuario introduzca dos números enteros positivos. Suponiendo que el primer número introducido
# por el usuario es mayor o igual al segundo número introducido por el usuario, comprueba que la división del
# primer número entre el segundo número es exacta.
# En caso de la división ser exacta, devuelve el cociente por pantalla e indica que la división en efecto es exacta.
# En caso de la división no ser exacta, devuelve el cociente y el resto por pantalla e indica que la división entre
# los dos números no es exacta.

num1 = int(input('Introduce un número entero positivo: '))
num2 = int(input('Introduce un segundo número entero positivo menor o igual al anterior: '))

if num1 >= num2:
 
    if num1 % num2 == 0:
        cociente = num1 / num2
        print(f'El resultado de dicha división es {cociente} y es exacta.')
 
    elif num1 % num2 != 0:
        cociente = num1 / num2
        resto = num1 % num2
        print(f'El resultado de dicha división es {cociente} con un resto de {resto}.')
        
else:
    print('Los números no son válidos')

# Ejercicio 6
# Fusiona lo hecho en los ejercicios 4 y 5 para que:
# 1. Un usuario introduzca dos números enteros por pantalla.
# 2. Comprobar si el primer número es mayor o igual al segundo número introducido por el usuario. Devolver
# por pantalla en que caso nos encontramos.
# 3. Hacer la división entera pertinente en cada caso.
# 4. Si la división es exacta, entonces devolver por pantalla el cociente e indicar que la división es exacta.
# Si la división no es exacta, entonces devolver por pantalla el cociente y el resto e indicar que la división
# realizada no es exacta.

num1 = int(input('Introduce un número entero positivo: '))
num2 = int(input('Introduce un segundo número entero positivo menor o igual al anterior: '))

if num1 >= num2:
    print(f'El número {num1} es mayor o igual al número {num2}.')

    if num1 % num2 == 0:
        cociente = num1 / num2
        print(f'El resultado de dicha división es {cociente} y es exacta.')

    elif num1 % num2 != 0:
        cociente = num1 / num2
        resto = num1 % num2
        print(f'El resultado de dicha división es {cociente} con un resto de {resto}.')

else:
    print(f'El número {num1} es menor a {num2}.')
    print('Los números no son válidos')
    
# Ejercicio 7
# Haz que un usuario introduzca dos números enteros positivos. Comprueba si el mayor es múltiplo del menor.
# Devuelve por pantalla el resultado en cada caso.

num1 = int(input('Introduce un número entero positivo: '))
num2 = int(input('Introduce un segundo número entero positivo menor al anterior: '))

if num1 > num2:
    
    if num1 % num2 == 0:
        print(f'{num1} es múltiplo de {num2}')
 
    elif num1 % num2 != 0:
        print(f'{num1} no es múltiplo de {num2}')

else:
    print('Los números no son válidos')
    
# Ejercicio 8
# Haz que un usuario introduzca una palabra y comprueba si dicha palabra empieza por mayúscula. Devuelve
# por pantalla el resultado en cada caso.

palabra = input('Escribe una palabra: ')

if palabra.isalpha() is False:
    print(f'La palabra \"{palabra}\" no es válida')

elif palabra[0].isupper() is True:
    print(f'La palabra \"{palabra}\" comienza por mayúsculas.')

else:
    print(f'La palabra \"{palabra}\" comienza por minúsculas.')
    
# Ejercicio 9
# Haz un usuario introduza una letra y comprueba si se trata de una vocal. Si el usuario introduce un string
# de más de un carácter, infórmale de que no se puede procesar el dato, pues debe tener como máximo tamaño 1.

letra = input('Escribe una sola letra: ')
letra = letra.lower()

if letra.isalpha() is False or len(letra) > 1:
    print(f'El dato introducido \"{letra}\" no cumple con los requisitos')

elif letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'El dato introducido \"{letra}\" se trata de una vocal')
    
else:
    print(f'El dato introducido \"{letra}\" se trata de una consonante')

# Ejercicio 10
# Dada una ecuación de segundo grado:
# 1. Comprueba que el coeficiente A es distinto de 0.
# 2. En función del discriminante, calcula cuántas soluciones va a tener la ecuación de segundo grado.
# 3. Devuelve por pantalla el resultado en cada caso (tanto el número de soluciones en los números reales
# como el valor de estas).

import math

print('Vamos a realizar una ecuación de sgundo grado!!')
a = int(input('Escribe el coeficiente A (No puede ser 0): '))
b = int(input('Escribe el coeficiente B: '))
c = int(input('Escribe el coeficiente C: '))

discriminante = b ** 2 - 4 * a * c

if a != 0:
    
    if discriminante > 0:
        print('Tenemos dos soluciones!')
        sol1 = (-b + math.sqrt(discriminante)) / (2 * a)
        sol2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print(f'Solución 1 = {sol1} y Solución 2 = {sol2}')
        
    elif discriminante == 0:
        sol3 = (-b) / (2 * a)
        print(f'La solución es {sol3}')
        
    else:
        print('La ecuación no tiene solución')
        
else:
    print('A es igual a 0, por tanto, datos incorrectos.')

