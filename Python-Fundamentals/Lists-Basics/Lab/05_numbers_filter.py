n = int(input())

even = []
odd = []
positive = []
negative = []

for i in range(n):
    number = int(input())

    if number % 2 == 0:
        even.append(number)

    if number % 2 != 0:
        odd.append(number)

    if number >= 0:
        positive.append(number)

    if number < 0:
        negative.append(number)

command1 = input()

if command1 == "even":
    print(even)

elif command1 == "odd":
    print(odd)

elif command1 == "positive":
    print(positive)

else:
    print(negative)
