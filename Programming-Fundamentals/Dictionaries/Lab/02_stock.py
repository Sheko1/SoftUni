stock = input().split()
bakery = {}

for el in range(0, len(stock), 2):
    key = stock[el]
    value = int(stock[el+1])
    bakery[key] = value

merfin = input().split()

for el in merfin:
    if el in bakery:
        print(f"We have {bakery[el]} of {el} left")

    else:
        print(f"Sorry, we don't have {el}")
