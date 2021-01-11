targets = input().split()
key = int(input())

result = []
index = 0
count = 0

while len(targets) > 0:
    target = ""
    count += 1

    if count == key:
        target = targets.pop(index)
        result.append(target)
        count = 0

    else:
        index += 1

    if index not in range(len(targets)):
        index = 0

print(f"[{','.join(result)}]")