def list_manipulator(numbers, *args):
    command = args[0]
    where = args[1]
    param = [el for el in args[2:]]

    if command == "add":
        if where == "beginning":
            for i in range(len(param)):
                numbers.insert(i, param[i])

        elif where == "end":
            numbers.extend(param)

    elif command == "remove":
        amount = 1
        if len(param) > 0:
            amount = param[0]

        if where == "beginning":
            numbers = numbers[amount:]

        elif where == "end":
            numbers = numbers[:-amount]

    return numbers


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
