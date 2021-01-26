def func_executor(*args):
    result = []
    for func_data in args:
        func, arg = func_data
        result.append(func(*arg))

    return result
