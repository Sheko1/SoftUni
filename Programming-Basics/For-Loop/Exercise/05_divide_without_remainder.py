n = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(n):
    num = int(input())

    if num % 2 == 0:
        p1 += 1

    if num % 3 == 0:
        p2 += 1

    if num % 4 == 0:
        p3 += 1

p1_percent = p1 / n * 100
p2_percent = p2 / n * 100
p3_percent = p3 / n * 100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
