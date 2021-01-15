def print_result(odd, even):
    if sum(odd) == sum(even):
        print(", ".join(map(str, odd.union(even))))

    elif sum(odd) > sum(even):
        print(", ".join(map(str, odd.difference(even))))

    else:
        print(", ".join(map(str, even.symmetric_difference(odd))))


def input_lines(times):
    input_result = []
    for _ in range(times):
        input_result.append(input())

    return input_result


names = input_lines(int(input()))
odd_set = set()
even_set = set()

for i in range(len(names)):
    result = 0
    for ch in names[i]:
        result += ord(ch)
    result //= (i + 1)

    if result % 2 == 0:
        even_set.add(result)

    else:
        odd_set.add(result)

print_result(odd_set, even_set)