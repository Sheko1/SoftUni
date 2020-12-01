version = [int(i) for i in input().split(".")]

for i in range(len(version)):
    if version[i] == 9:
        if version[1] == 9 and version[-1] == 9:
            version[0] += 1
            version[1] = 0
            version[2] = 0
            break

        elif version[-1] == 9:
            version[i - 1] += 1
            version[i] = 0
            break

    elif i + 1 == len(version):
        version[i] += 1

result = list(map(str, version))
print(".".join(result))