from itertools import permutations


def possible_permutations(data):
    result = permutations(data)
    for el in result:
        yield [*el]


[print(n) for n in possible_permutations([1, 2, 3])]
