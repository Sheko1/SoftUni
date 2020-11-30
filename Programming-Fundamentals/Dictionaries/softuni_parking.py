n = int(input())
users = {}

for i in range(n):
    command = input().split(maxsplit=1)

    if command[0] == "register":
        username, license_num = command[1].split()

        if username not in users:
            users[username] = license_num
            print(f"{username} registered {license_num} successfully")

        else:
            print(f"ERROR: already registered with plate number {users[username]}")

    elif command[0] == "unregister":
        username = command[1]

        if username not in users:
            print(f"ERROR: user {username} not found")

        else:
            print(f"{username} unregistered successfully")
            users.pop(username)

[print(f"{key} => {value}") for key, value in users.items()]