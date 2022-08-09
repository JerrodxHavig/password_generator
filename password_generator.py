import string
import random

# Characters for password generation.
characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')


def random_password():
    """Generate random password."""

    # Get password length
    length = int(input('Enter password length: '))

    # Shuffle characters
    random.shuffle(characters)

    # Pick random characters from list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    # Shuffle password
    random.shuffle(password)

    # Print password
    print(''.join(password))


# Calling function
random_password()
