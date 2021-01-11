command = input()
result = []
while command != "End":
    data = command.split("-")
    result.extend(data)

    command = input()

result_1 = []
for i in range(1, len(result)+1):
    index = i - 1
    for j in range(len(result)):
        if str(i) == result[j]:
            result_1.append(result[j+1])
            break
print(result_1)
