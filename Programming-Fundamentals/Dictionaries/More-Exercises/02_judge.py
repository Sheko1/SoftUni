command = input()
participants_data = {}

while command != "no more time":
    data = command.split(" -> ")

    if data[1] not in participants_data:
        participants_data[data[1]] = {}

    if data[0] not in participants_data[data[1]]:
        participants_data[data[1]][data[0]] = int(data[2])

    else:
        if int(data[2]) > participants_data[data[1]][data[0]]:
            participants_data[data[1]][data[0]] = int(data[2])

    command = input()


participants_data = {key: dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
                     for key, value in participants_data.items()}

result = {}

for key, value in participants_data.items():
    print(f"{key}: {len(value)} participants")
    position = 1

    for user, points in value.items():
        if user not in result:
            result[user] = points

        else:
            result[user] += points

        print(f"{position}. {user} <::> {points}")
        position += 1

print("Individual standings:")
position = 1
result = sorted(result.items(), key=lambda x: -x[1])

for user, points in result:
    print(f"{position}. {user} -> {points}")
    position += 1