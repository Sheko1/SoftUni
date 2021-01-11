def shoot(index_1, power_1, list_1):
    if len(list_1) > index_1 >= 0:
        list_1[index_1] -= power_1

        if list_1[index_1] <= 0:
            list_1.pop(index_1)

    return targets


def add(index_1, value_1, list_1):
    if len(list_1) > index_1 >= 0:
        list_1.insert(index_1, value_1)

    else:
        print("Invalid placement!")

    return targets


def strike(index_1, radius_1, list_1):
    if index_1 + radius_1 < len(list_1) and index_1 - radius_1 >= 0:
        start = index_1 - radius_1
        end = index_1 + radius_1

        del list_1[start:end+1]

    else:
        print("Strike missed!")

    return targets


targets = [int(i) for i in input().split()]
command = input()

while command != "End":
    data = command.split(maxsplit=1)

    if data[0] == "Shoot":
        index, power = [int(i) for i in data[1].split()]
        shoot(index, power, targets)

    elif data[0] == "Add":
        index, value = [int(i) for i in data[1].split()]
        add(index, value, targets)

    elif data[0] == "Strike":
        index, radius = [int(i) for i in data[1].split()]
        strike(index, radius, targets)

    command = input()

print('|'.join(str(i) for i in targets))
