quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

price = 0
count = 0
for i in range(1, days+1):
    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        price += ornament_set * quantity
        count += 5

    if i % 3 == 0:
        price += (tree_skirt * quantity) + (tree_garlands * quantity)
        count += 13

    if i % 5 == 0:
        price += tree_lights * quantity
        count += 17
        if i % 3 == 0:
            count += 30

    if i % 10 == 0:
        count -= 20
        price += tree_skirt + tree_garlands + tree_lights
        if i == days:
            count -= 30

print(f"Total cost: {price}")
print(f"Total spirit: {count}")
