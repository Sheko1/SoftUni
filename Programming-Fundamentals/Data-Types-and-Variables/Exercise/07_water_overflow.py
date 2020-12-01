n = int(input())

litters_1 = 255
litters_2 = 0

for i in range(n):
    litters = int(input())
    if litters <= litters_1:
        litters_1 -= litters
        litters_2 += litters
    else:
        print("Insufficient capacity!")

print(litters_2)
