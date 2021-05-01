import functools
import time


def exec_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start

    return wrapper


@exec_time
def loop(start, end):
    total = 0

    for x in range(start, end):
        total += x

    return total


@exec_time
def concatenate(strings):
    result = ""

    for string in strings:
        result += string

    return result


print(loop(1, 10000000))
print(concatenate(["a" for i in range(1000000)]))
