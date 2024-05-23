from typing import Callable, Generator

def pow(x: int) -> int:
    return x ** 2

def some_gen(begin: int, end: int, func: Callable[[int], int]) -> Generator[int, None, None]:
    """
    begin: перший елемент послідовності
    end: кількість елементів у послідовності
    func: функція, яка формує значення для послідовності
    """
    current = begin
    for _ in range(end):
        yield current
        current = func(current)

if __name__ == "__main__":
    from inspect import isgenerator

    gen = some_gen(2, 4, pow)
    assert isgenerator(gen) == True, 'Test1'
    assert list(gen) == [2, 4, 16, 256], 'Test2'
    print('OK')