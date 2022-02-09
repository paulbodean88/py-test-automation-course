class Driver:
    def __init__(self, name):
        self._driver = name

    def __add__(self, other):
        return self._driver + other

    def __mul__(self, other):
        return self._driver * other

    def __str__(self):
        return f"I'm a driver for  {self._driver}"


if __name__ == '__main__':
    driver = Driver('Chrome')
    print(driver)
    print(driver + 'Firefox')
    print(driver * 4)
