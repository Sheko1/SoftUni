lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

price = 0
count = 0

for i in range(1, lost_fights+1):
    if i % 2 == 0:
        price += helmet_price

    if i % 3 == 0:
        price += sword_price
        if i % 2 == 0:
            price += shield_price
            count += 1
            if count % 2 == 0:
                price += armor_price

print(f"Gladiator expenses: {price:.2f} aureus")
