# EJERCICIOS y EXAMEN FINAL del Tema
# NOTA: No es necesario usar código para comprobar si los datos introducidos por el usuario son correctos.
# Vamos a interpretar que así es por ahora a menos que se especifique lo contrario.

# Tarea 01
# Vamos a crear una función que cuente y devuelva todas las apariciones de una letra proporcionada
# por parámetro en una frase también proporcionada por parámetro.

def contar_letras(fr, le):
    fr = fr.lower()
    le = le.lower()
    n = fr.count(le)
    return n


frase = str(input('Escribe una frase: '))
letra = str(input('Escribe una letra: '))

print(f'En la frase \"{frase}\" la letra \"{letra}\" aparace \"{contar_letras(fr=frase, le=letra)}\" veces.')

# Tarea 02
# Vamos a crear una función que muestre por pantalla el triángulo de Pascal. Por parámetro se
# indicará el número de filas a mostrar. Por defecto n valdrá 1.
# Para calcular el número combinatorio en Python, utilizaremos el siguiente método:

def combi(n, k):       # Calcula el número combinatorio n sobre k
    import math

    if (n >= k and k >= 0):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

    else:
        return 'No se puede calcular el número factorial indicado'

def trian_pascal(n = 1):
    print(1)

    for i in range(1, n + 1):
        for k in range(i + 1):
            print(combi(i, k), end=' ')
        print('')


trian_pascal(5)

# Tarea 03
# Vamos a crear una función recursiva que lleve a cabo una cuenta atrás.

def cuenta_atras(number):
    """
    Cuenta atrás recursiva.

    :param
        number: Número entero positivo.
        if: Garantizamos que una vez llegemos a cero, parará.
        print: Vamos mostrando el número.

    :return:
        Ejecutamos de nuevo la función restando 1 al número.
    """
    if number >= 0:
        print(number)
        return cuenta_atras(number - 1)


cuenta_atras(30)

# Tarea 04
# Vamos a crear una función recursiva que calcule el factorial de un número entero positivo.

def factorial(n):
    """
        Calcula el número factorial de un número entero positivo
    
    :param 
        n: El número entero positivo
    
    :return:
        Factorial de n
    """

    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))

# Tarea 05
# Vamos a crear una función que resuelva ecuaciones de primer grado de la forma Ax + B = 0
# Siempre que A no sea 0.

def ecuaciones_grado1(a, b):
    """
    Resuelve ecuaciones de primer grado en la forma Ax + B = 0
    
    :param a: Número real (coeficiente de x)
    
    :param b: Número real (término independiente)
    
    :return: Valor de x o Datos incorrectos
    
    """
    if a != 0:
        x = -b / a
        return x

    else:
        return 'Datos incorrectos'


A = float(input('Dime que valor tendrá A (No puede ser 0): '))
B = float(input('Dime que valor tendrá B: '))
print(ecuaciones_grado1(A, B))
