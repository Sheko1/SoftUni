command = input()
followers = {}

while command != "Log out":
    data = command.split(":")

    if data[0] == "New follower":
        user = data[1].strip()
        if user not in followers:
            followers[user] = 0

    elif data[0] == "Like":
        user = data[1].strip()
        count = int(data[2])

        if user not in followers:
            followers[user] = count

        else:
            followers[user] += count

    elif data[0] == "Comment":
        user = data[1].strip()

        if user not in followers:
            followers[user] = 1

        else:
            followers[user] += 1

    elif data[0] == "Blocked":
        user = data[1].strip()

        if user in followers:
            followers.pop(user)

        else:
            print(f"{user} doesn't exist.")

    command = input()

followers = sorted(followers.items(), key=lambda x: (-x[1], x[0]))

print(f"{len(followers)} followers")
[print(f"{key}: {value}") for key, value in followers]