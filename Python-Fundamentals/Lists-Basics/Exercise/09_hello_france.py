items = input().split("|")
budget = float(input())

profit_items = []
budget_1 = budget

for i in items:
    item, price = i.split("->")
    price = float(price)

    if (
        item == "Clothes" and 0 < price <= 50 or
        item == "Shoes" and 0 < price <= 35 or
        item == "Accessories" and 0 < price <= 20.50

    ):

        if budget >= price:
            budget -= price
            profit_items.append(price + price * 0.4)

final_money = sum(profit_items) + budget

for i in range(len(profit_items)):
    profit_items[i] = "{:.2f}".format(profit_items[i])

print(*profit_items)

print(f"Profit: {final_money - budget_1:.2f}")

if final_money >= 150:
    print("Hello, France!")

else:
    print("Time to go.")
