import string
import random

# Characters for password generation.
characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')


def random_password():
    # Password length
    length = int(input('Password length: '))

    # Shuffle characters
    random.shuffle(characters)

    # Pick random character from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    # Shuffle password
    random.shuffle(password)

    print(''.join(password))


random_password()