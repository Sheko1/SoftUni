command = input()

registered_students = {}

while command != "end":
    key, value = command.split(" : ")

    if key not in registered_students:
        registered_students[key] = []
        registered_students[key].append(value)

    else:
        registered_students[key].append(value)

    command = input()

registered_students = dict(sorted(registered_students.items(), key=lambda x: len(x[1]), reverse=True))

for key, value in registered_students.items():
    print(f"{key}: {len(value)}")
    [print(f"-- {name}") for name in sorted(value)]