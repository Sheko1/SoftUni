usernames = input().split(", ")

is_valid = False

for user in usernames:
    if 3 <= len(user) <= 16:
        for char in user:
            if char.isdigit() or char.isalpha() or char == "-" or char == "_":
                is_valid = True

            else:
                is_valid = False
                break

        if is_valid:
            print(user)