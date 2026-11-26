from faker import Faker
import csv

fake = Faker("pl_PL")

amount = 50

with open('employees.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['id_emp', 'name', 'surname', 'date_of_birth', 'account', 'base_salary', 'prov'])

    for i in range(amount):
        id_emp = i+1
        name = fake.first_name()
        surname = fake.last_name()
        date_of_birth = fake.date_of_birth(minimum_age=20, maximum_age=95)
        account = fake.iban()
        base_salary = fake.random_int(7000, 100000)
        prov = 0
            
        writer.writerow([id_emp, name, surname, date_of_birth, account, base_salary, prov])
        