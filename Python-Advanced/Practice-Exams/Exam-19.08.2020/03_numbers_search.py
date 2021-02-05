def numbers_searching(*args):
    received_numbers = []
    duplicates_numbers = []
    result = []

    for num in args:
        if num not in received_numbers:
            received_numbers.append(num)

        if args.count(num) > 1 and num not in duplicates_numbers:
            duplicates_numbers.append(num)

    received_numbers.sort()
    last_number = received_numbers[0] - 1

    for num in received_numbers:
        if num - last_number == 1:
            last_number = num
            continue

        result.append(num - 1)
        break

    duplicates_numbers.sort()
    result.append(duplicates_numbers)
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
