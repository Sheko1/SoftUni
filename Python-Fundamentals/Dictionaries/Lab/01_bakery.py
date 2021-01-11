stock = input().split()
bakery = {}

for el in range(0, len(stock), 2):
    key = stock[el]
    value = int(stock[el+1])
    bakery[key] = value

print(bakery)
