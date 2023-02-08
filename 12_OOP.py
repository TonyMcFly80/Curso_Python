# EJERCICIOS y EXAMEN FINAL del Tema
# NOTA: No es necesario usar código para comprobar si los datos introducidos por el usuario son correctos.
# Vamos a interpretar que así es por ahora a menos que se especifique lo contrario.

##############################################################

# Tarea 01
# Vamos a crear la clase RationalNumber. Vamos a configurar el constructor de modo que haya un
# atributo numerator y otro denominator, este último con 1 como valor por defecto. Ambos atributos
# deben ser números enteros.

class RationalNumber():
    """
    Clase para trabajar con números racionales.
    """
    def __init__(self, numerator, denominator=1):
        if type(numerator) is int and type(denominator) is int:
            self.numerator = numerator
            self.denominator = denominator
        else:
            print('ERROR... Ambos números deben ser números enteros')

##############################################################
