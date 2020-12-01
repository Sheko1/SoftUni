command = input()

information = {}

while command != "End":
    key, value = command.split(" -> ")

    if key not in information:
        information[key] = []
        information[key].append(value)

    else:
        if value not in information[key]:
            information[key].append(value)

    command = input()

information = dict(sorted(information.items(), key=lambda x: x[0]))

for key, value in information.items():
    print(f"{key}")
    [print(f"-- {el}") for el in value]