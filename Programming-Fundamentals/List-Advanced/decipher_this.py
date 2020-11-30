message = input().split()

for i in range(len(message)):
    cha_code = ""
    letters = []
    for j in range(len(message[i])):
        if message[i][j].isdigit():
            cha_code += message[i][j]

        if message[i][j].isalpha():
            letters.append(message[i][j])

    letters[0], letters[-1] = letters[-1], letters[0]
    print(f"{chr(int(cha_code))}{''.join(letters)}", end=" ")