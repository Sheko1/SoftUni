numbers = input()
num_beggars = int(input())

beggars = [0] * num_beggars

data = numbers.split(", ")

counter = 0

for i in range(len(data)):
    if counter == num_beggars:
        counter = 0
        beggars[counter] += int(data[i])
        counter += 1

    else:
        beggars[counter] += int(data[i])
        counter += 1

print(beggars)
