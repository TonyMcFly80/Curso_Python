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
