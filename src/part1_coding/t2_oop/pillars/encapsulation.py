class Encapsulation:
    def public(self):
        print("I'm public")

    def _protected(self):
        print("I'm protected")

    def __private(self):
        print("I'm private")

    def get(self):
        self.__private()


class Ch(Encapsulation):
    def test(self):
        self._protected()
        # self.__private()


father = Encapsulation()
father.public()
# father._protected()
# father.__private()
ch = Ch()
ch.test()
ch.get()
