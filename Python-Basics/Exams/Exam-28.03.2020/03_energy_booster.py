fruit = input()
size = input()
sets = int(input())

price = 0

if fruit == "Watermelon":
    if size == "small":
        set_price = 56 * 2
        price = set_price * sets

    elif size == "big":
        set_price = 28.70 * 5
        price = set_price * sets

elif fruit == "Mango":
    if size == "small":
        set_price = 36.66 * 2
        price = set_price * sets

    elif size == "big":
        set_price = 19.60 * 5
        price = set_price * sets

elif fruit == "Pineapple":
    if size == "small":
        set_price = 42.10 * 2
        price = set_price * sets

    elif size == "big":
        set_price = 24.80 * 5
        price = set_price * sets

elif fruit == "Raspberry":
    if size == "small":
        set_price = 20 * 2
        price = set_price * sets

    elif size == "big":
        set_price = 15.20 * 5
        price = set_price * sets

if 400 <= price <= 1000:
    price *= 0.85

elif price > 1000:
    price *= 0.5

print(f"{price:.2f} lv.")
