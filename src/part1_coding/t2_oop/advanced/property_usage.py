class TestCase:
    x = 'a'

    def __init__(self, nr_of_steps):
        self._nr_of_steps = nr_of_steps

    @property
    def steps(self):
        return self._nr_of_steps

    @steps.setter
    def steps(self, new_nr):
        if new_nr > self._nr_of_steps:
            self._nr_of_steps = new_nr * 22
        else:
            print(f'Same nr. of steps for this test {self._nr_of_steps}')

    @steps.getter
    def add_environment_setup_steps(self):
        return self._nr_of_steps * 2


tc = TestCase(5)
print(tc.steps)
tc.steps = 22
print(tc.steps)
print(tc.add_environment_setup_steps)
