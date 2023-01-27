# EJERCICIOS y EXAMEN FINAL del Tema
# NOTA: No es necesario usar código para comprobar si los datos introducidos por el usuario son correctos.
# Vamos a interpretar que así es por ahora a menos que se especifique lo contrario.

# Tarea 01
# Vamos a hacer que el usuario rellene una ficha de cliente y vamos a guardar toda la información
# en un diccionario. Para ello, vamos a pedir el nombre, apellidos, edad, dni y el dinero total que
# va a pagar el cliente.

print('Introduce los siguentes datos...')

datos_cliente = {'Nombre':    str(input('Nombre: ')),
                 'Apellidos': str(input('Apellidos: ')),
                 'Edad':      int(input('Edad: ')),
                 'DNI':       str(input('DNI: ')),
                 'Dinero':    float(input('¿Cuanto dinero va a pagar?: '))
                 }

print(datos_cliente)

# Tarea 02
# Tenemos un diccionario con 5 claves: Math, English, History, Science, IT. Cada clave contiene una
# lista de tamaño 3, donde cada una de esas entradas se corresponde con una nota de 0 a 10. El usuario
# va a ser quien introduzca esas notas por teclado. Finalmente, para cada clave, mostraremos la media
# de las 3 notas.

asignaturas = {'Math': [], 
               'English': [], 
               'History': [], 
               'Science': [], 
               'IT': []}

for key in asignaturas:
    asignaturas[key].append(float(input(f'Introduce la primera nota para {key}: ')))
    asignaturas[key].append(float(input(f'Introduce la segunda nota para {key}: ')))
    asignaturas[key].append(float(input(f'Introduce la tercera nota para {key}: ')))

print('\n/// La Nota Final de cada Asignatura es: /// ')

for key in asignaturas:
    nota = sum(asignaturas[key]) / 3
    print(f'Tu nota de {key} es: {nota}')
    
# Tarea 03
# Dado un diccionario, vamos a solicitar al usuario una clave que quiera eliminar y vamos a eliminarla.
# Al final, le mostraremos el dicc actualizado.

dicc = {'Nombre': 'Juan',
        'Apellido': 'Sanchez',
        'Edad': 38,
        'Profesión': 'Pintor',
        }
print('/// Estas son las claves de este diccionario ///')

for key in dicc:
    print(key)

eliminar = str(input('Cual deseas eliminar?: '))

dicc.pop(eliminar)

print(dicc)

# Tarea 04
# Vamos a solicitar al usuario 8 números enteros del 0 al 9. Se supone que son los números de su
# DNI, que guardaremos cada uno en una entrada de una lista. A continuación, con esos números calcularemos
# la letra correspondiente y la guardaremos en una variable. Finalmente, crearemos un diccionario con
# dos claves, cada una guardará, respectivamente, los números y la letra del DNI. Finalmente, mostraremos
# el diccionario resultante.
print('/// Vamos a solicitarte tu número de DNI sin la letra ///')

n_dni = []
cont = 1

for n in range(8):
    n_dni.append(str(input(f'Escribe el número en posición {cont} de tu DNI: ')))
    cont += 1

dicc_letra = {0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F', 8: 'P', 9: 'D', 10: 'X',
              11: 'B', 12: 'N', 13: 'J', 14: 'Z', 15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L', 20: 'C',
              21: 'K', 22: 'E'}

numero = ''

for n in n_dni:
    numero += str(n)

calculo = int(numero) % 23

letra = dicc_letra[calculo]

DNI = {'Número': numero, 'Letra': letra}

print(DNI)

# Tarea 05
# Vamos a leer un string por teclado y vamos a devolver un diccionario con la cantidad de apariciones
# de cada caracter en el string proporcionado por el usuario.

intro = str(input('Escribe una palabra o una frase: '))
letras = intro.lower()

dicc = {}

for l in letras:

    if l == ' ':
        continue

    else:
        dicc.setdefault(l, letras.count(l))

print(dicc)
