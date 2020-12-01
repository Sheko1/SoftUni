events = input().split("|")

energy = 100
coins = 100
is_bankrupt = False

for i in events:
    event, value = i.split("-")
    value = int(value)

    if event == "rest":
        if value + energy > 100 and value >= 0:
            print("You gained 0 energy.")
        else:
            energy += value
            print(f"You gained {value} energy.")

        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy >= 30 and value >= 0:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")

        else:
            print("You had to rest!")
            energy += 50
            continue
    else:
        if coins - value > 0:
            coins -= value
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            is_bankrupt = True
            break

if not is_bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
