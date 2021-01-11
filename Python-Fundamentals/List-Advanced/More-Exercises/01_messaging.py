numbers = [list(i) for i in input().split()]
text = input()

result = ""

for i in numbers:
    index = 0
    number = 0

    for num in i:
        number += int(num)

    while number > 0:
        index += 1
        number -= 1
        if index not in range(len(text)):
            index = 0

    result += text[index]
    text = text[:index] + text[index+1:]
print(result)