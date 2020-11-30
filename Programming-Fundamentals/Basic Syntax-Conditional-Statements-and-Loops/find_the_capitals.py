word = input()

result = []

for index in range(len(word)):
    if word[index].isupper():
        result.append(index)

print(result)