from address import Address
from mailing import Mailing

from_addr = Address(101000,'Москва','Тверская', 10, 15)
to_addr = Address(102000,'Санкт-Петербург', 'Невский проспект', 1, 3)
price = int(500)
track_number = str('TRACK_№1323912')

mail = Mailing(from_addr, to_addr, price, track_number)

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. Стоимость {mail.cost} рублей.")

print(mail.from_address.index)