n = int(input())

students = {}

for i in range(n):
    key = input()
    value = float(input())

    if key not in students:
        students[key] = []
        students[key].append(value)

    else:
        students[key].append(value)

for key, value in students.items():
    students[key] = sum(value) / len(value)

students = dict(sorted(students.items(), key=lambda x: -x[1]))

[print(f"{key} -> {value:.2f}") for key, value in students.items() if value >= 4.5]