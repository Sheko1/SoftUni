import functools


def type_check(param_type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            params = args + tuple(kwargs.values())

            for param in params:
                if not isinstance(param, param_type):
                    return "Bad Type"

            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


@type_check(str)
def first_letter(word):
    return word[0]


print(times2(2))
print(times2('Not A Number'))
print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
