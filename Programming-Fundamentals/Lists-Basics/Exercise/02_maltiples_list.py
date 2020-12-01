factor = int(input())
count = int(input())

numbers = []
num = 0

while len(numbers) < count:
    num += 1
    if num % factor == 0:
        numbers.append(num)

print(numbers)
