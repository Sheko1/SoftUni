days = int(input())
type_room = input()
rating = input()

price = 0

if type_room == "room for one person" and rating == "positive":
    price = (days - 1) * 18
    price = price + price * 0.25

if type_room == "room for one person" and rating == "negative":
    price = (days - 1) * 18
    price = price - price * 0.1

if type_room == "apartment" and rating == "positive":
    if days < 10:
        price = ((days - 1) * 25) * 0.70
        price = price + price * 0.25

    elif 10 <= days <= 15:
        price = ((days - 1) * 25) * 0.65
        price = price + price * 0.25

    elif days > 15:
        price = ((days - 1) * 25) * 0.5
        price = price + price * 0.25

if type_room == "apartment" and rating == "negative":
    if days < 10:
        price = ((days - 1) * 25) * 0.70
        price = price * 0.9

    elif 10 <= days <= 15:
        price = ((days - 1) * 25) * 0.65
        price = price * 0.9

    elif days > 15:
        price = ((days - 1) * 25) * 0.5
        price = price * 0.9


if type_room == "president apartment" and rating == "positive":
    if days < 10:
        price = ((days - 1) * 35) * 0.90
        price = price + price * 0.25

    elif 10 <= days <= 15:
        price = ((days - 1) * 35) * 0.85
        price = price + price * 0.25

    elif days > 15:
        price = ((days - 1) * 35) * 0.80
        price = price + price * 0.25


if type_room == "president apartment" and rating == "negative":
    if days < 10:
        price = ((days - 1) * 35) * 0.90
        price = price * 0.9

    elif 10 <= days <= 15:
        price = ((days - 1) * 35) * 0.85
        price = price * 0.9

    elif days > 15:
        price = ((days - 1) * 35) * 0.80
        price = price * 0.9

print(f"{price:.2f}")
