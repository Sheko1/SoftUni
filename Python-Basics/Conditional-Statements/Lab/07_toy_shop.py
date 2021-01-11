price_vac = float(input())
number_puzzle = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_cars = int(input())

price_puzzle = number_puzzle * 2.6
price_dolls = number_dolls * 3
price_bears = number_bears * 4.1
price_minions = number_minions * 8.2
price_cars = number_cars * 2
total_price = price_puzzle + price_dolls + price_bears + price_minions + price_cars

total_toys = number_puzzle + number_dolls + number_bears + number_minions + number_cars
if total_toys >= 50:
    price = total_price * 0.25
    total_price = total_price - price

rent = total_price * 0.1
profit = total_price - rent

remaining_money = profit - price_vac
needed_money = price_vac - profit

if profit >= price_vac:
    print(f"Yes! {remaining_money:.2f} lv left.")

else:
    print(f"Not enough money! {needed_money:.2f} lv needed.")
