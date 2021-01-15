def input_elements(times):
    result = []
    for _ in range(times):
        result.extend(input().split())

    return result


def print_result(elements):
    for el in elements:
        print(el)


chemical_elements = input_elements(int(input()))

print_result(set(chemical_elements))