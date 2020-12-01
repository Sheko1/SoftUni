houses = [int(i) for i in input().split("@")]
command = input()

index = 0
count = 0

while command != "Love!":
    data = command.split()
    index += int(data[1])

    if index > len(houses) - 1:
        index = 0
        houses[index] -= 2

    else:
        houses[index] -= 2

    if houses[index] == 0:
        count += 1
        print(f"Place {index} has Valentine's day.")

    elif houses[index] < 0:
        print(f"Place {index} already had Valentine's day.")

    command = input()

print(f"Cupid's last position was {index}.")

if len(houses) == count:
    print("Mission was successful.")

else:
    print(f"Cupid has failed {len(houses) - count} places.")