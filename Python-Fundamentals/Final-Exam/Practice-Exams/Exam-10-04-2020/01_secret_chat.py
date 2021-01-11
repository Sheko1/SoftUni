message = input()
command = input()

while command != "Reveal":
    data = command.split(":|:")

    if data[0] == "InsertSpace":
        index = int(data[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif data[0] == "Reverse":
        substring = data[1]

        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)

        else:
            print("error")

    elif data[0] == "ChangeAll":
        substring = data[1]
        replacement = data[2]

        message = message.replace(substring, replacement)
        print(message)

    command = input()

print(f"You have a new text message: {message}")
