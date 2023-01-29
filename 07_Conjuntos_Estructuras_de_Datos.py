# EJERCICIOS y EXAMEN FINAL del Tema
# NOTA: No es necesario usar código para comprobar si los datos introducidos por el usuario son correctos.
# Vamos a interpretar que así es por ahora a menos que se especifique lo contrario.

# Tarea 01
# Vamos a pedirle al usuario una frase y vamos a guardar en un conjunto las letras que aparecen
# en dicha frase.

frase = str(input('Escribe una frase: '))
f = frase.lower()
set1 = set()

for l in f:

    if l.isalnum() is True:
        set1.add(l)

    else:
        continue

print(set1)

