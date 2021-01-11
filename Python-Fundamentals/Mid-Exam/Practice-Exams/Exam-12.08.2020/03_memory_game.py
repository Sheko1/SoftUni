elements = input().split()

command = input()
moves = 0
win = False
while command != "end":
    moves += 1
    data = command.split()
    index_1 = int(data[0])
    index_2 = int(data[1])

    if not win:
        if index_1 < 0 or index_1 > len(elements) - 1 or index_2 < 0 or index_2 > len(elements) - 1:
            middle = len(elements) // 2
            elements.insert(middle, f"-{moves}a")
            elements.insert(middle, f"-{moves}a")
            print("Invalid input! Adding additional elements to the board")

        elif elements[index_1] == elements[index_2]:
            element = elements[index_1]
            print(f"Congrats! You have found matching elements - {elements[index_1]}!")
            elements.remove(element)
            elements.remove(element)

        elif elements[index_1] != elements[index_2]:
            print("Try again!")

        if len(elements) == 0:
            print(f"You have won in {moves} turns!")
            win = True

    command = input()

if not win:
    print(f"Sorry you lose :(\n{' '.join(str(i) for i in elements)}")
