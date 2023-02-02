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

# Tarea 06
# Vamos a crear una función que haga de calculadora (suma, resta, producto y división),
# haciendo uso de funciones helper para mostrar la operación realizada. Pediremos por parámetro
# tipo de operación ("sum", "subract", "product", "division") y dos números reales. Devolveremos
# el resultado de la operación correspondiente.

def helper_calculadora(operacion, x, y, resultado):
    print(f'La {operacion} de {x} y {y} es igual {resultado}')


def calculadora(operacion, x, y):
    """
    Calculadora que resuelve una operacion aritmética para los valores X e Y

    :param operacion: String que indica el tipo de operación aritmética

    :param x: Primer valor entero

    :param y: Segundo valor entero

    :return: Solución de la operación
    """
    if operacion == 'sum':
        resultado = x + y
        helper_calculadora(operacion, x, y, resultado)

    elif operacion == 'subract':
        resultado = x - y
        helper_calculadora(operacion, x, y, resultado)

    elif operacion == 'product':
        resultado = x * y
        helper_calculadora(operacion, x, y, resultado)

    elif operacion == 'division':
        if x < y:
            print('Esta operación no se puede resolver')
        else:
            resultado = x / y
            helper_calculadora(operacion, x, y, resultado)

    else:
        print('Operación incorrecta')


print('Vamos va realizar una operación matemática!')
operacion = str(input('Cual eliges "sum", "subract", "product", "division": '))
num1 = int(input('Introduce un número entero: '))
num2 = int(input('Introduce un otro número entero: '))
print(calculadora(operacion, num1, num2))


# EXAMEN DEL TEMA


# Ejercicio 01
# Crea una función que busque todos los divisores del número entero positivo dado por parámetro y devuelva
# una lista con todos los divisores de dicho número.

def divisores(num):
    """
    Busca todos los divisores de un número entero.
    :param num: Número entero solicitado.
    :return: Lista con todos los divisores del número entero 
    """
    lista = []

    for i in range(1, num + 1):

        if num % i == 0:
            lista.append(i)

        else:
            continue

    return lista


# Ejercicio 02
# Crea una función que dados dos números reales por parámetro, devuelve el mayor.

def comparativa(x, y):
    """
    Calcula que número es mayor.
    :param x: Número entero
    :param y: Número entero
    :return: Devuelve el número mayor de ambos en cada caso, a menos que sean iguales
    """
    if x > y:
        return x

    elif y > x:
        return y

    else:
        return 'Son iguales'

    
# Ejercicio 03
# Crea una función que dado un número devuelva su valor absoluto.

def valor_absoluto(num):
    """
    Calculamos el valor absoluto de un número.
    :param num: Número a calcular.
    :return: Valor absoluto de número
    """
    if num >= 0:
        return num
    else:
        return num * -1

    
# Ejercicio 04
# Crea una función que devuelva True si el caracter introducido por parámetro se trata de una vocal
# y False en caso contrario.

def verificador(letra):
    """
    Verifica si el caracter introducido es una vocal.
    :param letra: Caracter introducido.
    :return: True o False si es o no vocal.
    """
    alf = 'aeiou'
    if letra in alf:
        return True
    else:
        return False
    
    
# Ejercicio 05
# Crea una función que devuelva el MCD (máximo común divisor) de 2 números proporcionados por parámetro.

def mcd(num1, num2):
    """
    Devuelve el máximo común divisor de 2 números
    :param num1: Número entero
    :param num2: Número entero
    :return: El máximo común divisor de num1 y num2
    """
    if num1 > num2:
        menor = num2
    else:
        menor = num1

    for i in range(1, menor + 1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            mcd_final = i
    return mcd_final


# Ejercicio 06
# Crea una función que devuelva el MCM (mínimo común múltiplo) de 2 números proporcionados por
# parámetro.

def mcd(num1, num2):
    """
    Devuelve el máximo común divisor de 2 números
    :param num1: Número entero
    :param num2: Número entero
    :return: El máximo común divisor de num1 y num2
    """
    if num1 > num2:
        menor = num2
    else:
        menor = num1

    for i in range(1, menor + 1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            mcd_final = i
    return mcd_final


def mcm(num1, num2):
    """
    Calculamos el mínimo común multiplo de 2 números
    :param num1: Número entero
    :param num2: Número entero
    :return: Resultado mínimo común multiplo basado en multiplar los números dados
            y dividirlos por el máximo común divisor de esos mismos números.
    """
    return (num1 * num2) / mcd(num1, num2)


# Ejercicio 07
# Crea una función que dada una palabra devuelva si es palíndroma.

def palindromo(palabra):
    """
    Analiza la palabra y devuelve si es o no palíndroma.
    :param palabra: Palabra introducida.
    :return: Si es o no palíndroma.
    """
    p = palabra.lower()

    if p == p[::-1]:
        return 'Es Palindroma'
    else:
        return 'NO es palíndroma'

# Ejercicio 08
# Crea una función que dado un color en hexadecimal devuelva una lista de 3 posiciones, cada una de ellas
# correspondiente al valor R, G o B en este orden. Los valores de RGB varían entre 0 y 255.

def conv_hex_rgb(hexa):
    """
    Convierte un codigo de color hexadecimal en codigo rgb.
    :param hexa: El codigo hexadecimal
    :return: El código rgb en orden R-G-B
    """
    hexa = hexa.lower()
    dicc = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 ,'a': 10,
            'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

    lista = []
    listaf = []
    rgb = []

    for elemento in hexa:
        lista.append(elemento)

    for i in range(len(hexa)):
        listaf.append(dicc[hexa[i]])

    rgb.append(int((listaf[0] * 16) + listaf[1]))
    rgb.append(int((listaf[2] * 16) + listaf[3]))
    rgb.append(int((listaf[4] * 16) + listaf[5]))

    return rgb
