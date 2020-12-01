target_value = [int(i) for i in input().split()]
command = input()

while command != "End":
    data = command.split()

    if data[0] == "Shoot":
        index = int(data[1])
        value = int(data[2])

        if 0 <= index <= len(target_value)-1:
            if target_value[index] - value <= 0:
                target_value.pop(index)

            else:
                target_value[index] -= value

    elif data[0] == "Add":
        index = int(data[1])
        value = int(data[2])

        if 0 <= index < len(target_value):
            target_value.insert(index, value)

        else:
            print("Invalid placement!")

    elif data[0] == "Strike":
        index = int(data[1])
        radius = int(data[2])

        if index + radius >= len(target_value) or index - radius < 0:
            print("Strike missed!")

        else:
            start = index - radius
            end = index + radius

            del target_value[start:end+1]

    command = input()

result = list(map(str, target_value))
print("|".join(result))