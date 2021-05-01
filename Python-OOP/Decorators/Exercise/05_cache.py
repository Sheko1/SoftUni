import functools


def cache(func):
    func.log = {}

    @functools.wraps(func)
    def wrapper(n):
        if n not in func.log:
            func.log[n] = func(n)

        return func.log[n]

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(5))
print(fibonacci.log)
