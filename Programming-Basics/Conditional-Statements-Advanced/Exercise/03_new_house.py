type_flower = input()
number_flower = int(input())
budget = int(input())

price = 0

if type_flower == "Roses":
    price = number_flower * 5
    if number_flower > 80:
        price = price * 0.9

elif type_flower == "Dahlias":
    price = number_flower * 3.8
    if number_flower > 90:
        price = price * 0.85

elif type_flower == "Tulips":
    price = number_flower * 2.8
    if number_flower > 80:
        price = price * 0.85

elif type_flower == "Narcissus":
    price = number_flower * 3
    if number_flower < 120:
        price = price + (price - price * 0.85)

else:
    price = number_flower * 2.5
    if number_flower < 80:
        price = price + (price - price * 0.8)


if budget >= price:
    money_left = budget - price
    print(f"Hey, you have a great garden with {number_flower} {type_flower} and {money_left:.2f} leva left.")

else:
    needed_money = price - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")
