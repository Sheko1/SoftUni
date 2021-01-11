data = [int(i) for i in input().split(", ")]
min_wealth = int(input())

possible = True

for i in range(len(data)):
    if data[i] < min_wealth:
        wealthiest = max(data)
        index = data.index(wealthiest)
        amount = min_wealth - data[i]

        if data[index] - amount < min_wealth:
            possible = False
            break

        data[index] -= amount
        data[i] += amount

if possible:
    print(data)

else:
    print("No equal distribution possible")