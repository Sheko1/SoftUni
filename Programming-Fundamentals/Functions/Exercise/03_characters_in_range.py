def characters_range(cha_1, cha_2):
    result = []
    for i in range(ord(cha_1), ord(cha_2)):
        if i == ord(cha_1):
            continue
        result.append(chr(i))
    return " ".join(result)


character_1 = input()
character_2 = input()

print(characters_range(character_1, character_2))