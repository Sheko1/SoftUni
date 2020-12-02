numbers = [int(num) for num in input().split(", ")]

for index in range(len(numbers)):
    if numbers[index] == 0:
        numbers.remove(0)
        numbers.append(0)
print(numbers)