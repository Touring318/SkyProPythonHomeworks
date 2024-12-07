# Импортируем класс Smartphone
from smartphone import Smartphone

# Создаем 5 экземпляров класса Smartphone
smartphone1 = Smartphone("Xiaomi", "Redmi12", "+79139998877")
smartphone2 = Smartphone("Samsung", "A5", "+79538888877")
smartphone3 = Smartphone("Apple", "iPhone 15 pro", "+79539996677")
smartphone4 = Smartphone("POCO", "M6 PRO", "+79239998844")
smartphone5 = Smartphone("realme", "NOTE 50", "+79234232277")

# Создаем список из 5 созданных экземпляров класса Smartphone
catalog = [smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]
# Распечатываем содержимое экземпляров класса Smartphone из списка
x = 0
while x < len(catalog):
    print(f'{catalog[x].brand} - {catalog[x].model}. {catalog[x].phonenumber}')
    x += 1
