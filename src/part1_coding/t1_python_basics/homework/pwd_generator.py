import random


def password(length, uppercase=None, special=None, numbers=None):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if uppercase:
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    print(len(characters))
    if special:
        characters.extend('!@#$%^&*()')
    if numbers:
        characters.extend('0123456789')
    print(f'Pwd length is {length} ')
    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)

    # print(f'Another print {args[0]}')
    return the_password


my_pwd = password(5, numbers=True)
print(f'My password is {my_pwd}')
