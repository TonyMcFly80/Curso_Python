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

# Tarea 02
# Vamos a configurar el método .__str__() para que nos muestre el número racional de la forma
# numerador / denominador.
# EXTRA: Busca como usar LaTeX en strings de Python y construye el método .mathMode() que muestre
# el número racional en formato numerator
#                               ---------
#                               denominator

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

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

    def mathFormat(self):
        from IPython.display import display, Latex
        display(Latex(f'${self.numerator}\\over{self.denominator}$'))


q = RationalNumber(12, 8)
print(q)
q.mathFormat()

##############################################################
