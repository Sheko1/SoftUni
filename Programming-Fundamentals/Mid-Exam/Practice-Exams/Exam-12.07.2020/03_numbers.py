numbers = [int(num) for num in input().split()]
average = sum(numbers) / len(numbers)

result = []

for num in numbers:
    if num > average:
        result.append(num)

result = sorted(result, reverse=True)

if len(result) > 0:
    if len(result) > 5:
        print(" ".join(str(result[i]) for i in range(5)))

    else:
        print(" ".join(str(num) for num in result))

else:
    print("No")
