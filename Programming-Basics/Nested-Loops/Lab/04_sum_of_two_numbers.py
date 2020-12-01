n = int(input())
n2 = int(input())
number = int(input())

count = 0
shebo = False

for i in range(n, n2+1):
    for j in range(n, n2+1):
        count += 1
        if i + j == number:
            print(f"Combination N:{count} ({i} + {j} = {i + j})")
            shebo = True
            break

    if shebo:
        break
if not shebo:
    print(f"{count} combinations - neither equals {number}")
