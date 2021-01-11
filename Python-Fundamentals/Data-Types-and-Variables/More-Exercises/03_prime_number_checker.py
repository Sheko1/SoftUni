num = int(input())

count = 0

for n in range(1, num+1):
    if num % n == 0:
        count += 1

    if count > 2:
        break

if count > 2:
    print(False)

else:
    print(True)