words = [i.lower() for i in input().split()]
result = {}

for el in words:
    if el not in result:
        result[el] = 1

    else:
        result[el] += 1

[print(f"{key}", end=" ") for key, value in result.items() if value % 2 != 0]
