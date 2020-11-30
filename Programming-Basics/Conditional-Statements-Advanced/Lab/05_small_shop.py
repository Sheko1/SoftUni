product = input()
city = input()
quantity = float(input())

if city == "Sofia":
    if product == "coffee":
        print(0.50 * quantity)

    elif product == "water":
        print(0.80 * quantity)

    elif product == "beer":
        print(1.20 * quantity)

    elif product == "sweets":
        print(1.45 * quantity)

    elif product == "peanuts":
        print(1.60 * quantity)

elif city == "Plovdiv":
    if product == "coffee":
        print(0.40 * quantity)

    elif product == "water":
        print(0.70 * quantity)

    elif product == "beer":
        print(1.15 * quantity)

    elif product == "sweets":
        print(1.30 * quantity)

    elif product == "peanuts":
        print(1.50 * quantity)

else:
    if product == "coffee":
        print(0.45 * quantity)

    elif product == "water":
        print(0.70 * quantity)

    elif product == "beer":
        print(1.10 * quantity)

    elif product == "sweets":
        print(1.35 * quantity)

    elif product == "peanuts":
        print(1.55 * quantity)
