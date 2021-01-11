from math import ceil
students = int(input())
lectures = int(input())
bonus = int(input())

total_bonus = 0
max_bonus = 0
student_attendances = 0

for student in range(students):
    attendances = int(input())
    total_bonus = ceil((attendances / lectures) * (5 + bonus))

    if max_bonus <= total_bonus:
        max_bonus = total_bonus
        student_attendances = attendances

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {student_attendances} lectures.")
