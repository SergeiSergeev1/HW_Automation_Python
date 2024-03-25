from address import Address
from mailing import Mailing

to_address = Address('111222', 'Moscow', 'Lesnaya street', '11', '33')
from_address = Address('115226', 'St.Petersburg', 'Nevsy Prjspekt', '136', '12')
my_mailing = Mailing(to_address, from_address, 100, '1432')

print('Отправление', my_mailing.track, 'из', my_mailing.from_address.index, ',', my_mailing.from_address.city, ',', my_mailing.from_address.street, ',', my_mailing.from_address.house, '-', my_mailing.from_address.apartment, 'в', my_mailing.to_address.index, ',', my_mailing.to_address.city, ',', my_mailing.to_address.street, ',', my_mailing.to_address.house, '-', my_mailing.to_address.apartment, '.' 'Стоимость', my_mailing.cost, 'рублей', '.')


