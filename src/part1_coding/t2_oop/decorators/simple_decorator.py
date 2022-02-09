# def test_one():
#     assert sum([1, 12], 2) == 15
#
#
# test_one()


def my_unit_test(func):
    def wrapper(a):
        print(f'my unit test started for {a}')
        func(a)
        print('my unit test ended')

    return wrapper


# @my_unit_test
# def test_one(a):
#     assert sum([1, 12], a) == 15
# test_one(1)

@my_unit_test
def test_2(a):
    assert a in [1, 2, 3]


test_2(1)
my_unit_test(test_2(3))

# test_one(1 + 1)
# test_2(2)
# my_unit_test(test_one)(2)
