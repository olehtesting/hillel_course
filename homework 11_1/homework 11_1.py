from typing import Generator

def prime_generator(end: int) -> Generator[int, None, None]:
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    for num in range(2, end + 1):
        if is_prime(num):
            yield num

if __name__ == "__main__":
    from inspect import isgenerator

    gen = prime_generator(1)
    assert isgenerator(gen) == True, 'Test0'
    assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
    assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
    assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
    print('Ok')