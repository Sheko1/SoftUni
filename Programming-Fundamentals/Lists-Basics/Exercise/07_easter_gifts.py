gift = input().split()
command = input()
index = 0
while command != "No Money":
    data = command.split()
    if data[0] == "OutOfStock":
        if data[1] in gift:
            count = gift.count(data[1])
            for i in range(count):
                index = gift.index(data[1])
                gift[index] = None

    elif data[0] == "Required":
        index = int(data[2])
        if len(gift) - 1 > index and index >= 0:
            gift[index] = data[1]

    elif data[0] == "JustInCase":
        index = len(gift) - 1
        gift[index] = data[1]

    command = input()
    data = []

final_result = []

for i in range(len(gift)):
    if gift[i] is not None:
        final_result.append(gift[i])

print(*final_result)
