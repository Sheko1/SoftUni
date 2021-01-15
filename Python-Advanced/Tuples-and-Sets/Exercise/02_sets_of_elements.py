def input_lines(times):
    result = set()
    for _ in range(times):
        result.add(int(input()))

    return result


def print_result(element):
    for el in element:
        print(el)


data = [int(n) for n in input().split()]
n_set = input_lines(data[0])
m_set = input_lines(data[1])


print_result(n_set.intersection(m_set))