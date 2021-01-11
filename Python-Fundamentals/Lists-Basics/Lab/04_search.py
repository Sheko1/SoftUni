n = int(input())
word = input()

data = []
similar_data = []

for i in range(n):
    strings = input()
    data.append(strings)
    if word in strings:
        similar_data.append(strings)

print(data)
print(similar_data)
