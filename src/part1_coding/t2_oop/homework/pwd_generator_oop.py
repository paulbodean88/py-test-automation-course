import random


class PasswordGenerator:
    def __init__(self, length):
        self._length = length

    def password(self, uppercase=None, special=None, numbers=None):
        characters = list('abcdefghijklmnopqrstuvwxyz')
        if uppercase:
            characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if special:
            characters.extend('!@#$%^&*()')
        if numbers:
            characters.extend('0123456789')
        print(f'Pwd length is {self._length} ')
        the_password = ''
        for x in range(self._length):
            the_password += random.choice(characters)

        return the_password


class StrongPassword(PasswordGenerator):
    def set_pwd(self):
        self.password(True, True, True)


class WeakPassword(PasswordGenerator):
    def set_pwd(self):
        self.password()


pwd = PasswordGenerator(5)
my_pwd = pwd.password(True, True, True)
print(f'My password is {my_pwd}')
