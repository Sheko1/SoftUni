needed_money = float(input())
owned_money = float(input())

count = 0
days = 0

while owned_money < needed_money and count < 5:
    command = input()
    money = float(input())
    days += 1

    if command == "save":
        count = 0
        owned_money += money

    elif command == "spend":
        count += 1
        owned_money -= money

    if owned_money < 0:
        owned_money = 0

if owned_money >= needed_money:
    print(f"You saved the money for {days} days.")

if count == 5:
    print(f"You can't save the money.")
    print(days)
