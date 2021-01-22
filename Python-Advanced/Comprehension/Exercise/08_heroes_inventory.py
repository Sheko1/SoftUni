inventory = {name: {} for name in input().split(", ")}
command = input()

while command != "End":
    data = command.split("-")

    if data[1] not in inventory[data[0]]:
        inventory[data[0]][data[1]] = int(data[2])

    command = input()

[print(f"{name} -> Items: {len(data)}, Cost: {sum(data.values())}") for name, data in inventory.items()]
