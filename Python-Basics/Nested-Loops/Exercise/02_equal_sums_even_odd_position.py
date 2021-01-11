start = int(input())
end = int(input())


for number in range(start, end+1):
    number_str = str(number)
    even_sum = 0
    odd_sum = 0
    for digit, index in enumerate(number_str):
        if int(digit) % 2 == 0:
            even_sum += int(index)

        else:
            odd_sum += int(index)
    if even_sum == odd_sum:
        print(str(number), end=" ")
