number = int(input())

for i in range(1, number+1):
    sum_of_digits = 0
    for index, digit in enumerate(str(i)):
        sum_of_digits += int(digit)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{i} -> True")

    else:
        print(f"{i} -> False")
