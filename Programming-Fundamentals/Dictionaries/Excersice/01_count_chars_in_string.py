words = input().split()
char_counter = {}

for i in range(len(words)):
    for char in words[i]:
        if char not in char_counter:
            char_counter[char] = 1

        else:
            char_counter[char] += 1

[print(f"{key} -> {value}") for key, value in char_counter.items()]