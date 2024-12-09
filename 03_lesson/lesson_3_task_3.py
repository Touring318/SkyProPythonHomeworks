# Импорт двух классов из других файлов
from address import Address
from mailing import Mailing

# Создание экземпляров класса Address для адресов назначения и отправления
to_address = Address(634099, 'г.Кемерово', 'пр.Ленина', 99, 15)
from_address = Address(635077, 'г.Новосибирск', 'ул.Строительная', 36, 24)

first_mailing = Mailing(to_address, from_address, 574, 1234567890)

print(first_mailing)
