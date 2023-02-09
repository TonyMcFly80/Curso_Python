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

# Tarea 03
# Implementa un método de instancia .quotient() que devuelva el cociente
# Implementa un método de instancia .isInfinite() que devuelva si el denominador es 0 o no
# Implementa un método de instancia .simplify() que simplifique la fracción a la fracción irreducible

def bigger(a, b):
  """
  Devuelve el mayor número de 2 números reales dados.
  Args:
    a: Número real
    b: Número real
  Returns:
    Número real
  """
  if a >= b:
    return a
  return b

def lower(a, b):
  """
  Devuelve el menor número de 2 números reales dados.
  Args:
    a: Número real
    b: Número real
  Returns:
    Número real
  """
  if a <= b:
    return a
  return b

def mcd(a, b):
  """
  Devuelve el MCD de dos números enteros.
  Args:
    a: Número entero
    b: Número entero
  Returns:
    max: Número entero
  """
  r = 0
  max = bigger(a, b)
  min = lower(a, b)
  while(min > 0):
    r = min
    min = max % min
    max = r
  return max

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

    def quotient(self):
        cociente = self.numerator // self.denominator
        return cociente

    def isInfinite(self):
        if self.denominator == 0:
            return True
        return False

    def simplify(self):
        div = mcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / div)
        self.denominator = int(self.denominator / div)


# Creamos y mostramos el objeto
q = RationalNumber(2, 4)
q.mathFormat()

# Mostramos el cociente
print(q.quotient())

# Mostramos si el denominador es 0
print(q.isInfinite())

# Mostramos la fracción irreducible
q.simplify()
q.mathFormat()

##############################################################
