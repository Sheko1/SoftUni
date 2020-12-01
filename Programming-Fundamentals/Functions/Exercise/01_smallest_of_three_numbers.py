def smallest_number(num, num_1, num_2):
    if num < num_1 and num < num_2:
        return num
    elif num_1 < num and num_1 < num_2:
        return num_1
    elif num_2 < num and num_2 < num_1:
        return num_2


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(smallest_number(number_1, number_2, number_3))