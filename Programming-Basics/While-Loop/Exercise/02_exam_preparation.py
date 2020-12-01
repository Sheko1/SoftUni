bad_grade = int(input())

count = 0
average_score = 0
problems = 0
failed = True
last_tasks = ""

while count < bad_grade:
    task_name = input()

    if task_name == "Enough":
        failed = False
        break

    grades = int(input())

    if grades <= 4:
        count += 1

    problems += 1
    last_tasks = task_name
    average_score += grades

if failed:
    print(f"You need a break, {bad_grade} poor grades.")

else:
    print(f"Average score: {average_score / problems:.2f}")
    print(f"Number of problems: {problems}")
    print(f"Last problem: {last_tasks}")
