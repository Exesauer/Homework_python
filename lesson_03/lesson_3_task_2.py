from smartphone import Smartphone

smartphone_1 = Smartphone('Motorolla', 'E398', 89004505401)
smartphone_2 = Smartphone('Samsung', 'C100', 89004505402)
smartphone_3 = Smartphone('Siemens', 'M55', 89004505403)
smartphone_4 = Smartphone('Nokia', '3310', 89004505404)
smartphone_5 = Smartphone('Poko', 'F5', 89004505405)

catalog = ([smartphone_1, smartphone_2, smartphone_3, smartphone_4, smartphone_5])

for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model}. {smartphone.phone_number}")