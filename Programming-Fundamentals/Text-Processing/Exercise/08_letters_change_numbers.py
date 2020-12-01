def position(character):
    character = character.lower()
    return ord(character) - 96


string = input().split()

result = 0

for word in string:
    number = ""
    for char in word:
        if char.isdigit():
            number += char

    number = int(number)
    
    if word[0].isupper():
        number /= position(word[0])

    else:
        number *= position(word[0])

    if word[-1].isupper():
        number -= position(word[-1])

    else:
        number += position(word[-1])

    result += number

print(f"{result:.2f}")