text = input()

character = ""
number = ""
other = ""

for char in text:
    if char.isdigit():
        number += char

    elif char.isalpha():
        character += char

    else:
        other += char

print(number)
print(character)
print(other)
