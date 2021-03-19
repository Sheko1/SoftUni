def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def get_primes(numbers):
    for num in numbers:
        if is_prime(num) and num > 1:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0, 79])))
