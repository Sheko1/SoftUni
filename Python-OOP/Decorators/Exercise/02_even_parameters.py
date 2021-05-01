import functools


def even_parameters(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        params = args + tuple(kwargs.values())
        message = "Please use only even numbers!"

        for num in params:
            if not isinstance(num, int):
                return message

            elif num % 2 != 0:
                return message

        return func(*args, **kwargs)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


@even_parameters
def multiply(*nums):
    result = 1

    for num in nums:
        result *= num

    return result


print(add(2, 4))
print(add("Peter", 1))
print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
