# импортировали из файла address класс Address
# импортировали из файла mailing класс Mailing

from address import Address
from mailing import Mailing

# Создаём адреса
from_addr = Address("101000", "Москва", "Тверская", "1", "5")
to_addr = Address("630000", "Новосибирск", "Красный проспект", "10", "23")

# Создаём почтовое отправление
mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350,
    track="TRK123456789"
)

# Формируем и выводим информацию
print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)