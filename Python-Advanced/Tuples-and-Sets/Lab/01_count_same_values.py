data = [float(num) for num in input().split()]

occurrences_count = {}

for el in data:
    if el not in occurrences_count:
        occurrences_count[el] = 0

    occurrences_count[el] += 1

for key, value in occurrences_count.items():
    print(f"{key} - {value} times")
