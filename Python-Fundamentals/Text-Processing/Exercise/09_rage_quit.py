string = input().upper()

result = ""
unique_symbols = set()
last_index = 0
rahim = False
for i in range(len(string)):
    if rahim:
        rahim = False
        continue
    value = ""
    if string[i].isdigit():
        try:
            if string[i].isdigit() and string[i+1].isdigit():
                value = string[i]+string[i+1]
                rahim = True

            else:
                value = string[i]

        except Exception as e:
            metin = e
            value = string[i]

        value = int(value)
        text = ""
        for char in string[last_index:i]:
            if not char.isdigit():
                text += char
                if value != 0:
                    unique_symbols.add(char)

        result += text * value
        last_index = i

print(f"Unique symbols used: {len(unique_symbols)}")
print(result)