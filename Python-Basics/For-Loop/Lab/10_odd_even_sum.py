n = int(input())

even = 0
odd = 0

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        even += num
    else:
        odd += num

if even == odd:
    print("Yes")
    print(f"Sum = {even}")

else:
    print("No")
    diff = even - odd
    diff = abs(diff)
    print(f"Diff = {diff}")
