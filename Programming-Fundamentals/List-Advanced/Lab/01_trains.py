wagons = int(input())

train_wagons = [0] * wagons

command = input()

while not command == "End":
    data = command.split()

    if data[0] == "add":
        train_wagons[-1] += int(data[1])

    elif data[0] == "insert":
        index = int(data[1])
        train_wagons[index] += int(data[2])

    elif data[0] == "leave":
        index = int(data[1])
        train_wagons[index] -= int(data[2])

    command = input()

print(train_wagons)
