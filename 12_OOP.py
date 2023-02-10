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
        d, i = math.modf(num)  
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
p5 = RationalNumber(1).fromRealNumber(0.72)

print(p2)
print(p3)
print(p4)
print(p5)

##############################################################

# Tarea 05
# Vamos a convertir los métodos .quotient() y .mathFormat() en una propiedad.

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

    @property
    def mathFormat(self):
        from IPython.display import display, Latex
        display(Latex(f'${self.numerator}\\over{self.denominator}$'))

    @property
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
        d, i = math.modf(num)
        while d != 0:
            num *= 10
            den *= 10
            d, i = math.modf(num)
        num = int(num)
        den = int(den)
        return cls(num, den)


q = RationalNumber.random()
q.mathFormat
print(q.quotient)

##############################################################

# Tarea 06
# Dada la clase Point2D, vamos a crear la clase Point3D que hereda de Point2D.
# Vamos a modificar todos los métodos y usar el método .super() donde sea necesario para poder usarlos
# con puntos en 3 dimensiones.

class Point2D(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    @classmethod
    def zero(cls):
        return cls(0, 0)


class Point3D(Point2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return super().__str__()[:-1] + f', {self.z})'

    @classmethod
    def zero(cls):
        return cls(0, 0, 0)


p = Point2D(1, -1)
print(p)

q = Point3D(1, 2, 3)
print(q)

cero2d = Point2D.zero()
print(cero2d)

cero3d = Point3D.zero()
print(cero3d)

##############################################################

# Tarea 07
# Dadas las clases Triangle y Square, vamos a crear la clase Pyramid que hereda de las dos anteriores.
# Practicaremos la herencia múltiple. Vamos a implementar el constructor, el método .area() y el
# método .volume() usando el método .super() donde sea necesario para poder construir una pirámide
# regular con base cuadrada y calcular correctamente el área y el volumen.

class Square(object):
    def __init__(self, base):
        self.base = base

    @property
    def perimeter(self):
        return 4 * self.base

    @property
    def area(self):
        return self.base * self.base


class Triangle(object):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def area(self):
        return 0.5 * self.base * self.height

import math

class Pyramid(Square, Triangle):
    def __init__(self, base, height):
        super().__init__(base)
        # Altura de la pirámide
        self.height = height

    @property
    def slant_height(self):
        return math.sqrt((self.base / 2) ** 2 + self.height ** 2)

    @property
    def area(self):
        base_area = super().area
        base_perimeter = super().perimeter
        lateral_area = 0.5 * base_perimeter * self.slant_height
        return lateral_area + base_area

    @property
    def volume(self):
        base_area = super().area
        return base_area * self.height / 3


p = Pyramid(2, 2)
print(p.area)
print(p.volume)

##############################################################

# EXAMEN DEL TEMA

##############################################################

# Ejercicio 01
# A lo largo de toda esta taraea vas a construir la clase Date. Empieza con el constructor,
# que recibe por parámetros el día (day), mes (month) y año (year). Los 3 parámetros son de tipo int
# y por defecto todos valen 1.

class Date(object):
    """
    Muestra dia, mes y año.
    """
    def __init__(self, day=1, month=1, year=1):
        if type(day) is int and type(month) is int and type(year) is int:
            self.day = day
            self.month = month
            self.year = year
        else:
            print('ERROR... Datos introducidos incorrectos')


##############################################################

# Ejercicio 02
# Configura el método .__str__() para que muestre la fecha en formato day / month / year.
# Si el valor del día o el mes son menores a 10, mostrar el valor con un 0 delante.
# Por ejemplo, si day = 8, month = 7 y year = 1998, entonces se debería mostrar 08 / 07 / 1998.
# En el caso del año, si el año es menor a 1000, mostrar con un cero delante; si es menor a 100,
# mostrar con 2 ceros delante; y si es menor a 10, mostrar con 3 ceros delante.
# PISTA: Puedes crear una función que dado un número entero y el número de cifras que debe tener,
# rellene con ceros a la izquierda hasta completar el número de cifras indicado.

class Date(object):
    """
    Muestra dia, mes y año.
    """

    def __init__(self, day=1, month=1, year=1):
        if type(day) is int and type(month) is int and type(year) is int:
            self.day = day
            self.month = month
            self.year = year
        else:
            print('ERROR... Datos introducidos incorrectos')

    @staticmethod
    def add_zero_d(day):
        if day < 10:
            return f'0{day}'
        else:
            return f'{day}'

    @staticmethod
    def add_zero_m(month):
        if month < 10:
            return f'0{month}'
        else:
            return f'{month}'

    @staticmethod
    def add_zero_y(year):
        if year in range(1, 10):
            return f'000{year}'
        elif year in range(10, 100):
            return f'00{year}'
        elif year in range(100, 1000):
            return f'0{year}'
        else:
            return f'{year}'

    def __str__(self):
        return f'{Date.add_zero_d(self.day)} / {Date.add_zero_m(self.month)} / {Date.add_zero_y(self.year)}'


fecha = Date(1, 9, 980)
print(fecha)

##############################################################

# Ejercicio 03
# Implementa el método de instancia .isLeap() que diga si el año es bisiesto o no.

class Date(object):
    """
    Muestra dia, mes y año.
    """

    def __init__(self, day=1, month=1, year=1):
        if type(day) is int and type(month) is int and type(year) is int:
            self.day = day
            self.month = month
            self.year = year
        else:
            print('ERROR... Datos introducidos incorrectos')

    @staticmethod
    def add_zero_d(day):
        if day < 10:
            return f'0{day}'
        else:
            return f'{day}'

    @staticmethod
    def add_zero_m(month):
        if month < 10:
            return f'0{month}'
        else:
            return f'{month}'

    @staticmethod
    def add_zero_y(year):
        if year in range(1, 10):
            return f'000{year}'
        elif year in range(10, 100):
            return f'00{year}'
        elif year in range(100, 1000):
            return f'0{year}'
        else:
            return f'{year}'

    def __str__(self):
        return f'{Date.add_zero_d(self.day)} / {Date.add_zero_m(self.month)} / {Date.add_zero_y(self.year)}'

    def isLead(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    print(f'El año {self.year} SI es bisiesto')
                else:
                    print(f'El año {self.year} NO es bisiesto')
            else:
                print(f'El año {self.year} SI es bisiesto')
        else:
            print(f'El año {self.year} NO es bisiesto')


fecha = Date(1, 9, 980)
fecha.isLead()

##############################################################
