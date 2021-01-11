key = int(input())
n = int(input())

result = ""

for _ in range(n):
    char = input()
    result += chr(ord(char)+key)

print(result)