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

asignaturas = {'Math': [], 'English': [], 'History': [], 'Science': [], 'IT': []}

for key in asignaturas:
    asignaturas[key].append(float(input(f'Introduce la primera nota para {key}: ')))
    asignaturas[key].append(float(input(f'Introduce la segunda nota para {key}: ')))
    asignaturas[key].append(float(input(f'Introduce la tercera nota para {key}: ')))

print('\n/// La Nota Final de cada Asignatura es: /// ')

for key in asignaturas:
    nota = sum(asignaturas[key]) / 3
    print(f'Tu nota de {key} es: {nota}')
    
