def factorial_divide(num, num_1):
    factorial = 1
    factorial_1 = 1
    for i in range(1, num + 1):
        factorial = factorial * i

    for i in range(1, num_1 + 1):
        factorial_1 = factorial_1 * i

    return factorial / factorial_1


number = int(input())
number_1 = int(input())
print(f"{factorial_divide(number, number_1):.2f}")