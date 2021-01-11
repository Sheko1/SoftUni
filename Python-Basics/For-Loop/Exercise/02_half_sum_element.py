import sys
n = int(input())

max_number = -sys.maxsize
result = 0
for i in range(n):
    num = int(input())
    if num > max_number:
        max_number = num
    result += num

result = result - max_number

if result == max_number:
    print("Yes")
    print(f"Sum = {result}")

else:
    diff = result - max_number
    diff = abs(diff)
    print("No")
    print(f"Diff = {diff}")
