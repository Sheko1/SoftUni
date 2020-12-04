def data(text):
    num_list = []
    non_num_list = []

    for char in text:
        if char.isdigit():
            num_list.append(int(char))

        else:
            non_num_list.append(char)

    return [num_list, non_num_list]


def take_skip_data(num_list):
    take_data = []
    skip_data = []

    for i in range(len(num_list)):
        if i % 2 == 0:
            take_data.append(num_list[i])

        else:
            skip_data.append(num_list[i])

    return [take_data, skip_data]


string = input()

number_list, non_number_list = data(string)
take_list, skip_list = take_skip_data(number_list)

result = ""

for i in range(len(take_list)):
    if take_list[i] != 0:
        result += "".join(non_number_list[:take_list[i]])
        del non_number_list[:take_list[i]]

    if skip_list[i] != 0:
        del non_number_list[:skip_list[i]]

print(result)