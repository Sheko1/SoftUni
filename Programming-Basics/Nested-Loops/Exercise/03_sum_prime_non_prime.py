command = input()
prime = 0
non_prime = 0
count = 0
while command != "stop":
    number = int(command)

    if number < 0:
        number = 0
        print('Number is negative.')

    else:
        count = 0
        for i in range(1, number+1):
            if number % i == 0:
                count += 1

    if count == 2:
        prime += number

    else:
        non_prime += number

    command = input()
print(f'Sum of all prime numbers is: {prime}')
print(f'Sum of all non prime numbers is: {non_prime}')
