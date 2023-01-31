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

