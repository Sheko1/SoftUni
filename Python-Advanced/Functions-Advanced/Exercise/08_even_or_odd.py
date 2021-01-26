def even_odd(*args):
    if args[-1] == "even":
        return [num for num in args[:-1] if num % 2 == 0]

    elif args[-1] == "odd":
        return [num for num in args[:-1] if num % 2 != 0]
