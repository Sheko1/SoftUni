targets = [int(i) for i in input().split()]
command = input()

count = 0
while command != "End":
    index = int(command)

    if len(targets) > index >= 0:
        if targets[index] != -1:
            count += 1
            merfin = targets[index]
            targets[index] = -1

            for i in range(len(targets)):
                if targets[i] != -1:
                    if merfin < targets[i]:
                        targets[i] -= merfin
                    else:
                        targets[i] += merfin

    command = input()

print(f"Shot targets: {count} -> {' '.join(str(i) for i in targets)}")
