from collections import deque

water_quantity = int(input())
que = deque()

while True:
    command = input()

    if command == "Start":
        break
    que.append(command)

while True:
    command = input()

    if command == "End":
        print(f"{water_quantity} liters left")
        break

    if command.startswith("refill"):
        water_quantity += int(command.split()[1])

    else:
        if int(command) <= water_quantity:
            print(f"{que.popleft()} got water")
            water_quantity -= int(command)

        else:
            print(f"{que.popleft()} must wait")