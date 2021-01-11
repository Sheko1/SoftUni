command = input()

total = 0
taxes = 0
while command != "special" and command != "regular":
    price = float(command)
    if price >= 0:
        total += price
        taxes += price * 0.2

    else:
        print("Invalid price!")
    command = input()

total_price = total + taxes

if command == "special":
    total_price *= 0.9

if total == 0:
    print("Invalid order!")

else:
    print(f"""Congratulations you've just bought a new computer!
Price without taxes: {total:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {total_price:.2f}$""")
