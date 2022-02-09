from abc import ABC, abstractmethod


class TestModel(ABC):
    @abstractmethod
    def set_up(self):
        raise NotImplemented

    @abstractmethod
    def execute(self):
        raise NotImplemented

    @abstractmethod
    def tear_down(self):
        raise NotImplemented

    @abstractmethod
    def _test(self):
        # raise NotImplemented
        raise NotImplemented


class Tc1(TestModel):
    login = False

    def _test(self):
        pass

    def set_up(self):
        print('set')

    def execute(self):
        print('step 1')
        print('step 2')
        print('step 3')

    def tear_down(self):
        pass


tc2 = TestModel
tc1 = Tc1()
tc1.set_up()
