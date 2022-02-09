"""

"""
import psutil


def get_virtual_memory():
    print(psutil.cpu_count())
    return psutil.virtual_memory().percent


mem = get_virtual_memory()
print(mem)


# nested function
def print_test_logs(msg):
    def logger():
        print(f'Logging memory data {msg}')

        def test():
            print('a')

        test()

    logger()


print_test_logs(mem)


# closure
def print_test_logs_3(msg):
    threshold = 90

    def logger():
        print(f'Logging memory data with closure {msg}. Keep an eye to the threshold {threshold}')

    return logger


x = print_test_logs_3(mem)()
# print_test_logs_3(mem)()
print(x)
