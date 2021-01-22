data = input().split("|")
data.reverse()

result = [x.strip() for i in range(len(data)) for x in data[i].split()]
print(*result)
