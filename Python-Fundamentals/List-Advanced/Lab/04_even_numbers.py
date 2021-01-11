numbers = [int(num) for num in input().split(", ")]
even_numbers = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
print(even_numbers)
