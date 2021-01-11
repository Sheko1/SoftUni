n = int(input())
presentation = input()

grade2 = 0
count = 0
while presentation != "Finish":
    grade1 = 0
    for i in range(n):
        grade = float(input())
        grade1 += grade
        grade2 += grade
        count += 1

    print(f"{presentation} - {grade1 / n:.2f}.")
    presentation = input()

print(f"Student's final assessment is {grade2 / count:.2f}.")
