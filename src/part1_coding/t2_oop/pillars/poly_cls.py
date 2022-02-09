class Ro:
    def capital(self):
        print('Bucharest')

    def language(self):
        print('ro')


class DE:
    def capital(self):
        print('Berlin')

    def language(self):
        print('de')


class US:
    def capital(self):
        print('hi')

    def language(self):
        print('deaas')


ro = Ro()
de = DE()
sal = US()

for l in ro, de, sal:
    l.capital()
    l.language()
