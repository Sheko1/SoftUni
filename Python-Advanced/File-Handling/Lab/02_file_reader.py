from re import findall

with open("numbers.txt", "r") as file:
    numbers = "".join(file.readlines())
    numbers = findall(r"[0-9]+", numbers)

    print(sum([int(num) for num in numbers]))
