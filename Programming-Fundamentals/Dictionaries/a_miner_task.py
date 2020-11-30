resources = {}

while True:
    key = input()

    if key == "stop":
        break

    value = int(input())

    if key not in resources:
        resources[key] = value

    else:
        resources[key] += value

[print(f"{key} -> {value}") for key, value in resources.items()]