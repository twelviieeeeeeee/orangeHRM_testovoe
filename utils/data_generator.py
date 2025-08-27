from faker import Faker

fake = Faker()

def random_name():
    firstname = fake.first_name()
    middlename = fake.first_name()
    lastname = fake.last_name()
    return firstname, middlename, lastname
