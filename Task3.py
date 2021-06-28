# Create a Fraction class, which will represent all basic arithmetic logic
# for fractions (+, -, /, *) with appropriate checking and error handling
from math import gcd


class Fraction:
    def __init__(self, numerator, denominator=None):
        if denominator is None:
            """Отработка, если вводится дробь с плавающей точкой"""
            if isinstance(numerator, (int, float)):
                self.numerator = numerator
                self.denominator = 1
                self.floating_to_fraction()
            else:
                raise ZeroDivisionError('Необходим тип данных int или float')
        else:
            """Отработка, если вводится числитель и знаменатель"""
            self.numerator = self.proper_argument(numerator, 'числителя')
            self.denominator = self.proper_argument(denominator, 'знаменателя')
            self.valid_denominator()
        self.fraction_reduction()
        self.negative_value_logic()

    @staticmethod
    def proper_argument(arg, comment):
        if isinstance(arg, int) or arg - int(arg) == 0:
            return int(arg)
        else:
            raise ValueError(f'Для {comment} требуется целочисленное значение')

    def floating_to_fraction(self):
        """Переводим дробь с плавающей точкой в обычную"""
        while(True):
            if self.numerator - int(self.numerator) == 0:
                self.numerator = int(self.numerator)
                break
            self.numerator *= 10
            self.denominator *= 10

    def valid_denominator(self):
        if self.denominator == 0:
            raise ValueError('Знаменатель не может равняться нулю')

    def fraction_reduction(self):
        """Функция сокращает дробь"""
        while(True):
            divisor = gcd(self.numerator, self.denominator)
            if divisor == 1:
                break
            else:
                self.numerator /= divisor
                self.denominator /= divisor
                self.numerator = int(self.numerator)
                self.denominator = int(self.denominator)

    def negative_value_logic(self):
        """Функция для изменения знакака знаменателя"""
        if self.denominator < 0:
            self.denominator *= -1
            self.numerator *= -1

    def __repr__(self):
        if self.numerator == 0:
            return '0'
        elif self.denominator == 1:
            return f'{self.numerator}'
        elif abs(self.numerator) > self.denominator:
            integer_part = int(self.numerator / self.denominator)
            new_numerator = abs(self.numerator) % self.denominator
            if new_numerator == 0:
                return f'{integer_part}'
            else:
                return f'{integer_part} ({new_numerator}/{self.denominator})'
        else:
            return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        return self.add_and_sub(other, '+')

    def __sub__(self, other):
        return self.add_and_sub(other, '-')

    def add_and_sub(self, other, math):
        denominator1 = self.denominator
        denominator2 = other.denominator
        denominator_new = denominator1 * denominator2
        if math == '-':
            numerator_new = self.numerator * denominator2 - other.numerator * denominator1
        else:
            numerator_new = self.numerator * denominator2 + other.numerator * denominator1
        new_fraction = Fraction(numerator_new, denominator_new)
        return new_fraction

    def __mul__(self, other):
        denominator_new = self.denominator * other.denominator
        numerator_new = self.numerator * other.numerator
        new_fraction = Fraction(numerator_new, denominator_new)
        return new_fraction

    def __truediv__(self, other):
        denominator_new = self.denominator * other.numerator
        numerator_new = self.numerator * other.denominator
        new_fraction = Fraction(numerator_new, denominator_new)
        return new_fraction


try:
    a = Fraction(1, 5)
    b = Fraction(-15/5)
    print(f'a = {a}, b = {b}')
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
except ValueError as massage:
    print(massage)
except ZeroDivisionError as massage:
    print(massage)
except TypeError:
    print('В класс переданно недостаточно переменных')
