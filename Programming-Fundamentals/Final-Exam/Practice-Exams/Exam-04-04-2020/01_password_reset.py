def take_odd(password):
    result = ""
    for i in range(len(password)):
        if i % 2 != 0:
            result += password[i]

    return result


def cut(index_1, length_1, password):
    sub_string = password[index_1:index_1+length_1]
    password = password.replace(sub_string, "", 1)
    return password


def substitute(old, new, password):
    if old in password:
        password = password.replace(old, new)
        return password

    else:
        return "Nothing to replace!"


string = input()
command = input()
while command != "Done":
    data = command.split(maxsplit=1)

    if data[0] == "TakeOdd":
        string = take_odd(string)
        print(string)

    elif data[0] == "Cut":
        index, length = data[1].split()
        index = int(index)
        length = int(length)

        string = cut(index, length, string)
        print(string)

    elif data[0] == "Substitute":
        sub_str, replace_str = data[1].split()

        if substitute(sub_str, replace_str, string) == "Nothing to replace!":
            print(substitute(sub_str, replace_str, string))

        else:
            string = substitute(sub_str, replace_str, string)
            print(string)

    command = input()

print(f"Your password is: {string}")
