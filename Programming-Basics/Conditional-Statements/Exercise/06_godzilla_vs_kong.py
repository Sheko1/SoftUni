budget = float(input())
extra = int(input())
clothing = float(input())

decor = budget * 0.1
clothing_money = clothing * extra

if extra > 150:
    clothing_money = clothing_money - clothing_money * 0.1

total_money = decor + clothing_money
money_left = budget - total_money
money_left1 = total_money - budget
if total_money <= budget:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {money_left1:.2f} leva more.")
