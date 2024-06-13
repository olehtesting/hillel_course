from math import gcd


class Fraction:
    def __init__(self, a: int, b: int):
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        self.a = a
        self.b = b
        self._reduce()

    def _reduce(self):
        common_divisor = gcd(self.a, self.b)
        self.a //= common_divisor
        self.b //= common_divisor

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other: 'Fraction') -> bool:
        return self.a == other.a and self.b == other.b

    def __gt__(self, other: 'Fraction') -> bool:
        return self.a * other.b > other.a * self.b

    def __lt__(self, other: 'Fraction') -> bool:
        return self.a * other.b < other.a * self.b

    def __str__(self) -> str:
        return f"Fraction: {self.a}, {self.b}"


if __name__ == "__main__":
    f_a = Fraction(2, 3)
    f_b = Fraction(1, 2)  # Заміна на правильний дріб (3, 6 скорочується до 1, 2)

    # Перевірка додавання
    f_c = f_b + f_a
    assert str(f_c) == 'Fraction: 7, 6', str(f_c)

    # Перевірка множення
    f_d = f_b * f_a
    assert str(f_d) == 'Fraction: 1, 3', str(f_d)

    # Перевірка віднімання
    f_e = f_a - f_b
    assert str(f_e) == 'Fraction: 1, 6', str(f_e)

    # Перевірка порівняння
    assert f_d < f_c  # True
    assert f_d > f_e  # True
    assert f_a != f_b  # True

    # Перевірка рівності
    f_1 = Fraction(2, 4)
    f_2 = Fraction(1, 2)
    assert f_1 == f_2  # True
    print('OK')