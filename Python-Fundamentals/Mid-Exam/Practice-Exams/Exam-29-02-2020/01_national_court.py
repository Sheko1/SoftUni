emp_1 = int(input())
emp_2 = int(input())
emp_3 = int(input())
people = int(input())

hour = 0
answers = emp_1 + emp_2 + emp_3

while people > 0:
    people -= answers
    hour += 1
    if hour % 4 == 0:
        hour += 1

print(f'Time needed: {hour}h.')
