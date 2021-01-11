n = float(input())
a = n
count = 0

while n > 0:
    n = "{:.2f}".format(n)
    n = float(n)
    if n - 2.00 >= 0:
        n -= 2.00
        count += 1

    elif n - 1.00 >= 0:
        n -= 1.00
        count += 1

    elif n - 0.50 >= 0:
        n -= 0.50
        count += 1

    elif n - 0.20 >= 0:
        n -= 0.20
        count += 1

    elif n - 0.10 >= 0:
        n -= 0.10
        count += 1

    elif n - 0.05 >= 0:
        n -= 0.05
        count += 1

    elif n - 0.02 >= 0:
        n -= 0.02
        count += 1

    elif n - 0.01 >= 0:
        n -= 0.01
        count += 1

print(count)
