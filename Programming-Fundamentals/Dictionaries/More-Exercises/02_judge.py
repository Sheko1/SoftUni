command = input()
<<<<<<< HEAD

contests_data = {}
=======
participants_data = {}
>>>>>>> c38fe72b57b5b73a6da29ddee820a6f4ae3e0d77

while command != "no more time":
    data = command.split(" -> ")

<<<<<<< HEAD
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
=======
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
>>>>>>> c38fe72b57b5b73a6da29ddee820a6f4ae3e0d77

        print(f"{position}. {user} <::> {points}")
        position += 1

<<<<<<< HEAD
users = sorted(users.items(), key=lambda x: (-x[1], x))
position = 1
print("Individual standings:")
for user, points in users:
=======
print("Individual standings:")
position = 1
result = sorted(result.items(), key=lambda x: -x[1])

for user, points in result:
>>>>>>> c38fe72b57b5b73a6da29ddee820a6f4ae3e0d77
    print(f"{position}. {user} -> {points}")
    position += 1