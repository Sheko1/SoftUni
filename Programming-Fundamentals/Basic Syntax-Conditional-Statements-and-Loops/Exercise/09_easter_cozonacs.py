budget = float(input())
floor_price = float(input())

final_price = 0

eggs_price = floor_price * 0.75
milk_price = (floor_price + floor_price * 0.25) / 4
cozonacs_price = floor_price + eggs_price + milk_price
count = 0
eggs = 0
count1 = 0

while budget >= cozonacs_price:
    if budget > cozonacs_price:
        budget -= cozonacs_price
        final_price += cozonacs_price
        count += 1
        eggs += 3

        if count % 3 == 0:
            eggs -= count - 2

print(f"You made {count} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.")
