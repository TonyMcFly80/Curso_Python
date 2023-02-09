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

# Tarea 04
# Vamos a implementar lo siguientes métodos estáticos:
# .sum(), .subract(), .product(), .division()

def helper(n, d):
    """
    Print de los decoradores de la Clase RatinalNumber y no repetir código.
    :param n: Numerador
    :param d: Donominador
    :return: print
    """
    print(f'{n} / {d} = {n / d}')


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

    @staticmethod
    def sum(p, q):
        num = p.numerator * q.denominator + q.numerator * p.denominator
        den = p.denominator * q.denominator
        helper(num, den)

    @staticmethod
    def subract(p, q):
        num = p.numerator * q.denominator - q.numerator * p.denominator
        den = p.denominator * q.denominator
        helper(num, den)

    @staticmethod
    def product(p, q):
        num = p.numerator * q.numerator
        den = p.denominator * q.denominator
        helper(num, den)

    @staticmethod
    def division(p, q):
        num = p.numerator * q.denominator
        den = p.denominator * q.numerator
        helper(num, den)


p = RationalNumber(1, 2)
q = RationalNumber(2, 3)

RationalNumber.sum(p, q)
RationalNumber.subract(p, q)
RationalNumber.product(p, q)
RationalNumber.division(p, q)

##############################################################

# Tarea 05
# Vamos a configurar los siguientes métodos de clase:
# .random() que se encarga de crear un objeto aleatorio de la clase RationalNumber.
# .zero() que se encarga de crear el objeto de la clase RationalNumber que tiene por numerador 0 y
# denominador 1.
# .one() que se encarga de crear el objeto de la clase RationalNumber que tiene por numerador 1 y
# denominador 1.
# .fromRealNumber() que dado un número real se encarga de buscar su expresión en racional.
# Por ejemplo, dado 5.4, tendremos que crear el objeto RationalNumber con numerador 54 y denominador 10.
# Investiga el método math.modf() para este caso.
import math


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

def helper(n, d):
    """
    Print de los decoradores de la Clase RatinalNumber y no repetir código.
    :param n: Numerador
    :param d: Donominador
    :return: print
    """
    print(f'{n} / {d} = {n / d}')

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
        cociente = self.numerator / self.denominator
        return cociente

    def isInfinite(self):
        if self.denominator == 0:
            return True
        return False

    def simplify(self):
        div = mcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / div)
        self.denominator = int(self.denominator / div)

    @staticmethod
    def sum(p, q):
        num = p.numerator * q.denominator + q.numerator * p.denominator
        den = p.denominator * q.denominator
        helper(num, den)

    @staticmethod
    def subract(p, q):
        num = p.numerator * q.denominator - q.numerator * p.denominator
        den = p.denominator * q.denominator
        helper(num, den)

    @staticmethod
    def product(p, q):
        num = p.numerator * q.numerator
        den = p.denominator * q.denominator
        helper(num, den)

    @staticmethod
    def division(p, q):
        num = p.numerator * q.denominator
        den = p.denominator * q.numerator
        helper(num, den)

    @classmethod
    def random(cls):
        import random
        num = random.randrange(1, 101)
        den = random.randrange(1, 101)
        return cls(num, den)

    @classmethod
    def zero(cls):
        num = 0
        den = 1
        return cls(num, den)

    @classmethod
    def one(cls):
        num = 1
        den = 1
        return cls(num, den)

    @classmethod
    def fromRealNumber(cls, f):  # f representa al float que tenemos que introducir
        import math
        num = f
        den = 1
        d, i = math.modf(num)  # d representa la parte decimal / i representa la parte entera
        while d != 0:
            num *= 10
            den *= 10
            d, i = math.modf(num)
        num = int(num)
        den = int(den)
        return cls(num, den)


p2 = RationalNumber(1).random()
p3 = RationalNumber(1).zero()
p4 = RationalNumber(1).one()
p5 = RationalNumber(1).fromRealNumber(5.4)

print(p2)
print(p3)
print(p4)
print(p5)

##############################################################
