numbers = [num for num in input().split() if num.lstrip("-").isdigit()]

s = []
result = ""

for char in numbers:
    s.append(char)

while s:
    result += s.pop() + " "

print(result)