def tribonacci_sequence(n):
    data_list = []
    number = 1

    while len(data_list) != n:
        if len(data_list[-1:-4:-1]) >= 3:
            last_3_numbers = sum(data_list[-1:-4:-1])
            data_list.append(last_3_numbers)

        elif len(data_list) == 2:
            data_list.append(number + 1)

        else:
            data_list.append(number)

    data_list = [str(i) for i in data_list]
    return ' '.join(data_list)


num = int(input())

print(tribonacci_sequence(num))