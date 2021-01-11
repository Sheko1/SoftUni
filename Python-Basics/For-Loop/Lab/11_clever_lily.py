age = int(input())
price = float(input())
toy_price = int(input())

money = 0
money1 = 0
num = 0
toy = 0


for i in range(2, age+1, 2):
    num += 10
    money1 += 1
    money += num

for i in range(1, age+1, 2):
    toy += 1

money -= money1
toy *= toy_price
total_money = money + toy

if total_money >= price:
    diff = total_money - price
    print(f"Yes! {diff:.2f}")
else:
    diff = price - total_money
    print(f"No! {diff:.2f}")
