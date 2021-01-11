import sys
n = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize
max_number1 = -sys.maxsize
min_number1 = sys.maxsize
even = 0
odd = 0

for i in range(n):
    num = float(input())
    if i % 2 == 0:
        odd += num
        if num > max_number:
            max_number = num
            if num == 0:
                max_number = "No"
        if num < min_number:
            min_number = num
            if num == 0:
                min_number = "No"

    else:
        even += num
        if num > max_number1:
            max_number1 = num

        if num < min_number1:
            min_number1 = num

min_number1 = f"{min_number1:.2f}"
max_number1 = f"{max_number1:.2f}"
min_number = f"{min_number:.2f}"
max_number = f"{max_number:.2f}"

if even == 0:
    max_number1 = "No"
    min_number1 = "No"

if odd == 0:
    max_number = "No"
    min_number = "No"

print(f"OddSum={odd:.2f},")
print(f"OddMin={min_number},")
print(f"OddMax={max_number},")
print(f"EvenSum={even:.2f},")
print(f"EvenMin={min_number1},")
print(f"EvenMax={max_number1}")
