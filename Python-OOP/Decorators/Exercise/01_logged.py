import functools


def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        arguments = args + tuple(kwargs.values())
        result = func(*args, **kwargs)

        return f"you called {func_name}{arguments}\nit returned {result}"

    return wrapper


@logged
def function(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(sum_func(a=1, b=4))

print(func(4, 4, 4))
