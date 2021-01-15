def search_input(times):
    result = []
    for _ in range(times):
        result.append(input())

    return result


def people_input():
    lines = input()
    result = []

    while not lines.isdigit():
        result.append(lines)
        lines = input()

    return result, int(lines)


def print_result(contact, searches):
    for s in searches:
        if s in contact:
            print(f"{s} -> {contact[s]}")

        else:
            print(f"Contact {s} does not exist.")


peoples_input_data = people_input()
search = search_input(peoples_input_data[1])

peoples_data = {}
for p in peoples_input_data[0]:
    data = p.split("-")
    peoples_data[data[0]] = data[1]

print_result(peoples_data, search)