from faker import Faker

fake = Faker()


def criar_usuario():
    return {
        "id": fake.random_int(),
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": "123456",
        "phone": fake.phone_number(),
    }