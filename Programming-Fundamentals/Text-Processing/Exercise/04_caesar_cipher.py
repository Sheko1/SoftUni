message = input()

result = ""

for char in message:
    result += chr(ord(char) + 3)

print(result)