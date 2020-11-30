string = input().split()

result = 0
rng = 0
str_1 = list(string[0])
str_2 = list(string[1])

if len(string[0]) > len(string[1]):
    rng = len(string[1])

else:
    rng = len(string[0])

for i in range(rng):
    result += ord(string[0][i]) * ord(string[1][i])
    str_1.remove(string[0][i])
    str_2.remove(string[1][i])

if len(str_1) > 0:
    for i in str_1:
        result += ord(i)

else:
    for i in str_2:
        result += ord(i)

print(result)