numbers = input()

data = numbers.split(" ")

for i in range(len(data)):
    num = int(data[i]) * -1
    data[i] = num
print(data)
