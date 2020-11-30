items = input().split(", ")

command = input()

while command != "Craft!":
    data = command.split(" - ")

    if data[0] == "Collect":
        if data[1] not in items:
            items.append(data[1])

    elif data[0] == "Drop":
        if data[1] in items:
            items.remove(data[1])

    elif data[0] == "Combine Items":
        combine_items = data[1].split(":")
        if combine_items[0] in items:
            index = items.index(combine_items[0])
            items.insert(index + 1, combine_items[1])

    elif data[0] == "Renew":
        if data[1] in items:
            items.remove(data[1])
            items.append(data[1])

    command = input()

print(", ".join(items))