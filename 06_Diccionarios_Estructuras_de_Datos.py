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


# EXAMEN DEL TEMA

# Ejercicio 1
# Crea un programa que pida un número entero positivo por teclado y que cree un diccionario cuyas claves
# sean desde el número 1 hasta el número indicado. Los valores de cada clave serán las propias claves elevadas
# al cubo.

print('/// Vamos a crear un diccionario de números que iran desde el 0 hasta el número que quieras ///')

number = int(input('Escribe el número entero positivo que quieras: '))
dicc = {}

for n in range(1, number):
    dicc.setdefault(n, n**3)

print(dicc)

# Ejercicio 2
# Escribe un programa que pregunte al usuario su nombre, edad y teléfono y lo guarde en un diccionario.
# Después, debe mostrar por pantalla el mensaje ‘{nombre} tiene {edad} años y su número de teléfono es
# {teléfono}.

print('/// Vamos a preguntarte algunos datos ///')

dicc = {}

nombre = dicc.setdefault('Nombre', str(input('Cual es tu nombre?: ')))
edad = dicc.setdefault('Edad', str(input('Cual es tu edad?: ')))
telefono = dicc.setdefault('Teléfono', int(input('Cual es tu número de teléfono?: ')))

print(f'{nombre} tiene {edad} años y su número de teléfono es {telefono}')
print(dicc)

# Ejercicio 3
# Escribe un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar
# el artículo y su precio por unidad. El artículo será la clave y el valor el precio, hasta que el usuario decida
# terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
# Artículo 1    Precio
# Artículo 2    Precio
# Artículo 3    Precio
# . . .         . . .
# Total         Precio Total


print('/// Vamos a calcular el coste de tu cesta de la compra ///')

cesta = {}
total = 0
ok = 1

while ok != 0:
    articulo = str(input('Escribe el nombre del artículo: '))
    precio = float(input('Marca el precio del artículo: '))
    cesta.setdefault(articulo, precio)
    ok = int(input('Desea finalizar? (1=NO , 0=SI): '))

print('\n/// LISTA DE LA COMPRA ///\n')

for i in cesta:
    print(f'{i}\t\t\t\t\t{cesta[i]}')

for j in cesta:
    total += cesta[j]

print(f' * * * \t\t\t\t\t * * * ')
print(f'Total\t\t\t\t\t{total}')
