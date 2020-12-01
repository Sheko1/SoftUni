def exchange(number_list, index_0):
    if 0 <= index_0 < len(number_list):
        first_part = number_list[:index_0 + 1]
        second_part = number_list[index_0 + 1:]
        exchanged_list = second_part + first_part
        return exchanged_list

    else:
        print("Invalid index")
        return numbers_list


def max_odd_even(num_list, odd_or_even):
    list_even = []
    list_odd = []

    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            list_even.append(num_list[i])

        elif num_list[i] % 2 != 0:
            list_odd.append(num_list[i])

    index_1 = 0
    count = 0

    if odd_or_even == "odd":
        if len(list_odd) == 0:
            return "No matches"

        else:
            for i in range(len(num_list)):
                count += 1
                if num_list[i] == max(list_odd):
                    index_1 = i

    elif odd_or_even == "even":
        if len(list_even) == 0:
            return "No matches"
        else:
            for i in range(len(num_list)):
                count += 1
                if num_list[i] == max(list_even):
                    index_1 = i

    return index_1


def min_odd_even(num_list, odd_or_even):
    list_even = []
    list_odd = []

    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            list_even.append(num_list[i])

        elif num_list[i] % 2 != 0:
            list_odd.append(num_list[i])

    index_1 = 0
    count = 0

    if odd_or_even == "odd":
        if len(list_odd) == 0:
            return "No matches"

        else:
            for i in range(len(num_list)):
                count += 1
                if num_list[i] == min(list_odd):
                    index_1 = i

    elif odd_or_even == "even":
        if len(list_even) == 0:
            return "No matches"
        else:
            for i in range(len(num_list)):
                count += 1
                if num_list[i] == min(list_even):
                    index_1 = i

    return index_1


def first_count(list_of_number, odd_or_even, count):
    even_list = []
    odd_list = []

    if int(count) > len(list_of_number):
        return "Invalid count"

    for i in range(len(list_of_number)):
        if list_of_number[i] % 2 == 0:
            even_list.append(list_of_number[i])

        elif list_of_number[i] % 2 != 0:
            odd_list.append(list_of_number[i])

    if odd_or_even == "even":
        return_list = []
        count_range = int(count)

        if count_range > len(even_list):
            count_range = len(even_list)

        for i in range(count_range):
            return_list.append(even_list[i])

        return return_list

    else:
        return_list = []
        count_range = int(count)

        if count_range > len(odd_list):
            count_range = len(odd_list)

        for i in range(count_range):
            return_list.append(odd_list[i])

        return return_list


def last_count(list_numbers, odd_or_even, count):
    even_list = []
    odd_list = []

    if int(count) > len(list_numbers):
        return "Invalid count"

    for i in range(len(list_numbers)):
        if list_numbers[i] % 2 == 0:
            even_list.append(list_numbers[i])

        elif list_numbers[i] % 2 != 0:
            odd_list.append(list_numbers[i])

    if odd_or_even == "even":
        even_list.reverse()
        return_list = []
        count_range = int(count)

        if count_range > len(even_list):
            count_range = len(even_list)

        for i in range(count_range):
            return_list.append(even_list[i])

        return_list.reverse()
        return return_list

    else:
        odd_list.reverse()
        return_list = []
        count_range = int(count)

        if count_range > len(odd_list):
            count_range = len(odd_list)

        for i in range(count_range):
            return_list.append(odd_list[i])

        return_list.reverse()
        return return_list


numbers = input().split()
command = input().split()

numbers_list = list(map(int, numbers))

while command[0] != "end":
    if "exchange" in command:
        index = int(command[1])
        numbers_list = exchange(numbers_list, index)

    elif "max" in command:
        if command[1] == "odd":
            print(max_odd_even(numbers_list, command[1]))
        else:
            print(max_odd_even(numbers_list, command[1]))

    elif "min" in command:
        if command[1] == "odd":
            print(min_odd_even(numbers_list, command[1]))
        else:
            print(min_odd_even(numbers_list, command[1]))

    elif "first" in command:
        if command[2] == "odd":
            print(first_count(numbers_list, command[2], command[1]))

        else:
            print(first_count(numbers_list, command[2], command[1]))

    elif "last" in command:
        if command[2] == "odd":
            print(last_count(numbers_list, command[2], command[1]))

        else:
            print(last_count(numbers_list, command[2], command[1]))

    command = input().split()

print(numbers_list)