# EXAMEN Strings con Python

# Ejercicio 1
# Utiliza las funciones de concatenar, + y repetir strings, *, junto con la función print()
# para dados los siguientes strings s1, s2, s3 y s4, conseguir el resultado siguiente:
# Había una vez, un barquito chiquitito Había una vez, un barquito chiquitito que no podía,
# que no podía, que no podía navegar.

s1 = "Había una vez, "
s2 = "un barquito chiquitito "
s3 = "que no podía, "
s4 = "que no podía navegar."
print(((s1 + s2) * 2) + (s3 * 2) + s4)

# Ejercicio 2
# Utiliza la función print() y el comando de salto de línea, \n, para reproducir exactamente
# el siguiente texto:
# Érase un hombre a una nariz pegado,
# Érase una nariz superlativa,
# Érase una alquitara medio viva,
# Érase un peje espada mal barbado;

print('Érase un hombre a una nariz pegado,\nÉrase una nariz superlativa,\n'
      'Érase una alquitara medio viva,\nÉrase un peje espada mal barbado;')

# Ejercicio 3
# Transforma el siguiente string s a mayúsculas y muéstralo por pantalla con la función print():
# s = "me encantan las matemáticas"

s = "me encantan las matemáticas"
print(s.upper())

# Ejercicio 4
# Calcula la longitud del string s
# s = "Mi pasión por el chocolate es superior a mis fuerzas"

s = "Mi pasión por el chocolate es superior a mis fuerzas"
longitud = len(s)
print(longitud)

# Ejercicio 5
# Del string s del ejercicio anterior, obtén el substring chocolate y guárdalo en una variable
# llamada s_sub.
# No vale contar, deberás hallar los índices del substring con el método .find()
# (o el que mejor consideres) y la función len().
# Finalmente, imprime tu resultado por pantalla

s = "Mi pasión por el chocolate es superior a mis fuerzas"
inicio = s.find('chocolate')
fin = inicio + len('chocolate')
s_sub = s[inicio:fin]
print(s_sub)

# Ejercicio 6
# Con la función input(), indícale al usuario que introduzca su nombre y guárdalo en la variable
# llamada nombre

nombre = str(input('Escribe tu nombre: '))

# Ejercicio 7
# Con la función input(), indícale al usuario que introduzca su apellido y guárdalo en la variable
# llamada apellido

apellido = str(input('Escribe tu apellido: '))

# Ejercicio 8
# Con la función input(), indícale al usuario que introduzca su edad y guárdala en la variable
# llamada edad.

edad = int(input('Escribe tu edad: '))

# Ejercicio 9
# Con la función input(), indícale al usuario que introduzca la ciudad en la que vive y guárdala
# en la variable llamada ciudad

ciudad = str(input('Escribe tu ciudad: '))

# Ejercicio 10
# Con lo hecho en los ejercicios 6, 7, 8 y 9, imprime por pantalla todos los datos introducidos
# por el usuario tal y como se muestra en el siguiente ejemplo, donde el usuario ha indicado que
# su nombre es María; su apellido, Santos; su edad, 21; y su ciudad, Palma de Mallorca.

nombre = str(input('Escribe tu nombre: '))
apellido = str(input('Escribe tu apellido: '))
edad = int(input('Escribe tu edad: '))
ciudad = str(input('Escribe tu ciudad: '))
print(f'Su nombre es {nombre} {apellido}, tiene {edad} años y actualmente vive en {ciudad}.')

