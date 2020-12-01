divisor = int(input())
bound = int(input())
number = 0
for i in range(1, bound+1):
    if i % divisor == 0:
        number = i
print(number)
