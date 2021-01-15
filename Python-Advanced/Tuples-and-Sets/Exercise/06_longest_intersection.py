def intersection_finder(first_range, second_range):
    if int(first_range[0]) >= int(second_range[0]):
        if int(first_range[1]) <= int(second_range[1]):
            intersection_data = (int(first_range[0]), int(first_range[1]))

        else:
            intersection_data = (int(first_range[0]), int(second_range[1]))

    else:
        if int(second_range[1]) <= int(first_range[1]):
            intersection_data = (int(second_range[0]), int(second_range[1]))

        else:
            intersection_data = (int(second_range[0]), int(first_range[1]))

    return [n for n in range(intersection_data[0], intersection_data[1]+1)]


def longest_intersection_checker(longest_itr_data, current_itr_data):
    if len(longest_itr_data) < len(current_itr_data):
        longest_itr_data = current_itr_data

    return longest_itr_data


def input_lines(times):
    result = []
    for _ in range(times):
        result.append(input())

    return result


ranges = input_lines(int(input()))

longest_intersection = []
for r in ranges:
    data = r.split("-")
    first_data = data[0].split(",")
    second_data = data[1].split(",")
    intersection = intersection_finder(first_data, second_data)

    longest_intersection = longest_intersection_checker(longest_intersection, intersection)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")