n = int(input())

result = 0
result2 = 0

for i in range(n):
    number = int(input())
    result += number

for i in range(n):
    number2 = int(input())
    result2 += number2

if result == result2:
    print(f"Yes, sum = {result}")

else:
    diff = result - result2
    diff = abs(diff)
    print(f"No, diff = {diff}")
