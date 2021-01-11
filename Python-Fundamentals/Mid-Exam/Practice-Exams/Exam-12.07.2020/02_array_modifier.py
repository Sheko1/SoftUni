numbers = [int(num) for num in input().split()]
command = input()


while command != "end":
    data = command.split(maxsplit=1)

    if data[0] == "swap":
        index_1, index_2 = [int(i) for i in data[1].split()]

        numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]

    elif data[0] == "multiply":
        index_1, index_2 = [int(i) for i in data[1].split()]

        numbers[index_1] *= numbers[index_2]

    elif data[0] == "decrease":
        numbers = [num-1 for num in numbers]

    command = input()

print(", ".join(str(num) for num in numbers))
