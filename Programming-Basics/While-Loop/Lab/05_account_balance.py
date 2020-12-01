command = input()

total = 0
increase = 0

while command != "NoMoreMoney":
    money = float(command)
    increase = money
    if increase < 0:
        print("Invalid operation!")
        break

    else:
        print(f"Increase: {increase:.2f}")

    command = input()
    total += money
print(f"Total: {total:.2f}")
