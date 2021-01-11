energy = int(input())
command = input()

battles = 0
win = True
while command != "End of battle":
    distance = int(command)

    if energy - distance >= 0:
        energy -= distance
        battles += 1

        if battles % 3 == 0:
            energy += battles

    else:
        win = False
        break

    command = input()

if not win:
    print(f"Not enough energy! Game ends with {battles} won battles and {energy} energy")

else:
    print(f"Won battles: {battles}. Energy left: {energy}")
