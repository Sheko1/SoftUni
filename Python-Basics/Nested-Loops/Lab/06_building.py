etaj = int(input())
stai = int(input())

for i in range(etaj, 0, -1):
    for j in range(stai):

        if i == etaj:
            print(f"L{i}{j}", end=" ")

        elif i % 2 == 0:
            print(f"O{i}{j}", end=" ")
        else:
            print(f"A{i}{j}", end=" ")
    print()
