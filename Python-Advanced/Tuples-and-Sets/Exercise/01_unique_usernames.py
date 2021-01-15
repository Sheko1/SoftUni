def input_lines(times):
    input_usernames = []
    for _ in range(times):
        input_usernames.append(input())

    return input_usernames


def print_result(usernames_data):
    for name in usernames_data:
        print(name)


n = int(input())
usernames = input_lines(n)

unique_usernames = set(usernames)
print_result(unique_usernames)
