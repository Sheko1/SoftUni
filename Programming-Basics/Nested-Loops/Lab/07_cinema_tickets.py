film = input()

total_ticked = 0
student_ticked = 0
standard_ticked = 0
kid_ticked = 0

while film != "Finish":
    space = int(input())
    count = 0
    while count < space:
        ticked = input()

        if ticked == "student":
            student_ticked += 1
            count += 1

        elif ticked == "standard":
            standard_ticked += 1
            count += 1

        elif ticked == "kid":
            kid_ticked += 1
            count += 1

        if ticked == "End":
            break
    total_ticked += count
    print(f"{film} - {count / space * 100:.2f}% full.")
    film = input()

print(f'Total tickets: {total_ticked}')
print(f'{student_ticked / total_ticked * 100:.2f}% student tickets.')
print(f'{standard_ticked / total_ticked * 100:.2f}% standard tickets.')
print(f'{kid_ticked / total_ticked * 100:.2f}% kids tickets.')
