from typing import Generator

def generate_cube_numbers(end: int) -> Generator[int, None, None]:
    n = 2
    while True:
        cube = n ** 3
        if cube >= end:
            return
        yield cube
        n += 1

if __name__ == "__main__":
    from inspect import isgenerator

    gen = generate_cube_numbers(1)
    assert isgenerator(gen) == True, 'Test0'
    assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
    assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
    assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729], '10 у кубі це 1000'
    print('Ok')