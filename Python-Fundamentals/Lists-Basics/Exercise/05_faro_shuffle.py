cards = input().split()
flush = int(input())

mid = int(len(cards) / 2)
data = []

for i in range(flush):
    data = []
    for j in range(mid):
        data.append(cards[j])
        data.append(cards[mid])
        mid += 1
    mid = int(len(cards) / 2)
    cards = data

print(data)
