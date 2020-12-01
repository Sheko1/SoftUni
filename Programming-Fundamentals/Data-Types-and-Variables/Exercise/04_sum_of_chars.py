n = int(input())
result = 0

for i in range(n):
    times = input()
    result += ord(times)

print(f"The sum equals: {result}")
