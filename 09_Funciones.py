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
