text = input()

result = ""
last_char = ""

for i in range(len(text)):
    if last_char != text[i]:
        result += text[i]
        last_char = text[i]

print(result)