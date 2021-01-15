def input_lines(times):
    lines = []
    for _ in range(times):
        lines.append(input())

    return lines


def print_result(elements):
    for el in elements:
        print(el)


n = int(input())
names = input_lines(n)

unique_names = set()

for name in names:
    unique_names.add(name)

print_result(unique_names)