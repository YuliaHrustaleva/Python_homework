
# импортировали из файла smartphone класс Smartphone
from smartphone import Smartphone

# создаем список-каталог
catalog = [
    Smartphone("Samsung", "Galaxy S24", "+79001112233"),
    Smartphone("Apple", "iPhone 15", "+79004445566"),
    Smartphone("Xiaomi", "13T", "+79007778899"),
    Smartphone("Huawei", "P60 Pro", "+79002223344"),
    Smartphone("Realme", "11 Pro", "+79005556677"),
]

# Цикл, который перебирает каждый смартфон в каталоге и печатает в заданном формате
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number_phone}")