from faker import Faker
import csv

fake = Faker("pl_PL")

amount = 100

with open('clients.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['id_clt', 'name', 'surname', 'pesel', 'tel', 'country', 'account'])

    for i in range(amount):
        id_clt = i+1
        name = fake.first_name()
        surname = fake.last_name()
        pesel = fake.pesel()
        tel = fake.phone_number()
        country = "Poland"
        account = fake.iban()
            
        writer.writerow([id_clt, name, surname, pesel, tel, country, account])
        