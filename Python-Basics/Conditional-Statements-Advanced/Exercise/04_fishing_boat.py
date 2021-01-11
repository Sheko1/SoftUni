money = int(input())
season = input()
fisher_mans = int(input())

price = 0

if season == "Spring":
    price = 3000
    if fisher_mans <= 6:
        price = price * 0.9

    elif 7 <= fisher_mans <= 11:
        price = price * 0.85

    else:
        price = price * 0.75

elif season == "Summer" or season == "Autumn":
    price = 4200
    if fisher_mans <= 6:
        price = price * 0.9

    elif 7 <= fisher_mans <= 11:
        price = price * 0.85

    else:
        price = price * 0.75

else:
    price = 2600
    if fisher_mans <= 6:
        price = price * 0.9

    elif 7 <= fisher_mans <= 11:
        price = price * 0.85

    else:
        price = price * 0.75

if season != "Autumn" and fisher_mans % 2 == 0:
    price = price * 0.95

if money >= price:
    left_money = money - price
    print(f"Yes! You have {left_money:.2f} leva left.")

else:
    needed_money = price - money
    print(f"Not enough money! You need {needed_money:.2f} leva.")
