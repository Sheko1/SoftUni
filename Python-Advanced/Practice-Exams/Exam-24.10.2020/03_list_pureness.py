def best_list_pureness(numbers, k, str_to_return="", rotation=0, best_sum=0):
    if k < rotation:
        return str_to_return

    curr_sum = 0
    for i in range(len(numbers)):
        curr_sum += numbers[i] * i

    rotated_numbers = [numbers[-1]]
    for num in numbers[:-1]:
        rotated_numbers.append(num)

    if curr_sum > best_sum:
        str_to_return = f"Best pureness {curr_sum} after {rotation} rotations"
        best_sum = curr_sum

    return best_list_pureness(rotated_numbers, k, str_to_return, rotation + 1, best_sum)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
