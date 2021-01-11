n = int(input())
rahim = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word not in rahim:
        rahim[word] = []
        rahim[word].append(synonym)

    else:
        rahim[word].append(synonym)

for key, value in rahim.items():
    print(f"{key} - {', '.join(value)}")
