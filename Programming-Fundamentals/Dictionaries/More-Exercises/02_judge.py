command = input()

contests_data = {}

while command != "no more time":
    data = command.split(" -> ")

    if data[1] not in contests_data:
        contests_data[data[1]] = {}
        contests_data[data[1]][data[0]] = int(data[2])

    else:
        if data[0] in contests_data[data[1]]:
            if int(data[2]) > contests_data[data[1]][data[0]]:
                contests_data[data[1]][data[0]] = int(data[2])

        else:
            contests_data[data[1]][data[0]] = int(data[2])

    command = input()

users = {}

for key, value in contests_data.items():
    value = sorted(value.items(), key=lambda x: (-x[1], x))
    print(f"{key}: {len(value)} participants")
    position = 1

    for user, points in value:
        if user not in users:
            users[user] = points
        else:
            users[user] += points

        print(f"{position}. {user} <::> {points}")
        position += 1

users = sorted(users.items(), key=lambda x: (-x[1], x))
position = 1
print("Individual standings:")
for user, points in users:
    print(f"{position}. {user} -> {points}")
    position += 1
