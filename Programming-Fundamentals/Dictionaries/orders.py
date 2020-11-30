commands = input()
products = {}

while commands != "buy":
    key, price, quantity = commands.split()
    price = float(price)
    quantity = int(quantity)

    if key not in products:
        products[key] = [price, quantity]

    else:
        if products[key][0] != price:
            products[key][0] = price

        products[key][1] += quantity

    commands = input()

[print(f"{key} -> {value[0] * value[1]:.2f}") for key, value in products.items()]