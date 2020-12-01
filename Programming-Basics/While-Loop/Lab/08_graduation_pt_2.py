name = input()

count = 1
count1 = 0
total_grades = 0

while count <= 12:
    grades = float(input())

    if grades < 4:
        count1 += 1

        if count1 == 2:
            break
    if grades >= 4:
        count += 1

    total_grades += grades
if count1 == 2:
    print(f"{name} has been excluded at {count} grade")
else:
    count -= 1
    print(f"{name} graduated. Average grade: {total_grades / count:.2f}")
