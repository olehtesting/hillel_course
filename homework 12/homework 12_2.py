from typing import Dict


class Item:
    def __init__(self, name: str, price: float, description: str, dimensions: str):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self) -> str:
        return f'{self.name}, price: {self.price}, description: {self.description}, dimensions: {self.dimensions}'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Item):
            return (self.name, self.price, self.description, self.dimensions) == (
            other.name, other.price, other.description, other.dimensions)
        return False

    def __hash__(self) -> int:
        return hash((self.name, self.price, self.description, self.dimensions))


class User:
    def __init__(self, name: str, surname: str, patronymic: str, numberphone: str):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.numberphone = numberphone

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class Purchase:
    def __init__(self, user: User):
        self.user = user
        self.products: Dict[Item, int] = {}

    def add_item(self, item: Item, cnt: int) -> None:
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def get_total(self) -> float:
        return sum(item.price * quantity for item, quantity in self.products.items())

    def __str__(self) -> str:
        items_str = '\n'.join([f'{item.name}: {quantity} pcs.' for item, quantity in self.products.items()])
        return f'User: {self.user}\nItems:\n{items_str}'


if __name__ == "__main__":
    # Створення екземплярів товарів
    lemon = Item('lemon', 5, "yellow", "small")
    apple = Item('apple', 2, "red", "middle")

    # Виведення інформації про товар
    print(lemon)  # lemon, price: 5, description: yellow, dimensions: small
    print(apple)  # apple, price: 2, description: red, dimensions: middle

    # Створення екземпляра покупця
    buyer = User("Ivan", "Ivanov", "Petrovich", "02628162")
    print(buyer)  # Ivan Ivanov

    # Створення екземпляра замовлення і додавання товарів
    cart = Purchase(buyer)
    cart.add_item(lemon, 4)
    cart.add_item(apple, 20)
    print(cart)
    """
    User: Ivan Ivanov
    Items:
    lemon: 4 pcs.
    apple: 20 pcs.
    """
    # Перевірка правильності обчислення загальної вартості замовлення
    total = cart.get_total()
    print(f'Total after adding 4 lemons and 20 apples: {total}')
    assert total == 60, f'Всього 60! Зараз: {total}'

    # Додавання додаткової кількості товару
    cart.add_item(apple, 10)
    print(cart)
    """
    User: Ivan Ivanov
    Items:
    lemon: 4 pcs.
    apple: 30 pcs.
    """
    # Перевірка правильності обчислення загальної вартості замовлення після додавання товару
    total = cart.get_total()
    print(f'Total after adding 10 more apples: {total}')
    assert total == 80, f'Повинно залишатися 80! Зараз: {total}'