def input_lines(n):
    lines = []
    for _ in range(n):
        lines.append(input())

    return lines


students = input_lines(int(input()))
students_data = {}

for data in students:
    student, grade = data.split()

    if student not in students_data:
        students_data[student] = []

    students_data[student].append(float(grade))

for student, grades in students_data.items():
    all_grades = ' '.join(map(lambda x: f"{x:.2f}", grades))
    avr_grade = f"{sum(grades) / len(grades):.2f}"
    print(f"{student} -> {all_grades} (avg: {avr_grade})")