def rahim(product, quantity):
    result = None
    if product == "coffee":
        result = 1.5 * quantity
    elif product == "water":
        result = 1 * quantity
    elif product == "coke":
        result = 1.4 * quantity
    elif product == "snacks":
        result = 2 * quantity
    return result


metio = input()
sheko = int(input())

print(f"{rahim(metio, sheko):.2f}")
