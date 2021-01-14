sequences = int(input())

s = []

for _ in range(sequences):
    query = input()

    if query.startswith("1"):
        s.append(int(query.split()[1]))

    elif query.startswith("2") and s:
        s.pop()

    elif query.startswith("3") and s:
        print(max(s))

    elif query.startswith("4") and s:
        print(min(s))

result = []
while s:
    result.append(str(s.pop()))

print(", ".join(result))