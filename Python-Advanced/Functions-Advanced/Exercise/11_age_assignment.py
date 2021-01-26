def age_assignment(*args, **kwargs):
    result = {}

    for name in args:
        result[name] = kwargs[name[0]]

    return result
