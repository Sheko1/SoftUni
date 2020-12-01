message = input()
command = input()

while command != "Decode":
    data = command.split("|", maxsplit=1)

    if "Move" in command:
        move = int(data[1])

        move_str = message[:move]
        message = message.replace(move_str, "") + move_str

    elif "Insert" in command:
        index, value = data[1].split("|")
        index = int(index)

        message = message[:index] + value + message[index:]

    elif "ChangeAll" in command:
        sub_str, replace_str = data[1].split("|")
        message = message.replace(sub_str, replace_str)

    command = input()

print(f"The decrypted message is: {message}")
