n = int(input())
count = 0

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for i in range(n):
    num = int(input())
    count += 1
    if num < 200:
        count1 += 1

    if 200 <= num <= 399:
        count2 += 1

    if 400 <= num <= 599:
        count3 += 1

    if 600 <= num <= 799:
        count4 += 1

    if num >= 800:
        count5 += 1


p1 = count1 / count * 100
p2 = count2 / count * 100
p3 = count3 / count * 100
p4 = count4 / count * 100
p5 = count5 / count * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
