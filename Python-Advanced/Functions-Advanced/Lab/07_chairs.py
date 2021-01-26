def combinations(list_data, n, comb=[]):
    if len(comb) == n:
        print(", ".join(comb))
        return

    for i in range(len(list_data)):
        comb.append(list_data[i])
        combinations(list_data[i+1:], n, comb)
        comb.pop()


combinations(input().split(", "), int(input()))
