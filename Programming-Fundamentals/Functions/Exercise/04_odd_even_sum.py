def odd_even_sum(num):
    odd_sum = 0
    even_sum = 0
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            even_sum += int(num[i])
        elif int(num[i]) % 2 != 0:
            odd_sum += int(num[i])
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
print(odd_even_sum(number))