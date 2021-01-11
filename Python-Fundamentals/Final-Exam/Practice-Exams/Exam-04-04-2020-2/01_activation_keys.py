key = input()
command = input()

while command != "Generate":
    data = command.split(">>>", maxsplit=1)
    if data[0] == "Contains":
        substring = command.split(">>>")[1]
        if substring in key:
            print(f"{key} contains {substring}")

        else:
            print("Substring not found!")

    elif data[0] == "Flip":
        flip_type, start_index, end_index = data[1].split(">>>")

        start_index = int(start_index)
        end_index = int(end_index)
        flip = key[start_index:end_index]

        if flip_type == "Upper":
            key = key.replace(flip, flip.upper(), 1)

        else:
            key = key.replace(flip, flip.lower(), 1)

        print(key)

    elif data[0] == "Slice":
        start_index, end_index = data[1].split(">>>")

        start_index = int(start_index)
        end_index = int(end_index)

        key = key.replace(key[start_index:end_index], "", 1)

        print(key)

    command = input()

print(f"Your activation key is: {key}")
