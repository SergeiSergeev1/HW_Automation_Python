from smartphone import Smartphone

phone1 = Smartphone('iPhone', '13Pro', '+70010000001')
phone2 = Smartphone('iPhone', '11', '+70020000002')
phone3 = Smartphone('siemens', 'me45', '+70030000003')
phone4 = Smartphone('Sony', 'Xperia Z5 Compact', '+79040000004')
phone5 = Smartphone('Motorola', 'E398', '+79050000005')


catalog = phone1, phone2, phone3, phone4, phone5

for phone in catalog:
    print(phone.phone_brand, '-',phone.phone_model, '.', phone.phone_number)

