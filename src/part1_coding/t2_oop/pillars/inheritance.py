class Base:
    def __init__(self, driver):
        self._browser = driver

    def open_browser(self):
        print(f'Open {self._browser} browser')

    def __str__(self):
        return f'Running tests on {self._browser}'


class TestSetup(Base):
    @staticmethod
    def set_up():
        print('set your test environment')

    @staticmethod
    def run_steps():
        print('Steps to be added')

    @staticmethod
    def tear_down(self):
        print('quit test')


class FirstTest(TestSetup):
    def run_steps(self):
        print('Step 1')
        print('Step 2')
        print('Step 3')


class SecondTest(TestSetup):
    def run_steps(self):
        print('Open the website')
        print('Click on login')
        print('Enter an invalid address')


if __name__ == '__main__':
    base = Base('Chrome')
    base.open_browser()
    print(base)
    second_test = SecondTest('Firefox')
    print(SecondTest.mro())
