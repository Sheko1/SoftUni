travel = input()
command = input()

while command != "Travel":
    data = command.split(":", maxsplit=1)
    if "Add" in command:
        index, string = data[1].split(":")
        index = int(index)

        if index in range(len(travel)):
            travel = travel[:index] + string + travel[index:]

    elif "Remove" in command:
        start_index, end_index = data[1].split(":")
        start_index = int(start_index)
        end_index = int(end_index)

        if start_index in range(len(travel)) and end_index in range(len(travel)):
            travel = travel.replace(travel[start_index:end_index+1], "")

    elif "Switch" in command:
        old_str, new_str = data[1].split(":")

        if old_str in travel:
            travel = travel.replace(old_str, new_str)

    print(travel)

    command = input()

print(f"Ready for world tour! Planned stops: {travel}")
