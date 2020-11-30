rows = int(input())

ships = []
count = 0

for _ in range(rows):
    ships.append([int(ship) for ship in input().split()])

attacks = input().split()
for attack in attacks:
    row, col = attack.split("-")
    row = int(row)
    col = int(col)

    if ships[row][col] > 0:
        ships[row][col] -= 1
        if ships[row][col] == 0:
            count += 1
print(count)