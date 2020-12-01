initial_list = input().split("!")
command = input()

while command != "Go Shopping!":
    data = command.split(maxsplit=1)

    if data[0] == "Urgent":
        if data[1] not in initial_list:
            initial_list.insert(0, data[1])

    elif data[0] == "Unnecessary":
        if data[1] in initial_list:
            initial_list.remove(data[1])

    elif data[0] == "Correct":
        old_item, new_item = data[1].split()
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list[index] = new_item

    elif data[0] == "Rearrange":
        if data[1] in initial_list:
            initial_list.remove(data[1])
            initial_list.append(data[1])

    command = input()

print(', '.join(initial_list))
