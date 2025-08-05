from faker import Faker

fake = Faker()

def register_new_courier():

    login = fake.user_name()
    password = fake.password()
    firstName = fake.name()
    reg_data = {
        "login": login,
        "password": password,
        "name": firstName
    }
    return reg_data


def register_new_courier_without_login():

    login = fake.user_name()
    firstName = fake.name()
    reg_data = {
        "login": login,
        "name": firstName
    }
    return reg_data


def register_new_courier_without_password():

    password = fake.password()
    firstName = fake.name()
    reg_data = {
        "password": password,
        "name": firstName
    }
    return reg_data